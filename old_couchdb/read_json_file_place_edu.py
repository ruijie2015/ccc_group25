import json
import couchdb
import pandas as pd

#connect to CouchDB
user = "admin"
password = "admin"
couch = couchdb.Server("http://%s:%s@172.26.128.232:5984/" % (user, password))

db = couch.create('local_data_place_edu')

education_keywords_csv = pd.read_csv('education_keywords.csv')
education_keywords = list(education_keywords_csv.iloc[:, 1])

file = open("ass2_real_time_data_have_place.json", 'r')


#filter each tweet related to education
done = 0
while not done:
    tweet = file.readline()
    count=0
    if tweet != "":

        tweet_dict = json.loads(tweet)
        tweet_text=tweet_dict['text']

        
        for word in education_keywords:
            if word in tweet_text:
                count = 1
                break
        # save to Database
        if (count == 1) and ("Melbourne" in tweet_dict['place_name']):
            print(tweet_dict)
            db.save(tweet_dict)
    else:
        done = 1

file.close()