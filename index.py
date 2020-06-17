import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_html_components as html
import overview_layout
import invalid_layout
import modify_layout
import front_layout

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUMEN])
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
app.title = 'MeerKAT S-band survey'

app.layout = html.Div([
    # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),
    # content will be rendered in this element
    html.Div(id='page-content')
])


@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    """Function to parse the URL and provide the correct content to display."""
    if pathname == '/':
        layout = front_layout.layout
    elif pathname == '/overview/':
        layout = overview_layout.layout
    elif pathname == '/modify/':
        layout = modify_layout.layout
    else:
        layout = invalid_layout.layout

    return layout

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8053)
    #app.run_server(debug=False, host='0.0.0.0', port=8051, \
    #              dev_tools_ui=False, dev_tools_props_check=False)
