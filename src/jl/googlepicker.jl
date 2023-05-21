# AUTO GENERATED FILE - DO NOT EDIT

export googlepicker

"""
    googlepicker(;kwargs...)

A GooglePicker component.

Keyword arguments:
- `id` (String; optional)
- `action` (String; optional)
- `client_id` (String; required)
- `developer_key` (String; required)
- `disabled_features` (String | Array of Strings; optional)
- `documents` (Dict; optional)
- `enabled_features` (String | Array of Strings; optional)
- `label` (String; required)
- `locale` (String; optional)
- `open` (Bool; optional)
- `scope` (String; optional)
- `selected_data` (Dict; optional)
- `value` (String; optional)
- `view_ids` (String | Array of Strings; optional)
"""
function googlepicker(; kwargs...)
        available_props = Symbol[:id, :action, :client_id, :developer_key, :disabled_features, :documents, :enabled_features, :label, :locale, :open, :scope, :selected_data, :value, :view_ids]
        wild_props = Symbol[]
        return Component("googlepicker", "GooglePicker", "dash_google_picker", available_props, wild_props; kwargs...)
end

