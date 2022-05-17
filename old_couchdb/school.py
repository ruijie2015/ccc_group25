import pandas as pd
import geopandas
import shapely.geometry as geometry
import couchdb


geo_data = geopandas.read_file('~/Desktop/melbourne.geojson')
school_data_2014 = pd.read_csv("~/Desktop/Education/school_locations_2013.csv")
school_data_2015 = pd.read_csv("~/Desktop/Education/school_locations_2015.csv")
school_data_2016 = pd.read_csv("~/Desktop/Education/school_locations_2016.csv")
school_data_2017 = pd.read_csv("~/Desktop/Education/school_locations_2017.csv")


# connect to couchdb
user = "admin"
password = "admin"
couch = couchdb.Server("http://%s:%s@172.26.128.232:5984/" % (user, password))
db = couch.create('school_data')


for i in range(len(school_data_2014)):
    school_dict = {"school_type": school_data_2014["school_type"][i], "school_name": school_data_2014["school_name"][i],
                   "year": 2014}
    print(school_dict)
    db.save(school_dict)


for i in range(len(school_data_2015)):
    school_dict = {"school_type": school_data_2015["school_type"][i], "school_name": school_data_2015["school_name"][i],
                   "year": 2015}

    pnts = geometry.Point([school_data_2015["x"][i], school_data_2015["y"][i]])
    for j in range(len(geo_data)):
        if pnts.within(geo_data["geometry"][j]):
            school_dict["suburb"] = geo_data["name"][j]
            print(school_dict)
            db.save(school_dict)
            break


for i in range(len(school_data_2016)):
    school_dict = {"school_type": school_data_2016["school_type"][i], "school_name": school_data_2016["school_name"][i],
                   "year": 2016}

    pnts = geometry.Point([school_data_2016["longitude"][i], school_data_2016["latitude"][i]])
    for j in range(len(geo_data)):
        if pnts.within(geo_data["geometry"][j]):
            school_dict["suburb"] = geo_data["name"][j]
            print(school_dict)
            db.save(school_dict)
            break


for i in range(len(school_data_2017)):
    school_dict = {"school_type": school_data_2017["school_type"][i], "school_name": school_data_2017["school_name"][i],
                   "year": 2017}

    pnts = geometry.Point([school_data_2017["x"][i], school_data_2017["y"][i]])
    for j in range(len(geo_data)):
        if pnts.within(geo_data["geometry"][j]):
            school_dict["suburb"] = geo_data["name"][j]
            print(school_dict)
            db.save(school_dict)
            break

