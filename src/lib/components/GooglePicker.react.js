import React, {Component} from 'react';
import PropTypes from 'prop-types';

/**
 * Dash Google Picker
 *
 * This component provides a Google file picker for react.
 * Build for dash.
 *
 * Props:
 * @prop {string} id - A unique identifier for the component
 * @prop {bool} open - Determines if the picker is open
 * @prop {(string|object|array)} view_ids - What views should be shown in the picker. Deprecated views will return a 403 error and invalid views will return a 500 error.
 * @prop {string} client_id - The client_id of the Google Cloud application
 * @prop {string} scope - The scope for the Google Cloud application
 * @prop {string} developer_key - The developer key of the Google Cloud application
 * @prop {(string|array)} enabled_features - Features to enable in the picker
 * @prop {(string|array)} disabled_features - Features to disable in the picker
 * @prop {string} locale - The locale/language to be used by the picker
 *
 * State:
 * @state {bool} pickerInited - Indicates if the Google Picker API has been loaded
 * @state {bool} gisInited - Indicates if the Google Sign-in API has been loaded
 * @state {string} accessToken - The access token received from Google Sign-in
 * @state {bool} open - Determines if the picker is opened or not
 * @state {bool} pendingPicker - Indicates if there is a pending picker creation
 *
 * Default Props:
 * @default {bool} open - false
 * @default {array} view_ids - ['all']
 * @default {string} scope - 'https://www.googleapis.com/auth/drive.readonly'
 * @default {array} enabled_features - []
 * @default {array} disabled_features - []
 * @default {string} locale - null
 *
 * Methods:
 * @method loadGoogleApi - Loads Google API script
 * @method loadGoogleGsiClient - Loads Google Sign-in script
 * @method onApiLoad - Callback for Google API load
 * @method gisLoaded - Callback for Google Sign-in load
 * @method createPicker - Creates the Google Picker
 * @method pickerCallback - Callback for Google Picker actions
 */
class GooglePicker extends Component 
{
    /**
   * Creates the React/Dash component.
   * @param {Object} props - A collection of properties passed to the component
   */
    constructor(props) 
    {
        super(props);
        this.state = 
        {
            pickerInited: false,
            gisInited: false,
            accessToken: null,
            open: props.open,
            pendingPicker: false,
        }
        this.pickerCallback = this.pickerCallback.bind(this);
    }

    /**
   * A lifecycle method that gets called immediately after a component is mounted
   * This method is used to load Google API scripts and initialize the Google Picker
   */
    async componentDidMount() 
    {
        try 
        {
            await Promise.all([this.loadGoogleApi(), this.loadGoogleGsiClient()]);
            if (this.state.pendingPicker) 
            {
                this.createPicker();
            }
        } 
        catch (error)
        {
            console.error(error);
        }
    }
    

    /**
   * This function is used to dynamically load Google API script into the HTML body
   * @returns {Promise} Promise object represents the eventual completion or failure of loading Google API script
   */
    loadGoogleApi() 
    {
        return new Promise((resolve, reject) => 
        {
            const script = document.createElement('script');
            script.src = 'https://apis.google.com/js/api.js';
            script.async = true;
            script.defer = true;
            script.onload = () => resolve(this.onApiLoad());
            script.onerror = () => reject(new Error('Failed to load Google API script'));
            document.body.appendChild(script);
        });
    }
    
    /**
   * This function is used to dynamically load Google gsi client script into the HTML body
   * @returns {Promise} Promise object represents the eventual completion or failure of loading Google gsi client
   */
    loadGoogleGsiClient() 
    {
        return new Promise((resolve, reject) => 
        {
            const script = document.createElement('script');
            script.src = 'https://accounts.google.com/gsi/client';
            script.async = true;
            script.defer = true;
            script.onload = () => resolve(this.gisLoaded());
            script.onerror = () => reject(new Error('Failed to load Google GSI Client script'));
            document.body.appendChild(script);
        });
    }

