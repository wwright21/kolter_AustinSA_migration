import plotly.express as px
import geopandas as gpd
import plotly.graph_objects as go
import pandas as pd
from urllib.request import urlopen
import json

europe = pd.read_csv(
    'https://raw.githubusercontent.com/softhints/Pandas-Exercises-Projects/main/data/europe_pop.csv')

lats = europe['lat']
lons = europe['lon']
text = europe['values'].astype(str)

with urlopen('https://raw.githubusercontent.com/leakyMirror/map-of-europe/master/GeoJSON/europe.geojson') as response:
    counties = json.load(response)

fig = go.Figure()
fig.add_trace(go.Scattermapbox(lat=lats,
                               lon=lons,
                               mode='text+markers',
                               text=text,
                               textfont=dict(
                                   family="san serif",
                                   size=15),
                               textposition='top center',
                               marker_size=12,
                               marker_color='red'))

fig.add_trace(go.Choroplethmapbox(geojson=counties,
                                  locations=europe['name'],
                                  z=europe['pop_est'],
                                  colorscale="Reds",
                                  featureidkey="properties.NAME",
                                  marker_opacity=0.8,
                                  marker_line_width=0))

fig.update_layout(title_text='Europe',
                  title_x=0.5,
                  width=1200,
                  height=1200,
                  mapbox=dict(center=dict(lat=52.370216, lon=4.895168),
                              accesstoken="pk.eyJ1Ijoid3dyaWdodDIxIiwiYSI6ImNsZTV3NWplcDBiam4zbnBoMDRqOGJhY2QifQ.Y8ZdfLVFyETj4qc8JNiaHw",
                              zoom=3,
                              style="light"
                              )
                  )
fig.show()
