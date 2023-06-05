import React, {Component} from 'react';
import PropTypes from 'prop-types';

export default class GooglePicker extends Component 
{
    constructor(props) 
    {
        super(props);
        this.state = 
        {
            pickerInited: false,
            gisInited: false,
            accessToken: null,
            open: props.open,
        }
        this.pickerCallback = this.pickerCallback.bind(this);
    }

    componentDidMount() 
    {
        this.loadGoogleApi();
        this.loadGoogleGsiClient();
    }

    loadGoogleApi() 
    {
        const script = document.createElement('script');
        script.src = 'https://apis.google.com/js/api.js';
        script.async = true;
        script.defer = true;
        script.onload = () => this.onApiLoad();
        document.body.appendChild(script);
    }

    onApiLoad() 
    {
        window.gapi.load('picker', () => this.setState({ pickerInited: true }));
    }

    loadGoogleGsiClient() 
    {
        const script = document.createElement('script');
        script.src = 'https://accounts.google.com/gsi/client';
        script.async = true;
        script.defer = true;
        script.onload = () => this.gisLoaded();
        document.body.appendChild(script);
    }

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

    createPicker() 
    {
        if(!this.state.pickerInited || !this.state.gisInited) 
        {
            console.error('Picker or GSI client is not initialized yet');
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

    pickerCallback(data) 
    {
        let action = data[window.google.picker.Response.ACTION];
        let documents = {};
    
        if (action === window.google.picker.Action.PICKED) 
        {
            let docsArray = data[window.google.picker.Response.DOCUMENTS];
            documents = Object.assign({}, docsArray);
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

    render() 
    {
        return (
            <React.Suspense fallback={null}>
                
            </React.Suspense>
        );
    }
}

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
    documents: {}
};

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
    documents: PropTypes.object
};

export const defaultProps = GooglePicker.defaultProps;
export const propTypes = GooglePicker.propTypes;