import pandas as pd
import couchdb

enroll_data = pd.read_csv("~/Desktop/Education/enroll.csv")

# connect to couchdb
user = "admin"
password = "admin"
couch = couchdb.Server("http://%s:%s@172.26.128.232:5984/" % (user, password))
db = couch.create('enroll_data')

for i in range(len(enroll_data)):
    enroll_dict = {"year_2014": int(enroll_data["2014"][i]), "year_2015": int(enroll_data["2015"][i]),
                   "year_2016": int(enroll_data["2016"][i]), "year_2017": int(enroll_data["2017"][i])}
    print(enroll_dict)
    db.save(enroll_dict)

