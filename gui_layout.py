import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table as d
import mysql.connector

header = html.Div(children=[
            html.H1('MeerKAT S-band survey database')
         ], style={'padding':'10px 10px'})

def get_table_data():
    # Connect to the database and execute the query
    db = mysql.connector.connect(host="localhost", user="reader", password="w4h2XF8kIXP6K36wBcWABPMQ#")
    cursor = db.cursor(buffered=True)
    cursor.execute('SELECT * FROM meerkat.meerkat')
    
    # Get the no. of rows and names of columns
    col_names = cursor.column_names
    n_rows = cursor.rowcount
    
    # Create a dict of column names needed by dash table
    columns = [{"name": "Pointing", "id": "name"},
               {"name": "Observational date", "id": "obs_date"},
               {"name": "Status", "id": "status"}]
    
    # Iterate through different rows and form a list of dictionaries
    tab_data = []
    for n in range(n_rows):
        this_row = cursor.fetchone()
        temp_dict = {
                        "name":this_row[0],
                        "obs_date":this_row[1],
                        "status":this_row[2]
                    }
        tab_data.append( temp_dict )

    # Close the database connection
    cursor.close()
    db.close()
    return columns, tab_data
    
cols, dat = get_table_data()
data_table = d.DataTable(
                id="table",
                columns=cols,
                data = dat
             )

layout = html.Div([
            dbc.Row(dbc.Col(header)),
            dbc.Row(dbc.Col(data_table, width=6), justify="center")
         ])
