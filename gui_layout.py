import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table as d
import backend

header = html.Div(children=[
            html.H1('MeerKAT S-band survey: overview')
         ], style={'padding':'10px 10px'})

cols, dat, n_rows = backend.get_table_data()
data_table = d.DataTable(
                style_as_list_view=True,
                style_cell={
                    'textAlign':'left'
                },
                style_header={
                    'fontWeight':'bold'
                },
                id="table",
                columns=cols,
                data = dat,
                
                page_size=10 # No of rows to display at once
             )

layout = html.Div([
            dbc.Row(dbc.Col(header)),
            dbc.Row(dbc.Col(data_table, width=5), justify="center")
         ])