    /**
   * This function is called after Google API script is loaded successfully
   */
    onApiLoad() 
    {
        window.gapi.load('picker', () => this.setState({ pickerInited: true }));
    }

    /**
   * This function is called after Google One Tap script is loaded successfully
   */
    gisLoaded() 
    {
        this.tokenClient = window.google.accounts.oauth2.initTokenClient(
        {
            client_id: this.props.client_id,
            scope: this.props.scope,
            callback: '', // defined later
        });
        this.setState({ gisInited: true });
    }

    /**
   * This function is used to create and display the Google Picker
   * It also handles the access token needed for authorizing Google Drive access
   */
    createPicker() 
    {
        if(!this.state.pickerInited || !this.state.gisInited) 
        {
            this.setState({ shouldShowPicker: true });
            return;
        }

        const showPicker = () => 
        {
            const pickerBuilder = new window.google.picker.PickerBuilder()
                .setOAuthToken(this.state.accessToken)
                .setDeveloperKey(this.props.developer_key)
                .setCallback(this.pickerCallback);
        
            // Generate real viewgroups from the converted python data
            const create_view_group = (view_group) =>
            {
                var viewGroup = new window.google.picker.ViewGroup(create_view(view_group.views[0]))
                for (var i = 1; i < view_group.views.length; i++) 
                {
                    var viewToAdd = view_group.views[i];
                    if (typeof viewToAdd === 'string')
                    {
                        viewGroup.addView(viewToAdd);
                    }
                    else if (typeof viewToAdd === 'object')
                    {
                        console.log(viewToAdd)
                        if (viewToAdd.type === "ViewGroup") 
                        {
                            viewGroup.addView(create_view_group(viewToAdd));
                        }
                        if (viewToAdd.type === "View") 
                        {
                            viewGroup.addView(create_view(viewToAdd));
                        }
                    }
                }
                if (view_group.label)
                {
                    viewGroup.addLabel(view_group.label)
                }
                return viewGroup;
            }

            // Generate a real view from the converted python data
            const create_view = (view_struct) =>
            {
                // Check if view_struct is actually a viewId
                if (typeof view_struct === 'string')
                {
                    return new window.google.picker.View(view_struct)
                }
                var view = new window.google.picker.View(view_struct.viewId)
                if (view_struct.mimeTypes)
                {
                    if (typeof view_struct.mimeTypes === 'string')
                    {
                        view_struct.mimeTypes = view_struct.mimeTypes
                    }
                    else
                    {
                        view.setMimeTypes(view_struct.mimeTypes.join(','));
                    }
                }
                if (view_struct.query)
                {
                    view.setQuery(view_struct.query);
                }
                return view;
            }

            // Views can either be a viewid or a viewgroup, or an array containing any combination of the two
            const views = Array.isArray(this.props.view_ids) ? this.props.view_ids : [this.props.view_ids];
            views.forEach(view => 
            {
                if (typeof view === 'string') 
                {
                    pickerBuilder.addView(view);
                } 
                else if (typeof view === 'object')
                {
                    if (view.type === "View") 
                    {
                        pickerBuilder.addView(create_view(view));
                    }
                    if (view.type === "ViewGroup") 
                    {
                        pickerBuilder.addViewGroup(create_view_group(view));
                    }
                }
            });
        
            // Enable features
            const enabledFeatures = Array.isArray(this.props.enabled_features) ? this.props.enabled_features : [this.props.enabled_features];
            enabledFeatures.forEach(feature => 
            {
                pickerBuilder.enableFeature(feature);
            });

            // Disable features
            const disabledFeatures = Array.isArray(this.props.disabled_features) ? this.props.disabled_features : [this.props.disabled_features];
            disabledFeatures.forEach(feature => 
            {
                pickerBuilder.disableFeature(feature);
            });

            // Set locale if provided
            if (this.props.locale) 
            {
                pickerBuilder.setLocale(this.props.locale);
            }

            const picker = pickerBuilder.build();
            picker.setVisible(true);
        }
        

        // Request an access token
        this.tokenClient.callback = async (response) => 
        {
            if (response.error !== undefined) 
            {
                throw (response);
            }
            this.setState({ accessToken: response.access_token });
            showPicker();
        };

        if (this.state.accessToken === null) 
        {
            // Prompt the user to select a Google Account and ask for consent to share their data
            // when establishing a new session
            this.tokenClient.requestAccessToken({prompt: 'consent'});
        } 
        else 
        {
            // Skip display of account chooser and consent dialog for an existing session
            this.tokenClient.requestAccessToken({prompt: ''});
        }
    }

