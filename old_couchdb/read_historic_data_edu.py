import json
import pandas as pd
import geopandas
import shapely.geometry as geometry
import couchdb
import time

geo_data = geopandas.read_file('melbourne.geojson')

education_keywords_csv = pd.read_csv('education_keywords.csv')
education_keywords = list(education_keywords_csv.iloc[:, 1])


#filter each twitter with keywords
def tweet_process(tweet):
    if (tweet['doc']['coordinates'] != None) and (tweet['doc']['lang'] == "en"):
        tweet_geo_coor = tweet['doc']['coordinates']['coordinates']
        tweet_id = tweet["id"]
        tweet_date_time = tweet['doc']['created_at']
        year = tweet_date_time.split()[-1]
        tweet_text = tweet['doc']['text']
        tweet_retweeted_counts = tweet['doc']["retweet_count"]
        tweet_liked_counts = tweet['doc']["favorite_count"]
        text = ""
        count = 0

        for word in education_keywords:
            if word in tweet_text:
                count = 1
                break

        if count == 1:
            text = tweet_text

        tweet_dict = {"year": year, "id": tweet_id, "text": text, "geo": tweet_geo_coor,
                      "retweeted_counts": tweet_retweeted_counts,
                      "tweet_favorite_counts": tweet_liked_counts, "suburb": "None"}

        for i in range(len(geo_data)):
            pnts = geometry.Point(tweet_dict['geo'])
            if pnts.within(geo_data.iloc[i]['geometry']):
                tweet_dict['suburb'] = geo_data['name'][i]
                break

        return tweet_dict


# connect to couchdb
user = "admin"
password = "admin"
couch = couchdb.Server("http://%s:%s@172.26.128.232:5984/" % (user, password))
db = couch.create('history_data_edu')



f1 = open('twitter-melb.json', 'r')
f1.readline()

while True:
    line = f1.readline()
    
    if len(line)<=3:
        break
    if line[-3] == ']':
        line = line[:-3] + ',\n'
    if line[-2] != ',':
        line = line[:-1] + ',\n'

    tweet = json.loads(line[:-2])
    single_data = tweet_process(tweet)
    
    #save to database
    if (single_data) and (single_data["suburb"]!="None") and (single_data["text"]!=""):
        single_data["timestamp"] = int(time.time()*1000000)
        #print(single_data)
        db.save(single_data)
        
f1.close()