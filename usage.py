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
        client_id=os.getenv('GOOGLE_CLIENT_ID'),
        developer_key=os.getenv('GOOGLE_DEVELOPER_KEY')
        ),
    dcc.Markdown(id='display-documents', style={'whiteSpace': 'pre-wrap'}),
    html.Div(id='display-action')
])

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

if __name__ == '__main__':
    app.run_server(debug=True)