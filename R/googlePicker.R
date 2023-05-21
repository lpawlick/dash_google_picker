# AUTO GENERATED FILE - DO NOT EDIT

#' @export
googlePicker <- function(id=NULL, action=NULL, client_id=NULL, developer_key=NULL, disabled_features=NULL, documents=NULL, enabled_features=NULL, label=NULL, locale=NULL, open=NULL, scope=NULL, selected_data=NULL, value=NULL, view_ids=NULL) {
    
    props <- list(id=id, action=action, client_id=client_id, developer_key=developer_key, disabled_features=disabled_features, documents=documents, enabled_features=enabled_features, label=label, locale=locale, open=open, scope=scope, selected_data=selected_data, value=value, view_ids=view_ids)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'GooglePicker',
        namespace = 'dash_google_picker',
        propNames = c('id', 'action', 'client_id', 'developer_key', 'disabled_features', 'documents', 'enabled_features', 'label', 'locale', 'open', 'scope', 'selected_data', 'value', 'view_ids'),
        package = 'dashGooglePicker'
        )

    structure(component, class = c('dash_component', 'list'))
}
