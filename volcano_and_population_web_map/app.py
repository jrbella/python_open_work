import folium
import pandas
import os

# Create Map Object
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

# importing variables to work on Windows
here = os.path.dirname(os.path.abspath(__file__))
# Volcanoe Data as CSV
volcanoes = "%s/volcanoes.csv" % (here)
# Poulation Data as JSON
world = "%s/world.json" % (here)

volcano_data = pandas.read_csv(volcanoes)
lat = list(volcano_data["LAT"])
lon = list(volcano_data["LON"])
elev = list(volcano_data["ELEV"])
name = list(volcano_data["NAME"])

# short function to determine color for elevation
def marker_color(elevation):
    if elevation < 1500:
        return "green"
    elif 1500 <= elevation < 3000:
        return "orange"
    else:
        return "red"


# for terminal view and data validation
print(volcano_data)

# Volcanoe feature group
fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el, nm in zip(lat, lon, elev, name):
    # format marker here
    coordinate_string = "%s, elevation:%s, lat:%s, long:%s" % (
        str(nm),
        str(el),
        str(lt),
        str(ln),
    )

    # formating for readability
    fgv.add_child(
        folium.Marker(
            location=[lt, ln],
            popup=coordinate_string,
            icon=folium.Icon(color=marker_color(el))
        )
    )

# population feature group
fgp = folium.FeatureGroup(name="Population")
# adding the polygons to seperate out countries/boundries
fgp.add_child(
    folium.GeoJson(
        data=open("world.json", "r", encoding="utf-8-sig").read(),
        style_function=lambda x: {
            "fillColor": "green"
            if x["properties"]["POP2005"] < 10000000
            else "orange"
            if 10000000 <= x["properties"]["POP2005"] < 20000000
            else "red"
        },
    )
)

# child groups added to Map Object
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

# Map Creation
map.save("Map1.html")
