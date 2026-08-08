import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

DATA_URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv'
spacex_df = pd.read_csv(DATA_URL)

max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()
launch_sites = sorted(spacex_df['Launch Site'].unique())

app = dash.Dash(__name__)
app.title = 'SpaceX Launch Records Dashboard'

app.layout = html.Div([
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign':'center', 'color':'#111827'}),

    html.Div([
        html.Label('Launch site'),
        dcc.Dropdown(
            id='site-dropdown',
            options=[{'label':'All Sites','value':'ALL'}] +
                    [{'label':s,'value':s} for s in launch_sites],
            value='ALL',
            clearable=False
        )
    ], style={'maxWidth':'700px','margin':'0 auto'}),

    html.Br(),
    dcc.Graph(id='success-pie-chart'),

    html.Div([
        html.Label('Payload range (kg)'),
        dcc.RangeSlider(
            id='payload-slider',
            min=0, max=10000, step=1000,
            marks={i:f'{i}' for i in range(0,10001,2500)},
            value=[min_payload, min(10000, max_payload)]
        )
    ], style={'maxWidth':'900px','margin':'0 auto'}),

    dcc.Graph(id='success-payload-scatter-chart')
])

@app.callback(
    [Output('success-pie-chart','figure'),
     Output('success-payload-scatter-chart','figure')],
    [Input('site-dropdown','value'),
     Input('payload-slider','value')]
)
def update_dashboard(site, payload_range):
    if site == 'ALL':
        filtered_site = spacex_df.copy()
        pie_data = (filtered_site.groupby('Launch Site')['class']
                    .mean().reset_index(name='Success Ratio'))
        pie = px.bar(
            pie_data, x='Launch Site', y='Success Ratio',
            title='Landing success ratio by launch site',
            range_y=[0,1]
        )
    else:
        filtered_site = spacex_df[spacex_df['Launch Site'] == site]
        counts = filtered_site['class'].value_counts().rename(index={0:'Failure',1:'Success'})
        pie = px.pie(
            values=counts.values, names=counts.index,
            title=f'Landing outcomes for {site}'
        )

    low, high = payload_range
    filtered = filtered_site[
        (filtered_site['Payload Mass (kg)'] >= low) &
        (filtered_site['Payload Mass (kg)'] <= high)
    ]
    scatter = px.scatter(
        filtered,
        x='Payload Mass (kg)', y='class',
        color='Booster Version Category',
        hover_data=['Launch Site'],
        title=f'Payload vs landing outcome: {site if site != "ALL" else "all sites"}'
    )
    scatter.update_yaxes(tickvals=[0,1], ticktext=['No success','Success'])
    return pie, scatter

if __name__ == '__main__':
    app.run(debug=True)
