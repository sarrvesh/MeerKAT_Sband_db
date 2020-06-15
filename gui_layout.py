import dash_html_components as html
import dash_bootstrap_components as dbc

header = html.Div(children=[
            html.H1('MeerKAT S-band survey database')
         ], style={'padding':'10px 10px'})

layout = html.Div([
            dbc.Row(dbc.Col(header)),
         ])
