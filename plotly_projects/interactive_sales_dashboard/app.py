# library imports

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Interactive Sales Dashboard"

# Load sample sales data
# Replace with actual data or a path to your CSV file
df = pd.read_csv('sales_data.csv')

# Ensure date is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Step 4: Create Dashboard Layout

app.layout = html.Div([
    html.H1("Sales Dashboard", style={'text-align': 'center'}),

    # Date range filter
    dcc.DatePickerRange(
        id='date-picker',
        min_date_allowed=df['Date'].min(),
        max_date_allowed=df['Date'].max(),
        start_date=df['Date'].min(),
        end_date=df['Date'].max()
    ),

    # Dropdowns for category and region filters
    html.Div([
        html.Label("Product Category"),
        dcc.Dropdown(
            id='category-dropdown',
            options=[{'label': cat, 'value': cat} for cat in df['Product Category'].unique()],
            multi=True
        )
    ], style={'width': '30%', 'display': 'inline-block'}),

    html.Div([
        html.Label("Region"),
        dcc.Dropdown(
            id='region-dropdown',
            options=[{'label': region, 'value': region} for region in df['Region'].unique()],
            multi=True
        )
    ], style={'width': '30%', 'display': 'inline-block'}),

    # KPIs and charts placeholders
    html.Div(id="kpi-section", style={'display': 'flex', 'justify-content': 'space-around'}),

    dcc.Graph(id='sales-trend-chart'),
    dcc.Graph(id='category-breakdown-chart'),
    dcc.Graph(id='region-sales-map'),
    dcc.Graph(id='customer-segmentation-pie')
])

# Step 5: Add Callback Functions for Interactivity

@app.callback(
    Output('sales-trend-chart', 'figure'),
    [Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date'),
     Input('category-dropdown', 'value'),
     Input('region-dropdown', 'value')]
)
def update_sales_trend(start_date, end_date, selected_categories, selected_regions):
    # Filter data based on user inputs
    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    if selected_categories:
        filtered_df = filtered_df[filtered_df['Product Category'].isin(selected_categories)]
    if selected_regions:
        filtered_df = filtered_df[filtered_df['Region'].isin(selected_regions)]

    # Create a line chart
    fig = px.line(filtered_df, x='Date', y='Sales Amount', title="Sales Trend Over Time")
    return fig

# Step 6: Run the App

if __name__ == '__main__':
    app.run_server(debug=True)