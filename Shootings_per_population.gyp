'''
This file is to display a map of the number of school shootings per state
weighted by the population of the state
'''
import pandas as pd
import plotly.graph_objects as go

# Read the shootings and populations csv files
shootings = pd.read_csv('Data/Shootings_per_state.csv', index_col='State')
shootings.sort_values('State', ascending=True, inplace=True)
state_populations = pd.read_csv('Data/StatePopulations.csv')
state_populations = state_populations[['Code', 'POPESTIMATE2019']]


# Combine the two dataframes
shootings_and_populations = state_populations.join(shootings, on='Code', how='inner')
shootings_and_populations['Shooting Density'] = shootings_and_populations[
    'Number of shootings'] / shootings_and_populations['POPESTIMATE2019'] * 100000

fig = go.Figure(data=go.Choropleth(locations=shootings_and_populations['Code'],
                z=shootings_and_populations['Shooting Density'].astype(float),
                locationmode='USA-states',
                colorscale='Reds',
                # text=shootings_per_state['text'],
                marker_line_color='white',
                colorbar_title='Number of shootings per 100,000 people'))

fig.update_layout(title_text = 'Number of school shootings per state adjusted for population', 
                geo = dict(scope='usa',
                projection = go.layout.geo.Projection(type='albers usa'),
                showlakes = True,
                lakecolor = 'rgb(255, 255, 255)'))

fig.show()