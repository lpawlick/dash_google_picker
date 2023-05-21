from dash import Dash, dcc, html, Input, Output, callback_context
import dash_google_picker
from dotenv import load_dotenv
import os

load_dotenv()
app = Dash(__name__)

app.layout = html.Div([
    html.Button('Open Google Picker', id='open-picker-button', n_clicks=0),
    dash_google_picker.GooglePicker(
        id='google-picker',
        value='my-value',
        label='my-label',
        open=False,
        client_id=os.getenv('GOOGLE_CLIENT_ID'),
        scope='https://www.googleapis.com/auth/drive.readonly',
        developer_key=os.getenv('GOOGLE_DEVELOPER_KEY')
        ),
    html.Div(id='display-selected-url'),
    html.Div(id='display-action')
])

@app.callback(
    Output('google-picker', 'open'),
    [Input('open-picker-button', 'n_clicks')],
)
def open_google_picker(n_clicks):
    if n_clicks > 0:
        return True
    return False

@app.callback(
    Output('display-selected-url', 'children'),
    [Input('google-picker', 'documents')]
)
def display_output(documents):
    # Now documents is a dictionary
    if documents:
        return f'Selected data: {documents}'

@app.callback(
    Output('display-action', 'children'),
    [Input('google-picker', 'action')]
)
def display_action(action):
    # action is a string
    return f'Action: {action}'

if __name__ == '__main__':
    app.run_server(debug=True)
