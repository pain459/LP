import dash
from dash import dcc, html, Input, Output, dash_table
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the dataset
data = {
    "client": ["client1", "client2", "client3", "client4", "client5", "client6", "client7", "client8", "client9", "client10", "client11", "client12"],
    "triggered_count": [2, 22, 4, 13, 5, 1, 18, 6, 1, 2, 65, 32],
    "total_retriggers": [0, 6, 0, 9, 2, 43, 4, 3, 1, 0, 157, 36],
    "total_notifications": [2, 28, 4, 22, 7, 44, 22, 9, 2, 2, 222, 68],
    "point1": [0, 10, 4, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    "point2": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "point3": [1, 18, 0, 19, 6, 0, 21, 9, 0, 2, 163, 63],
}
df = pd.DataFrame(data)

# Initialize Dash App
app = dash.Dash(__name__)
app.title = "Client Activity Analysis Dashboard"

# App Layout
app.layout = html.Div([
    html.H1("Client Activity Analysis Dashboard", style={'textAlign': 'center'}),
    
    # Dropdowns for selecting rows, values, and aggregation function
    html.Div([
        html.Div([
            html.Label("Select Rows:"),
            dcc.Dropdown(
                id='row-dropdown',
                options=[{'label': col, 'value': col} for col in df.columns],
                value='client',
                multi=True,
                placeholder="Select column(s) for Rows"
            ),
        ], style={'width': '30%', 'display': 'inline-block', 'padding': '10px'}),

        html.Div([
            html.Label("Select Values:"),
            dcc.Dropdown(
                id='value-dropdown',
                options=[{'label': col, 'value': col} for col in df.columns if col != 'client'],
                multi=True,
                placeholder="Select column(s) for Values"
            ),
        ], style={'width': '30%', 'display': 'inline-block', 'padding': '10px'}),

        html.Div([
            html.Label("Aggregation Function:"),
            dcc.Dropdown(
                id='agg-func-dropdown',
                options=[
                    {'label': 'Sum', 'value': 'sum'},
                    {'label': 'Mean', 'value': 'mean'},
                    {'label': 'Count', 'value': 'count'},
                    {'label': 'Max', 'value': 'max'},
                    {'label': 'Min', 'value': 'min'}
                ],
                value='sum',
                placeholder="Select aggregation function"
            ),
        ], style={'width': '30%', 'display': 'inline-block', 'padding': '10px'}),
    ]),

    # Data Table
    html.Div(id='pivot-table', style={'marginTop': '30px'}),

    # Visualization Dropdown and Graph
    html.Div([
        html.Label("Select Visualization Type:"),
        dcc.Dropdown(
            id='viz-dropdown',
            options=[
                {'label': 'Bar Chart', 'value': 'bar'},
                {'label': 'Line Chart', 'value': 'line'},
                {'label': 'Heatmap', 'value': 'heatmap'}
            ],
            value='bar',
            placeholder="Select a visualization type"
        ),
        dcc.Graph(id='graph-output'),
    ], style={'marginTop': '40px'})
])

# Callback to Update Pivot Table and Graph
@app.callback(
    [Output('pivot-table', 'children'),
     Output('graph-output', 'figure')],
    [Input('row-dropdown', 'value'),
     Input('value-dropdown', 'value'),
     Input('agg-func-dropdown', 'value'),
     Input('viz-dropdown', 'value')]
)
def update_dashboard(rows, values, agg_func, viz_type):
    if not rows or not values:
        return "Select rows and values to display the pivot table.", go.Figure()

    # Create Pivot Table
    pivot_table = pd.pivot_table(
        df,
        values=values,
        index=rows,
        aggfunc=agg_func,
        fill_value=0
    )

    # Convert Pivot Table to HTML Table for Display
    pivot_table_html = dash_table.DataTable(
        columns=[{"name": str(col), "id": str(col)} for col in pivot_table.reset_index().columns],
        data=pivot_table.reset_index().to_dict('records'),
        style_table={'overflowX': 'auto'},
        page_size=10,
        style_data={'whiteSpace': 'normal', 'height': 'auto'},
        style_cell={'textAlign': 'left'}
    )

    # Create Visualization
    fig = {}
    if viz_type == 'bar':
        fig = px.bar(pivot_table, barmode='group', title=f"{agg_func.capitalize()} of Selected Values")
    elif viz_type == 'line':
        fig = px.line(pivot_table, title=f"{agg_func.capitalize()} of Selected Values")
    elif viz_type == 'heatmap':
        fig = px.imshow(
            pivot_table.values, 
            x=pivot_table.columns, 
            y=pivot_table.index,
            title=f"{agg_func.capitalize()} of Selected Values",
            labels={'color': 'Value'}
        )

    return pivot_table_html, fig


# Run the App
if __name__ == '__main__':
    app.run_server(debug=True)
