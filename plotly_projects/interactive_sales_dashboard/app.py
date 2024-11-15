import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Load the dataset
df = pd.read_csv('sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])  # Ensure Date column is in datetime format

# Initialize the app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.title = "Interactive Sales Dashboard"

# Layout with Advanced Styling
app.layout = dbc.Container([
    # Header Section
    dbc.Row([
        dbc.Col(html.Div([
            html.H1("Interactive Sales Dashboard", className='text-center text-primary mb-4'),
            html.H5("Analyze and visualize sales data dynamically", className='text-center text-secondary mb-4')
        ]), width=12)
    ]),

    # Filter Section
    dbc.Row([
        dbc.Col(dcc.DatePickerRange(
            id='date-picker',
            min_date_allowed=df['Date'].min(),
            max_date_allowed=df['Date'].max(),
            start_date=df['Date'].min(),
            end_date=df['Date'].max(),
            style={'width': '100%'}
        ), width=4),

        dbc.Col(dcc.Dropdown(
            id='category-dropdown',
            options=[{'label': cat, 'value': cat} for cat in df['Product Category'].unique()],
            multi=True,
            placeholder="Select Product Category",
        ), width=4),

        dbc.Col(dcc.Dropdown(
            id='region-dropdown',
            options=[{'label': region, 'value': region} for region in df['Region'].unique()],
            multi=True,
            placeholder="Select Region",
        ), width=4),
    ], className="mb-4"),

    # KPI Section
    dbc.Row([
        dbc.Col(html.Div(id="kpi-section"), width=12)
    ], className="mb-4"),

    # Tabs for Visualizations
    dbc.Row([
        dbc.Col(dcc.Tabs(id="tabs", value="tab-1", children=[
            dcc.Tab(label="Overview", value="tab-1"),
            dcc.Tab(label="Details", value="tab-2")
        ]), width=12)
    ], className="mb-4"),

    html.Div(id="tabs-content"),

    # Footer Section
    dbc.Row([
        dbc.Col(html.Div([
            html.P("Developed by Your Name", className="text-center text-secondary"),
        ]), width=12)
    ], className="mt-4")
], fluid=True)

# Callback for KPIs
@app.callback(
    Output("kpi-section", "children"),
    [Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date'),
     Input('category-dropdown', 'value'),
     Input('region-dropdown', 'value')]
)
def update_kpis(start_date, end_date, selected_categories, selected_regions):
    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    if selected_categories:
        filtered_df = filtered_df[filtered_df['Product Category'].isin(selected_categories)]
    if selected_regions:
        filtered_df = filtered_df[filtered_df['Region'].isin(selected_regions)]

    total_sales = filtered_df['Sales Amount'].sum()
    avg_sales = filtered_df['Sales Amount'].mean()
    total_units = filtered_df['Units Sold'].sum()

    return dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Total Sales", className="card-title"),
                html.P(f"${total_sales:,.2f}", className="card-text")
            ])
        ], color="primary", inverse=True), width=4),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Average Sales", className="card-title"),
                html.P(f"${avg_sales:,.2f}", className="card-text")
            ])
        ], color="success", inverse=True), width=4),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Total Units Sold", className="card-title"),
                html.P(f"{total_units:,}", className="card-text")
            ])
        ], color="info", inverse=True), width=4)
    ])

# Callback for Tabs Content
@app.callback(
    Output("tabs-content", "children"),
    [Input("tabs", "value"),
     Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date'),
     Input('category-dropdown', 'value'),
     Input('region-dropdown', 'value')]
)
def render_tab_content(tab, start_date, end_date, selected_categories, selected_regions):
    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    if selected_categories:
        filtered_df = filtered_df[filtered_df['Product Category'].isin(selected_categories)]
    if selected_regions:
        filtered_df = filtered_df[filtered_df['Region'].isin(selected_regions)]

    if tab == "tab-1":
        fig1 = px.line(
            filtered_df, x='Date', y='Sales Amount',
            title="Sales Trend Over Time",
            template="plotly_dark"
        )
        fig2 = px.bar(
            filtered_df, x='Product Category', y='Sales Amount',
            title="Sales by Product Category",
            template="plotly_dark",
            color='Product Category'
        )
        return html.Div([
            dcc.Graph(figure=fig1),
            dcc.Graph(figure=fig2)
        ])

    elif tab == "tab-2":
        fig1 = px.scatter_geo(
            filtered_df, locations="Region", locationmode="USA-states",
            color="Sales Amount", hover_name="Product Category",
            title="Sales by Region",
            template="plotly_dark"
        )
        fig2 = px.pie(
            filtered_df, names='Product Category', values='Sales Amount',
            title="Customer Segmentation by Product Category",
            template="plotly_dark"
        )
        return html.Div([
            dcc.Graph(figure=fig1),
            dcc.Graph(figure=fig2)
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
