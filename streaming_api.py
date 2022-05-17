import json
import tweepy
import geopandas
import shapely.geometry as geometry
import couchdb
import pandas as pd
import argparse


parser = argparse.ArgumentParser(description="Ip address of new instance")
parser.add_argument('ip', type=str)
args = parser.parse_args()
ip = args.ip

# you need to change the route to read this file
geo_data = geopandas.read_file('melbourne.geojson')

consumer_key = "PUk2VClousB5IPRSYgvlxKCjV"
consumer_secret = "6rcZRWhrftL0R2zAdC2JKl3X69PLEtYClzgcL2R1aZOW8Yp3ms"
access_token = "1511598829862551554-5mj3IoOX7ddU95BWbC526Iux6JF06D"
access_token_secret = "xFC7bWhWrabgXRq1kFBZPIv8HdCWq5zz4abpceo3VAXLR"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def conn_new():
    # connect to new couchdb
    user = "admin"
    password = "admin"
    couch = couchdb.Server("http://%s:%s@%s:5984/" % (user, password, ip))
    return couch


def conn_old():
    # connect to old couchdb
    user = "admin"
    password = "admin"
    couch = couchdb.Server("http://%s:%s@172.26.128.232:5984/" % (user, password))
    return couch


# use existing database
couch1 = conn_new()
couch2 = conn_old()
db1 = couch2["history_data_edu"]
db2 = couch2["local_data_place_edu"]
db3 = couch2["history_data_environment"]
db4 = couch2["local_data_place_environment"]
db5 = couch1.create("streaming_data")


# do mapreduce
map_Tweet_num = '''function (doc) {
        emit(doc.year, 1);
    }
'''

reduce_Tweet_num = "_count"

streaming_tweet = {
        "_id": f"_design/view",
        "views": {
            "year": {
                "map": map_Tweet_num,
                "reduce": reduce_Tweet_num
            }

        },
        "language": "javascript",
        "options": {"partitioned": False}
}

db5.save(streaming_tweet)


# you need to change the route to run these two csv files
education_keywords_csv = pd.read_csv('~/Desktop/education_keywords.csv')
education_keywords = list(education_keywords_csv.iloc[:, 1])

environment_keywords_csv = pd.read_csv('~/Desktop/environment_keywords.csv')
environment_keywords = list(environment_keywords_csv.iloc[:, 1])


class MyStreamListener(tweepy.StreamListener):

    def on_data(self, raw_data):
        data = json.loads(raw_data)

        # tweets in Australia
        t_dict_no_filter = {"year": data['created_at'][-4:], "id": data["id"], "text": data['text'],
                            "place": data['place']['full_name']}
        print(t_dict_no_filter)

        db5.save(t_dict_no_filter)

        try:
            data_id = data["id"]
            data_coor = data['coordinates']["coordinates"]
            data_year = data['created_at'][-4:]
            data_text = data['text']
            count = 0

            for word in education_keywords:
                if word in data_text:
                    count = 1
                    break

            for word in environment_keywords:
                if word in data_text:
                    count = 2
                    break

            # education tweets with geo
            if count == 1:
                t_dict_geo = {"year": data_year, "id": data_id, "text": data_text, "geo": data_coor}

                pnts = geometry.Point(t_dict_geo["geo"])
                for i in range(len(geo_data)):
                    if pnts.within(geo_data.iloc[i]['geometry']):
                        t_dict_geo["suburb"] = geo_data['name'][i]
                        print(t_dict_geo)
                        db1.save(t_dict_geo)
                        break

            # environment tweets with geo
            if count == 2:
                t_dict_geo = {"year": data_year, "id": data_id, "text": data_text, "geo": data_coor}

                pnts = geometry.Point(t_dict_geo["geo"])
                for i in range(len(geo_data)):
                    if pnts.within(geo_data.iloc[i]['geometry']):
                        t_dict_geo["suburb"] = geo_data['name'][i]
                        print(t_dict_geo)
                        db3.save(t_dict_geo)
                        break

        except KeyError as e:
            print("None")

        except TypeError as t:
            # tweet with place, without geo
            data_id = data["id"]
            data_year = data['created_at'][-4:]
            data_text = data['text']
            data_place_name = data['place']['full_name']

            count = 0

            for word in education_keywords:
                if word in data_text:
                    count = 1
                    break

            for word in environment_keywords:
                if word in data_text:
                    count = 2
                    break

            # education tweets with place
            if count == 1:

                t_dict_no_geo = {"year": data_year, "id": data_id, "text": data_text, "place_name": data_place_name}

                if "Melbourne" in t_dict_no_geo["place_name"]:
                    print(t_dict_no_geo)

                    db2.save(t_dict_no_geo)

            # environment tweets with place
            if count == 2:

                t_dict_no_geo = {"year": data_year, "id": data_id, "text": data_text, "place_name": data_place_name}

                if "Melbourne" in t_dict_no_geo["place_name"]:
                    print(t_dict_no_geo)

                    db4.save(t_dict_no_geo)

    def on_error(self, status_code):
        if status_code == 420:
            return False  # returning False in on_error disconnects the stream


AU_bounding_box = [113.338953078, -43.6345972634, 153.569469029, -10.6681857235]

twitterStream = tweepy.Stream(api.auth, MyStreamListener())

twitterStream.filter(locations=AU_bounding_box, languages=['en'])






