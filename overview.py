import time
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import flask
from gui_layout import layout

# Initialize the dash app
server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUMEN], \
                server=server, url_base_pathname='/meerkatsdb/')
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

#######################################
# Setup the layout of the web interface
#######################################
app.layout = layout
app.title = 'MeerKAT S-band survey: overview'

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8053)
    #app.run_server(debug=False, host='0.0.0.0', port=8051, \
    #              dev_tools_ui=False, dev_tools_props_check=False)
