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

# Calculate KPIs
df['retrigger_ratio'] = df['total_retriggers'] / df['triggered_count']
df['notification_efficiency'] = df['total_notifications'] / df['triggered_count']
df['total_points'] = df[['point1', 'point2', 'point3']].sum(axis=1)
df['point1_contribution'] = (df['point1'] / df['total_points']) * 100
df['point2_contribution'] = (df['point2'] / df['total_points']) * 100
df['point3_contribution'] = (df['point3'] / df['total_points']) * 100

# Initialize Dash App
app = dash.Dash(__name__)
app.title = "Client KPI Dashboard"

# App Layout
app.layout = html.Div([
    html.H1("Client KPI Dashboard", style={'textAlign': 'center'}),
    
    # Dropdowns for selecting metrics
    html.Div([
        html.Label("Select KPI:"),
        dcc.Dropdown(
            id='kpi-dropdown',
            options=[
                {'label': 'Triggered Count', 'value': 'triggered_count'},
                {'label': 'Total Retriggers', 'value': 'total_retriggers'},
                {'label': 'Total Notifications', 'value': 'total_notifications'},
                {'label': 'Retrigger Ratio', 'value': 'retrigger_ratio'},
                {'label': 'Notification Efficiency', 'value': 'notification_efficiency'},
                {'label': 'Point 1 Contribution (%)', 'value': 'point1_contribution'},
                {'label': 'Point 2 Contribution (%)', 'value': 'point2_contribution'},
                {'label': 'Point 3 Contribution (%)', 'value': 'point3_contribution'},
            ],
            multi=True,
            value=['triggered_count', 'retrigger_ratio'],
            placeholder="Select KPIs to visualize"
        ),
        html.Label("Visualization Type:"),
        dcc.Dropdown(
            id='viz-type-dropdown',
            options=[
                {'label': 'Bar Chart', 'value': 'bar'},
                {'label': 'Line Chart', 'value': 'line'}
            ],
            value='bar',
            placeholder="Select visualization type"
        ),
    ], style={'display': 'grid', 'grid-template-columns': '50% 50%', 'gap': '20px', 'marginTop': '20px'}),

    # Graph Output
    dcc.Graph(id='kpi-graph-output'),

    # Data Table for KPI Summary
    html.Div(id='kpi-summary', style={'marginTop': '40px'}),
])

# Callback to Update Graph and KPI Summary
@app.callback(
    [Output('kpi-graph-output', 'figure'),
     Output('kpi-summary', 'children')],
    [Input('kpi-dropdown', 'value'),
     Input('viz-type-dropdown', 'value')]
)
def update_dashboard(selected_kpis, viz_type):
    if not selected_kpis:
        return go.Figure(), "Select at least one KPI to visualize."

    # Create Visualization
    if viz_type == 'bar':
        fig = px.bar(
            df,
            x='client',
            y=selected_kpis,
            title="KPI Analysis",
            barmode='group'
        )
    elif viz_type == 'line':
        fig = px.line(
            df,
            x='client',
            y=selected_kpis,
            title="KPI Analysis"
        )

    # Create KPI Summary Table
    summary_table = dash_table.DataTable(
        columns=[{"name": col, "id": col} for col in ['client'] + selected_kpis],
        data=df[['client'] + selected_kpis].to_dict('records'),
        style_table={'overflowX': 'auto'},
        page_size=10,
        style_data={'whiteSpace': 'normal', 'height': 'auto'},
        style_cell={'textAlign': 'left'}
    )

    return fig, summary_table


# Run the App
if __name__ == '__main__':
    app.run_server(debug=True)
