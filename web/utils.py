import couchdb


# connect to couchdb
user = "admin"
password = "admin"
couch = couchdb.Server("http://%s:%s@172.26.128.232:5984/" % (user, password))


def get_t1_data():
    tweet_dict = {"tweet_edu":0, "tweet_envir":0}

    db = couch["local_data_place_edu"]
    for item in db.view("view/year", group=True):
        tweet_dict["tweet_edu"] += item.value

    db = couch["local_data_place_environment"]
    for item in db.view("view/year", group=True):
        tweet_dict["tweet_envir"] += item.value

    return tweet_dict

def get_c1_data():

    db = couch["history_data_edu"]

    edu_dict = {}
    for item in db.view("view/suburb", group=True):
        edu_dict[item.key] = item.value

    suburb_list = list(edu_dict.keys())
    tweet_num_list = list(edu_dict.values())

    edu_dict = {"suburb": suburb_list, "tweet_num": tweet_num_list}

    return edu_dict

def get_c2_data():

    db = couch["history_data_environment"]

    envir_dict = {}
    for item in db.view("view/suburb", group=True):
        envir_dict[item.key] = item.value

    suburb_list = list(envir_dict.keys())
    tweet_num_list = list(envir_dict.values())

    envir_dict = {"suburb": suburb_list, "tweet_num": tweet_num_list}
    return envir_dict

def get_l1_data():

    # get top 10 suburb and tweet num from database 'history_data_edu'
    db = couch["history_data_edu"]

    edu_dict = {}
    for item in db.view("view/suburb", group=True):
        edu_dict[item.key] = item.value

    edu_dict = dict(sorted(edu_dict.items(), key=lambda x: x[1], reverse=True))

    suburb_list = list(edu_dict.keys())[0:10]
    tweet_num_list = list(edu_dict.values())[0:10]

    # get school number from database "school_data"
    db = couch["school_data"]
    school_num_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(10):
        for item in db.view("view/suburb", group=True):
            if item.key == suburb_list[i]:
                school_num_list[i] = item.value

    edu_dict = {"suburb": suburb_list, "tweet_num": tweet_num_list, "school_num": school_num_list}

    return edu_dict

def get_l2_data():

    # get year and tweet num for each year
    db = couch["history_data_edu"]

    year_list = [2014, 2015, 2016, 2017]
    tweet_num_list = []

    for item in db.view("view/year", group=True):
        tweet_num_list.append(item.value)

    # get school num for each year
    db = couch["school_data"]

    school_num_list = []

    for item in db.view("view/year", group=True):
        school_num_list.append(item.value)

    # get enroll num for each year
    db = couch["enroll_data"]

    enroll_num_list = []

    for item in db.view("view/year2014", group=True):
        enroll_num_list.append(int(item.value))

    for item in db.view("view/year2015", group=True):
        enroll_num_list.append(int(item.value))

    for item in db.view("view/year2016", group=True):
        enroll_num_list.append(int(item.value))

    for item in db.view("view/year2017", group=True):
        enroll_num_list.append(int(item.value))

    edu_dict = {"year": year_list, "tweet_num": tweet_num_list, "school_num": school_num_list,
                "enroll_num": enroll_num_list}

    return edu_dict

def get_l3_data():

    db = couch["local_data_place_edu"]

    edu_dict = {}

    for item in db.view("view/word", group=True):
        edu_dict[item.key[0]] = item.value

    edu_dict = dict(sorted(edu_dict.items(), key=lambda x: x[1], reverse=True))
    word_list = list(edu_dict.keys())[0:10]
    word_num_list = list(edu_dict.values())[0:10]
    percentage_list = [i / sum(word_num_list) for i in word_num_list]
    edu_dict = {"words": word_list, "word_num": word_num_list, "percentage": percentage_list}

    return edu_dict

def get_r1_data():

    db = couch["history_data_environment"]

    envir_dict = {}
    for item in db.view("view/suburb", group=True):
        envir_dict[item.key] = item.value

    envir_dict = dict(sorted(envir_dict.items(), key=lambda x: x[1], reverse=True))

    suburb_list = list(envir_dict.keys())[0:5]
    tweet_num_list = list(envir_dict.values())[0:5]

    envir_dict = {"suburb": suburb_list, "tweet_num": tweet_num_list}

    return envir_dict

def get_r2_data():

    # get year and tweet num for each year
    db = couch["history_data_environment"]

    year_list = [2014, 2015, 2016, 2017]
    tweet_num_list = []

    for item in db.view("view/year", group=True):
        tweet_num_list.append(item.value)

    # get bin num and residential num for each year
    db = couch["waste_data"]

    bin_list = []
    residential_list = []

    for item in db.view("view/year_litter_bins", group=True):
        bin_list.append(item.value)

    for item in db.view("view/year_residential", group=True):
        residential_list.append(item.value)

    envir_dict = {"year": year_list, "tweet_num": tweet_num_list, "bin": bin_list, "residential": residential_list}

    return envir_dict

def get_r3_data():

    # get environment data
    db = couch["local_data_place_environment"]

    envir_dict = {}

    for item in db.view("view/word", group=True):
        envir_dict[item.key[0]] = item.value

    envir_dict = dict(sorted(envir_dict.items(), key=lambda x: x[1], reverse=True))

    word_list = list(envir_dict.keys())[0:10]
    word_num_list = list(envir_dict.values())[0:10]
    percentage_list = [i / sum(word_num_list) for i in word_num_list]

    envir_dict = {"words": word_list, "word_num": word_num_list, "percentage": percentage_list}

    return envir_dict

def get_c_data():
    dic1 = get_c1_data()
    dic2 = get_c2_data()
    new_dic = {}
    new_dic['suburb'] = dic1['suburb']
    tweet_num = []
    tweet1 = dic1['tweet_num']
    tweet2 = dic2['tweet_num']
    for i in range(122):
        tweet_num.append(tweet1[1]+tweet2[i])
    new_dic['tweet_num'] = tweet_num
    return new_dic



