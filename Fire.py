import csv
from plotly import offline
from plotly.graph_objs import Scattergeo, Layout
#Gather the csv file global_fires.html
def create_fire_map(csv_filename, output_html='global_fires.html'):
    lats, lons, brightnesses, hover_texts = [], [], [], []
    
    with open(csv_filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Adjust field names if needed (e.g., 'latitude', 'longitude', 'brightness')
            lat = float(row.get('latitude') or row.get('lat') or row.get('Latitude'))
            lon = float(row.get('longitude') or row.get('lon') or row.get('Longitude'))
            brightness = float(row.get('brightness') or row.get('Bright_ti4') or row.get('brightness'))

            lats.append(lat)
            lons.append(lon)
            brightnesses.append(brightness)

            hover = f"Brightness: {brightness}"
            hover_texts.append(hover)
#map the fire_map
    data = [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': hover_texts,
        'marker': {
            'size': [b / 20 for b in brightnesses],
            'color': brightnesses,
            'colorscale': 'YlOrRd',
            'reversescale': True,
            'colorbar': {'title': 'Brightness'},
        },
    }]

    layout = Layout(title='Global Fire Activity (Past Day)')
    fig = {'data': data, 'layout': layout}
    offline.plot(fig, filename=output_html)
    print(f"Map saved to {output_html}")
