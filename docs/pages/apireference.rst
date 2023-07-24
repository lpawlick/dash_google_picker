.. currentmodule:: dash_google_picker

===============
API Reference
===============

GooglePicker
=============

The Google Picker Python class

Usage:
::
    GooglePicker(
        id='google-picker',
        client_id='GOOGLE_CLIENT_ID',
        developer_key='GOOGLE_DEVELOPER_KEY',
        ),

Parameters
-----------

.. py:class:: GooglePicker

    :param id: A unique identifier for the component
    :type id: str
    :param open: If the picker should be opened immediately, defaults to `False`
    :type open: bool
    :param view_ids: What documents should be shown in the picker popup. All possible values can be found in :class:`~ViewId`. Defaults to ["all"]
    :type view_ids: List[str]
    :param client_id: The client ID for authenticating with the Google API.
    :type client_id: str
    :param scope: The api scope for this application, defaults to `https://www.googleapis.com/auth/drive.readonly`
    :type scope: str
    :param developer_key: The developer key for accessing the Google API.
    :type developer_key: str
    :param enabled_features: The features that should be enabled in the picker, all values can be found in :class:`~Feature`, defaults to `[]`
    :type enabled_features: List[str]
    :param disabled_features: The features that should be disabled in the picker, all values can be found in :class:`~Feature`, defaults to `[]`
    :type enabled_features: List[str]
    :param locale: The language of the google picker, all supported langauges can be found in the `Google Picker API Documentation <https://developers.google.com/drive/picker/guides/overview#i18n>`_, defaults to `None`.
    :type locale: str

.. note::
    Due to how props work in dash, there might be other valid parameters but setting them might break this component.

Documents
==========

Representation of the documents selected by the Google Picker

.. autoclass:: dash_google_picker.Documents.GoogleDocument
    :members:

.. autoclass:: dash_google_picker.Documents.GoogleDocuments
    :members:

Enums
======

Enums for filters and features

.. autoclass:: dash_google_picker.Enums.ViewId
    :members:

.. autoclass:: dash_google_picker.Enums.Feature
    :members:

GooglePicker React Component
==============================

The underlying react component for the Google Picker.

.. note::
    This is not available in the Python Environment, only when interacting with the react component directly

.. js:autoclass:: GooglePicker
    :short-name:

Prop Types
-----------

    .. js:autoattribute:: GooglePicker.propTypes.id
        :short-name:

    .. js:autoattribute:: GooglePicker.propTypes.open
        :short-name:

    .. js:autoattribute:: GooglePicker.propTypes.view_ids
        :short-name:

    .. js:autoattribute:: GooglePicker.propTypes.client_id
        :short-name:

    .. js:autoattribute:: GooglePicker.propTypes.scope
        :short-name:

    .. js:autoattribute:: GooglePicker.propTypes.developer_key
        :short-name:

    .. js:autoattribute:: GooglePicker.propTypes.enabled_features
        :short-name:

    .. js:autoattribute:: GooglePicker.propTypes.disabled_features
        :short-name:

    .. js:autoattribute:: GooglePicker.propTypes.locale
        :short-name:


Default Props
--------------

    .. js:autoattribute:: GooglePicker.defaultProps.open
        :short-name:

    .. js:autoattribute:: GooglePicker.defaultProps.view_ids
        :short-name:

    .. js:autoattribute:: GooglePicker.defaultProps.scope
        :short-name:

    .. js:autoattribute:: GooglePicker.defaultProps.enabled_features
        :short-name:

    .. js:autoattribute:: GooglePicker.defaultProps.disabled_features
        :short-name:

    .. js:autoattribute:: GooglePicker.defaultProps.locale
        :short-name:

Functions
-----------

    .. js:autofunction:: GooglePicker#componentDidMount
        :short-name:

    .. js:autofunction:: GooglePicker#loadGoogleApi
        :short-name:

    .. js:autofunction:: GooglePicker#loadGoogleGsiClient
        :short-name:
        
    .. js:autofunction:: GooglePicker#onApiLoad
        :short-name:
        
    .. js:autofunction:: GooglePicker#gisLoaded
        :short-name:
        
    .. js:autofunction:: GooglePicker#createPicker
        :short-name:
        
    .. js:autofunction:: GooglePicker#componentDidUpdate
        :short-name:
        
    .. js:autofunction:: GooglePicker#pickerCallback
        :short-name:
        
    .. js:autofunction:: GooglePicker#render
        :short-name:
