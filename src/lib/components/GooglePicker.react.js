import React, {Component} from 'react';
import PropTypes from 'prop-types';

/**
 * GooglePicker Component.
 *
 * This component provides a Google file picker for the application.
 * The picker provides access to files stored in Google Drive.
 *
 * Props:
 * @prop {string} id - A unique identifier for the component.
 * @prop {string} label - A required label for the component.
 * @prop {string} value - A string value related to the component.
 * @prop {function} setProps - Function to update component's props.
 * @prop {bool} open - Determines if the picker is opened or not.
 * @prop {object} selected_data - The currently selected data.
 * @prop {(string|array)} view_ids - Google View IDs to be displayed in the picker.
 * @prop {string} client_id - The client_id of the Google Cloud application.
 * @prop {string} scope - The scopes for the Google Cloud application.
 * @prop {string} developer_key - The developer key of the Google Cloud application.
 * @prop {(string|array)} enabled_features - Features to enable in the picker.
 * @prop {(string|array)} disabled_features - Features to disable in the picker.
 * @prop {string} locale - The locale to be used in the picker.
 * @prop {string} action - The current action performed in the picker.
 * @prop {array} documents - The documents selected from the picker.
 *
 * State:
 * @state {bool} pickerInited - Indicates if the Google Picker API has been loaded.
 * @state {bool} gisInited - Indicates if the Google Sign-in API has been loaded.
 * @state {string} accessToken - The access token received from Google Sign-in.
 * @state {bool} open - Determines if the picker is opened or not.
 * @state {bool} pendingPicker - Indicates if there is a pending picker creation.
 *
 * Default Props:
 * @default {bool} open - false
 * @default {object} selected_data - {}
 * @default {array} view_ids - ['all']
 * @default {string} scope - 'https://www.googleapis.com/auth/drive.readonly'
 * @default {array} enabled_features - []
 * @default {array} disabled_features - []
 * @default {string} locale - null
 * @default {string} action - ''
 * @default {null} documents - null
 *
 * Methods:
 * @method loadGoogleApi - Loads Google API script.
 * @method loadGoogleGsiClient - Loads Google Sign-in script.
 * @method onApiLoad - Callback for Google API load.
 * @method gisLoaded - Callback for Google Sign-in load.
 * @method createPicker - Creates the Google Picker.
 * @method pickerCallback - Callback for Google Picker actions.
 */
export default class GooglePicker extends Component 
{

  /**
   * The constructor method is a special method for creating and initializing objects created with a class.
   * @param {Object} props - A collection of properties passed to the component.
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
   * A lifecycle method that gets called immediately after a component is mounted. 
   * This method is used to load Google API scripts and initialize the Google Picker.
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
   * This function is used to dynamically load Google API script into the HTML body.
   * @returns {Promise} Promise object represents the eventual completion or failure of loading Google API script.
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
   * This function is used to dynamically load Google One Tap script into the HTML body.
   * @returns {Promise} Promise object represents the eventual completion or failure of loading Google One Tap script.
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
   * This function is called after Google API script is loaded successfully. It initializes the Google Picker.
   */
    onApiLoad() 
    {
        window.gapi.load('picker', () => this.setState({ pickerInited: true }));
    }

  /**
   * This function is called after Google One Tap script is loaded successfully. It initializes Google One Tap client.
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
   * This function is used to create and display the Google Picker.
   * It also handles the access token needed for authorizing Google Drive access.
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
        
            // Assume that this.props.view_ids is an array of view id strings
            // If it is a single string, convert it into an array
            const viewIds = Array.isArray(this.props.view_ids) ? this.props.view_ids : [this.props.view_ids];
            viewIds.forEach(viewId => 
            {
                pickerBuilder.addView(window.google.picker[viewId] || window.google.picker.ViewId.DOCS);
            });
        
            // Enable features
            const enabledFeatures = Array.isArray(this.props.enabled_features) ? this.props.enabled_features : [this.props.enabled_features];
            enabledFeatures.forEach(feature => 
            {
                pickerBuilder.enableFeature(window.google.picker.Feature[feature]);
            });

            // Disable features
            const disabledFeatures = Array.isArray(this.props.disabled_features) ? this.props.disabled_features : [this.props.disabled_features];
            disabledFeatures.forEach(feature => 
            {
                pickerBuilder.disableFeature(window.google.picker.Feature[feature]);
            });

            // Set locale if provided
            if (this.props.locale) 
            {
                pickerBuilder.setLocale(this.props.locale);
            }

            const picker = pickerBuilder.build();
            picker.setVisible(true);
        }
        

        // Request an access token.
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
            // when establishing a new session.
            this.tokenClient.requestAccessToken({prompt: 'consent'});
        } 
        else 
        {
            // Skip display of account chooser and consent dialog for an existing session.
            this.tokenClient.requestAccessToken({prompt: ''});
        }
    }

  /**
   * A lifecycle method that gets called when a component's props have been changed. 
   * This method is used to update the component state and create Google Picker if the `open` prop is changed.
   * @param {Object} prevProps - A collection of properties of the component before update.
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
   * This function is a callback that gets called after the user selects any file/folder in Google Picker.
   * It updates the component state or props (if `setProps` is defined) based on the selected files/folders.
   * @param {Object} data - The response data from Google Picker after user selection.
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
            this.props.setProps({ action: action, documents: documents });
        } 
        else 
        {
            this.setState({ action: action, documents: documents });
        }
    }    

  /**
   * A lifecycle method that defines the render output of the component.
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
 * Default properties for the GooglePicker component.
 */
GooglePicker.defaultProps = 
{
    open: false,
    selected_data: {},
    view_ids: ['all'],
    scope: 'https://www.googleapis.com/auth/drive.readonly',
    enabled_features: [],
    disabled_features: [],
    locale: null,
    action: '',
    documents: null
};

/**
 * Typechecking for properties of the GooglePicker component.
 * This checks if the provided properties match the expected types.
 */
GooglePicker.propTypes = 
{
    id: PropTypes.string,
    label: PropTypes.string.isRequired,
    value: PropTypes.string,
    setProps: PropTypes.func,
    open: PropTypes.bool,
    selected_data: PropTypes.object,
    view_ids: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.arrayOf(PropTypes.string)
    ]),
    client_id: PropTypes.string.isRequired,
    scope: PropTypes.string,
    developer_key: PropTypes.string.isRequired,
    enabled_features: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.arrayOf(PropTypes.string)
    ]),
    disabled_features: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.arrayOf(PropTypes.string)
    ]),
    locale: PropTypes.string,
    action: PropTypes.string,
    documents: PropTypes.arrayOf(PropTypes.object)
};

export const defaultProps = GooglePicker.defaultProps;
export const propTypes = GooglePicker.propTypes;