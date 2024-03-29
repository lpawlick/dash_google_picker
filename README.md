# Dash Google Picker
[![PyPI version](https://badge.fury.io/py/dash-google-picker.svg)](https://badge.fury.io/py/dash-google-picker)

The `dash_google_picker` is a Python module that allows the integration of Google's Picker API with a Dash application. The module provides a Dash component `GooglePicker` to easily implement the Google Picker functionality into your application, enabling your users to select files from their Google Drive account, among other data sources.

## Features

- Leverages Google Picker API for seamless integration with Google Drive.
- Allows selection of multiple files from Google Drive.
- Customizable views and features according to Google Picker API.

## [Documentation](https://docs.pawlick.dev/projects/dash_google_picker/)

## Installation

Use pip to install the package:

```bash
pip install dash-google-picker
```

## Prerequisites

Follow the official [Google Picker Guide](https://developers.google.com/drive/picker/guides/overview) to create the required credentials.

## Usage

The usage example below shows how to use the `GooglePicker` component in your Dash application.

```python
from typing import List
from dash import Dash, dcc, html, Input, Output, State, dcc
from dash_google_picker import GooglePicker 
from dash_google_picker.Documents import GoogleDocuments, GoogleDocument
import os

app = Dash(__name__)

app.layout = html.Div([
    html.Button('Open Google Picker', id='open-picker-button', n_clicks=0),
    GooglePicker(
        id='google-picker',
        client_id='GOOGLE_CLIENT_ID',
        developer_key='GOOGLE_DEVELOPER_KEY'
        ),
    dcc.Markdown(id='display-documents', style={'whiteSpace': 'pre-wrap'}),
    html.Div(id='display-action')
])

if __name__ == '__main__':
    app.run_server(debug=True)
```

The picker view can be customised, for more information see the `GooglePicker` component documentation or the [Google Picker API Documentation](https://developers.google.com/picker/docs/reference).

## Callbacks

The `GooglePicker` component generates two outputs `documents` and `action`. The `documents` output contains a list of documents selected by the user, and `action` contains the current action status.

```python
@app.callback(
    Output('google-picker', 'open'),
    [Input('open-picker-button', 'n_clicks')],
    [State('google-picker', 'open')]
)
def open_google_picker(n_clicks, is_open):
    if n_clicks > 0:
        return not is_open
    return False

@app.callback(
    Output('display-documents', 'children'),
    [Input('google-picker', 'documents')],
    prevent_initial_call=True
)
def display_output(documents):
    docs : List[GoogleDocument] = GoogleDocuments(documents)
    x = "\n".join([f"{prop}: {getattr(obj, prop)}" for obj in docs for prop in dir(obj) if not prop.startswith("__")])
    return x

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
```

## License

[MIT](https://github.com/lpawlick/dash_google_picker/blob/master/LICENSE) 
