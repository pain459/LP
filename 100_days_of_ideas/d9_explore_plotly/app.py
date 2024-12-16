import dash
from dash import dcc, html, Input, Output, dash_table
import pandas as pd
import plotly.express as px

# Load the CSV file
# Replace 'your_file.csv' with your actual CSV file path
df = pd.read_csv('metrics.csv')

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Interactive Pivot Table Dashboard"

# Get the column names for dropdown options
column_options = [{'label': col, 'value': col} for col in df.columns]

# App Layout
app.layout = html.Div([
    html.H1("Interactive Pivot Table and Visualization", style={'textAlign': 'center'}),
    
    # Dropdowns for pivot table settings
    html.Div([
        html.Label("Rows:"),
        dcc.Dropdown(
            id='row-dropdown',
            options=column_options,
            multi=True,
            placeholder="Select column(s) for Rows"
        ),
        html.Label("Columns:"),
        dcc.Dropdown(
            id='col-dropdown',
            options=column_options,
            multi=True,
            placeholder="Select a column for Columns"
        ),
        html.Label("Values:"),
        dcc.Dropdown(
            id='value-dropdown',
            options=column_options,
            multi=True,
            placeholder="Select a column for Values"
        ),
        html.Label("Aggregation Function:"),
        dcc.Dropdown(
            id='agg-func-dropdown',
            options=[
                {'label': 'Sum', 'value': 'sum'},
                {'label': 'Average', 'value': 'mean'},
                {'label': 'Count', 'value': 'count'},
                {'label': 'Max', 'value': 'max'},
                {'label': 'Min', 'value': 'min'}
            ],
            value='sum',
            placeholder="Select aggregation function"
        ),
    ], style={'display': 'grid', 'grid-template-columns': 'repeat(2, 1fr)', 'gap': '20px'}),

    # Table to display pivoted data
    html.Div(id='pivot-table', style={'marginTop': '20px'}),
    
    # Visualization dropdown and graph
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

# Callbacks to update pivot table and visualizations
@app.callback(
    [Output('pivot-table', 'children'),
     Output('graph-output', 'figure')],
    [Input('row-dropdown', 'value'),
     Input('col-dropdown', 'value'),
     Input('value-dropdown', 'value'),
     Input('agg-func-dropdown', 'value'),
     Input('viz-dropdown', 'value')]
)
def update_dashboard(rows, cols, values, agg_func, viz_type):
    if not values:
        return "Select values to display the pivot table.", {}

    # Create pivot table
    pivot_table = pd.pivot_table(
        df,
        values=values,
        index=rows,
        columns=cols,
        aggfunc=agg_func,
        fill_value=0
    )

    # Convert pivot table to HTML table for display
    pivot_table_html = dash_table.DataTable(
        columns=[{"name": str(col), "id": str(col)} for col in pivot_table.reset_index().columns],
        data=pivot_table.reset_index().to_dict('records'),
        style_table={'overflowX': 'auto'},
        page_size=10,
        style_data={'whiteSpace': 'normal', 'height': 'auto'},
        style_cell={'textAlign': 'left'}
    )

    # Create visualizations
    fig = {}
    if viz_type == 'bar':
        fig = px.bar(pivot_table, barmode='group', title=f"{agg_func.capitalize()} of {values}")
    elif viz_type == 'line':
        fig = px.line(pivot_table, title=f"{agg_func.capitalize()} of {values}")
    elif viz_type == 'heatmap':
        fig = px.imshow(pivot_table.values, x=pivot_table.columns, y=pivot_table.index,
                        title=f"{agg_func.capitalize()} of {values}", labels={'color': values})

    return pivot_table_html, fig


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
