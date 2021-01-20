'''
Creates a map showing the total shootings for each state
'''

import pandas as pd 
import plotly.graph_objects as go

# Read in the created csv
shootings_per_state = pd.read_csv("Data/Shootings_per_state.csv")

# Add the text to be displayed when hovering over each state
shootings_per_state['text'] = shootings_per_state['State'] + '<br>' + \
    'Number of shootings: ' + str(shootings_per_state['Number of shootings'])

# Create the choropleth map
fig = go.Figure(data=go.Choropleth(locations=shootings_per_state['State'],
                z=shootings_per_state['Number of shootings'].astype(float),
                locationmode='USA-states',
                colorscale='Reds',
                # text=shootings_per_state['text'],
                marker_line_color='white',
                colorbar_title='Number of shootings'))

fig.update_layout(title_text = 'Number of school shootings per state', 
                geo = dict(scope='usa',
                projection = go.layout.geo.Projection(type='albers usa'),
                showlakes = True,
                lakecolor = 'rgb(255, 255, 255)'))

fig.show()

