=========
Tutorial
=========

Prerequisites
--------------

Follow the official `Google Picker Guide <https://developers.google.com/drive/picker/guides/overview>`_ to create the required credentials.

Creating a the Google Picker
-----------------------------

.. code-block:: python

    from typing import List
    from dash import Dash, dcc, html, Input, Output, State, dcc
    from dash_google_picker import GooglePicker 
    from dash_google_picker.Documents import GoogleDocuments, GoogleDocument
    from dash_google_picker.Enums import ViewId
    import os

    app = Dash(__name__)

    app.layout = html.Div([
        html.Button('Open Google Picker', id='open-picker-button', n_clicks=0),
        GooglePicker(
            id='google-picker', # The unique component id
            client_id='GOOGLE_CLIENT_ID', # Your Google Client ID
            developer_key='GOOGLE_DEVELOPER_KEY' # Your Google Developer key
            view_ids=[ViewId.DOCS],
            enabled_features=[Feature.daa] # Enables multiselect
            ),
        dcc.Markdown(id='display-documents', style={'whiteSpace': 'pre-wrap'}),
        html.Div(id='display-action')
    ])

    if __name__ == '__main__':
        app.run_server(debug=True)

Create the google picker like every other dash component. 
The only required arguments are the unique `id`, the `client_id` and the `developer_key` which are both obtained from the google cloud console.
`view_ids` is optional but can be used to filter what document types should be show. Alternatively the :class:`~View` can be used which be use to restrict the files shown based on mimetypes or the :class:`~ViewGroup` which can group several Views together into a separate tab.
All possible view options can be found in the :class:`~ViewId` enum.

Lastly additional features like multiselect can be enabled or disabled with `enabled_features` or `disabled_features`. 
Some, if not all, appear to be experimental and subject to change. Additionally there appears to exist no documentation about them. 
At the time of writing all Features can be found in the enum :class:`~Feature` but any future features, which are not yet present in this enum, should be supported as well if just passed as a string.

Opening and closing the Picker
-------------------------------

.. code-block:: python

    @app.callback(
        Output('google-picker', 'open'),
        [Input('open-picker-button', 'n_clicks')],
        [State('google-picker', 'open')]
    )
    def open_google_picker(n_clicks, is_open):
        if n_clicks > 0:
            return not is_open
        return False

The picker can be opened and closed by setting the attribute `open` to `True` for open or `False` for closed.
It is generally recommended to use a toggle like shown above because the attribute can change unexpectedly due to user input.

Reacting to user action
------------------------

.. code-block:: python

    @app.callback(
        Output('display-action', 'children'),
        [Input('google-picker', 'action')],
        prevent_initial_call=True
    )
    def display_action(action):
        if action == "loaded":
            return "Opened the Google Picker Popup"
        elif action == "picked":
            return "Picked a document"
        elif action == "cancelled":
            return "Cancelled the Google Picker Popup"
        return f'Action: {action}'

The `action` attribute contains the current user action. If it is "loaded" then the user logged in with google and the google picker popup just opened.
If it is "picked" then the user selected a document and hit confirm, it is recommended to use the `documents` (see below) attribute instead if code should be run when documents were selected.
Lastly if the "action" is "cancelled" then the user logged in with google but closed the google picker without picking any documents.

Interacting with picked files
------------------------------

.. code-block:: python

    @app.callback(
        Output('display-documents', 'children'),
        [Input('google-picker', 'documents')],
        prevent_initial_call=True
    )
    def display_output(documents):
        docs : List[GoogleDocument] = GoogleDocuments(documents)
        doc_info = "\n".join([f"{prop}: {getattr(obj, prop)}" for obj in docs for prop in dir(obj) if not prop.startswith("__")])
        return doc_info

The `document` attribute contains the raw data (or `None`) when documents were selected. 
This raw data can be converted to a list of :class:`~GoogleDocument` with the help of :class:`~GoogleDocuments`.
A :class:`~GoogleDocument` is essentially just a dictionary, however certain keys might only be present with certain file types. 
All keys can be found `here <https://developers.google.com/drive/picker/reference#document>`_.
