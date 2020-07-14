import pandas
from geopy.geocoders import ArcGIS
nom = ArcGIS()

df1 = pandas.read_json("json/supermarkets.json")


df1["Address"] = df1["Address"] + ", " + df1["City"] + ", " + df1["Country"]
df1["Coordinates"] = df1["Address"].apply(nom.geocode)
df1["Latitude"]=df1["Coordinates"].apply(lambda x: x.latitude)
df1["Longitude"]=df1["Coordinates"].apply(lambda x: x.longitude)
print(df1)
