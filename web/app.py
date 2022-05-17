from flask import Flask, jsonify, url_for
from flask import render_template
import utils
import argparse
import couchdb


ip = ""
app = Flask(__name__)
couch = 0


@app.route('/')
def template():
    return render_template('index.html')


@app.route('/t1')
def get_t1_data():
    data = utils.get_t1_data()
    return data

@app.route('/t2')
def get_t2_data():
    db = couch["streaming_data"]
    total_num = 0
    for item in db.view("view/year", group=True):
        total_num = item.value
    stream = {}
    stream['num'] = total_num
    return stream


@app.route('/c1')
def get_c1_data():
    data = utils.get_c1_data()
    return data


@app.route('/c2')
def get_c2_data():
    data = utils.get_c2_data()
    return data


@app.route('/l1')
def get_l1_data():
    data = utils.get_l1_data()
    return data


@app.route('/l2')
def get_l2_data():
    data = utils.get_l2_data()
    return data


@app.route('/l3')
def get_l3_data():
    data = utils.get_l3_data()
    return data


@app.route('/r1')
def get_r1_data():
    data = utils.get_r1_data()
    return data


@app.route('/r2')
def get_r2_data():
    data = utils.get_r2_data()
    return data


@app.route('/r3')
def get_r3_data():
    data = utils.get_r3_data()
    return data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ip addresss of new instance')
    parser.add_argument('ip', type=str)
    args = parser.parse_args()
    ip = args.ip
    couch = couchdb.Server("http://%s:%s@%s:5984/" % ("admin", "admin", ip))
    app.run(host="0.0.0.0", port=5000, debug=True)