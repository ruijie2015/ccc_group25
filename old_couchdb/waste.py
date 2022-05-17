import pandas as pd
import couchdb


waste_data = pd.read_csv("~/Desktop/Environment/Waste_collected.csv")

# connect to couchdb
user = "admin"
password = "admin"
couch = couchdb.Server("http://%s:%s@172.26.128.232:5984/" % (user, password))
db = couch['waste_data']
# db = couch.create('waste_data')


for i in range(len(waste_data)):
    waste_dict = {"residential": int(waste_data["residential"][i]),
                  "public_litter_bins": int(waste_data["public_litter_bins"][i]), "year": int(waste_data["year"][i])}
    print(waste_dict)
    db.save(waste_dict)

