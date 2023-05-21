# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class GooglePicker(Component):
    """A GooglePicker component.


Keyword arguments:

- id (string; optional)

- action (string; default '')

- client_id (string; required)

- developer_key (string; required)

- disabled_features (string | list of strings; optional)

- documents (dict; optional)

- enabled_features (string | list of strings; optional)

- label (string; required)

- locale (string; optional)

- open (boolean; default False)

- scope (string; default 'https://www.googleapis.com/auth/drive.readonly')

- selected_data (dict; optional)

- value (string; optional)

- view_ids (string | list of strings; default ['all'])"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_google_picker'
    _type = 'GooglePicker'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, label=Component.REQUIRED, value=Component.UNDEFINED, open=Component.UNDEFINED, selected_data=Component.UNDEFINED, view_ids=Component.UNDEFINED, client_id=Component.REQUIRED, scope=Component.UNDEFINED, developer_key=Component.REQUIRED, enabled_features=Component.UNDEFINED, disabled_features=Component.UNDEFINED, locale=Component.UNDEFINED, action=Component.UNDEFINED, documents=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'action', 'client_id', 'developer_key', 'disabled_features', 'documents', 'enabled_features', 'label', 'locale', 'open', 'scope', 'selected_data', 'value', 'view_ids']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'action', 'client_id', 'developer_key', 'disabled_features', 'documents', 'enabled_features', 'label', 'locale', 'open', 'scope', 'selected_data', 'value', 'view_ids']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['client_id', 'developer_key', 'label']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(GooglePicker, self).__init__(**args)