    /**
   * A lifecycle method that gets called when a component's props have been changed
   * This method is used to update the component state and create Google Picker Popup if the `open` prop is changed
   * @param {Object} prevProps - A collection of properties of the component before update
   */
    componentDidUpdate(prevProps) 
    {
        if(this.props.open !== prevProps.open) 
        {
            this.setState({ open: this.props.open }, () => 
            {
                this.createPicker();
            });
        }
    }

    /**
   * This function is a callback that gets called after the user selects any file/folder in Google Picker
   * It updates the component state based on the selected files/folders
   * @param {Object} data - The response data from Google Picker after user selection
   */
    pickerCallback(data) 
    {
        let action = data[window.google.picker.Response.ACTION];
        let documents = null;

        if (action === window.google.picker.Action.PICKED) 
        {
            documents = data[window.google.picker.Response.DOCUMENTS];
        }
        if (this.props.setProps) 
        {
            this.props.setProps({ action: action, ...(documents && {documents: documents}) });
        } 
        else 
        {
            this.setState({ action: action, ...(documents && {documents: documents}) });
        }
    }

    /**
   * A lifecycle method that defines the render output of the component
   */
    render() 
    {
        return (
            <React.Suspense fallback={null}>
                
            </React.Suspense>
        );
    }
}

/**
 * Default properties for the GooglePicker component
 */
GooglePicker.defaultProps = 
{
    /**
     * The picker popup is closed by default
     */
    open: false,
    /**
     * No filtering by default
     */
    view_ids: ['all'],
    /**
     * The read only scope is enough to pick a document
     */
    scope: 'https://www.googleapis.com/auth/drive.readonly',
    /**
     * No extra features enabled by default
     */
    enabled_features: [],
    /**
     * No features disabled by default
     */
    disabled_features: [],
    /**
     * No default locale set
     */
    locale: null,
    action: '',
    documents: null
};

/**
 * Typechecking for properties of the GooglePicker component
 * This checks if the provided properties match the expected types
 */
GooglePicker.propTypes = 
{
    /**
     * A unique identifier for the component
     */
    id: PropTypes.string.isRequired,
    
    /**
     * Function to update component's props
     */
    setProps: PropTypes.func,

    /**
     * Determines if the picker is opened or not
     */
    open: PropTypes.bool,

    /**
     * Google View IDs to be displayed in the picker
     */
    view_ids: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object,
        PropTypes.arrayOf(PropTypes.string),
        PropTypes.arrayOf(PropTypes.object),
        PropTypes.arrayOf(PropTypes.string, PropTypes.object),
    ]),

    /**
     * The client_id of the Google Cloud application
     */
    client_id: PropTypes.string.isRequired,

    /**
     * The scopes for the Google Cloud application
     */
    scope: PropTypes.string,

    /**
     * The developer key of the Google Cloud application
     */
    developer_key: PropTypes.string.isRequired,

    /**
     * Features to enable in the picker
     */
    enabled_features: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.arrayOf(PropTypes.string)
    ]),

    /**
     * Features to disable in the picker
     */
    disabled_features: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.arrayOf(PropTypes.string)
    ]),

    /**
     * The locale to be used in the picker
     */
    locale: PropTypes.string,

    /**
     * The current action performed in the picker
     */
    action: PropTypes.string,

    /**
     * The documents selected from the picker
     */
    documents: PropTypes.arrayOf(PropTypes.object)
};

export const defaultProps = GooglePicker.defaultProps;
export const propTypes = GooglePicker.propTypes;
export default GooglePicker;