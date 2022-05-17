import couchdb


# history_data_edu
user = "admin"
password = "admin"
couch = couchdb.Server("http://%s:%s@172.26.128.232:5984/" % (user, password))

db = couch["history_data_edu"]

map_suburb_hist_edu = '''function (doc) {
    emit(doc.suburb, 1);
    }
'''

reduce_suburb_hist_edu = "_count"

map_word_hist_edu = '''function(doc) {
     if (doc.text.indexOf('student') >1) emit(["student"], 1);
     if (doc.text.indexOf('fee') >1) emit(["fee"], 1);
     if (doc.text.indexOf('tuition') >1) emit(["tuition"], 1);
     if (doc.text.indexOf('teacher') >1) emit(["teacher"], 1);
     if (doc.text.indexOf('mentor') >1) emit(["mentor"], 1);
     if (doc.text.indexOf('professor') >1) emit(["professor"], 1);
     if (doc.text.indexOf('project') >1) emit(["project"], 1);
     if (doc.text.indexOf('assignment') >1) emit(["assignment"], 1);
     if (doc.text.indexOf('exam') >1) emit(["exam"], 1);
     if (doc.text.indexOf('academic') >1) emit(["academic"], 1);
     if (doc.text.indexOf('accessibility') >1) emit(["accessibility"], 1);
     if (doc.text.indexOf('achievement') >1) emit(["achievement"], 1);
     if (doc.text.indexOf('activities') >1) emit(["activities"], 1);
     if (doc.text.indexOf('andragogy') >1) emit(["andragogy"], 1);
     if (doc.text.indexOf('attention') >1) emit(["attention"], 1);
     if (doc.text.indexOf('attitude') >1) emit(["attitude"], 1);     
     if (doc.text.indexOf('challenge') >1) emit(["challenge"], 1);
     if (doc.text.indexOf('case') >1) emit(["case"], 1);
     if (doc.text.indexOf('class') >1) emit(["class"], 1);
     if (doc.text.indexOf('college') >1) emit(["college"], 1);
     if (doc.text.indexOf('collaborative') >1) emit(["collaborative"], 1);
     if (doc.text.indexOf('college') >1) emit(["college"], 1);
     if (doc.text.indexOf('communication') >1) emit(["communication"], 1);
     if (doc.text.indexOf('learn') >1) emit(["learn"], 1);
     if (doc.text.indexOf('teach') >1) emit(["teach"], 1);
     if (doc.text.indexOf('confidentiality') >1) emit(["confidentiality"], 1);
     if (doc.text.indexOf('grade') >1) emit(["grade"], 1);
     if (doc.text.indexOf('grading') >1) emit(["grading"], 1);
     if (doc.text.indexOf('course') >1) emit(["course"], 1);
     if (doc.text.indexOf('curriculum') >1) emit(["curriculum"], 1);
     if (doc.text.indexOf('discussions') >1) emit(["discussions"], 1);
     if (doc.text.indexOf('exams') >1) emit(["exams"], 1);
     if (doc.text.indexOf('evaluation') >1) emit(["evaluation"], 1);
     if (doc.text.indexOf('explanation') >1) emit(["explanation"], 1);
     if (doc.text.indexOf('faculty') >1) emit(["faculty"], 1);
     if (doc.text.indexOf('feedback') >1) emit(["feedback"], 1);
     if (doc.text.indexOf('graduate') >1) emit(["graduate"], 1);
     if (doc.text.indexOf('goal') >1) emit(["goal"], 1);
     if (doc.text.indexOf('instructor') >1) emit(["instructor"], 1);
     if (doc.text.indexOf('internship') >1) emit(["internship"], 1);
     if (doc.text.indexOf('knowledge') >1) emit(["knowledge"], 1);
     if (doc.text.indexOf('objectives') >1) emit(["objectives"], 1);
     if (doc.text.indexOf('participation') >1) emit(["participation"], 1);
     if (doc.text.indexOf('peer') >1) emit(["peer"], 1);
     if (doc.text.indexOf('plagiarism') >1) emit(["plagiarism"], 1);
     if (doc.text.indexOf('doctor') >1) emit(["doctor"], 1);
     if (doc.text.indexOf('question') >1) emit(["question"], 1);
     if (doc.text.indexOf('quiz') >1) emit(["quiz"], 1);
     if (doc.text.indexOf('reading') >1) emit(["reading"], 1);
     if (doc.text.indexOf('report') >1) emit(["report"], 1);
     if (doc.text.indexOf('research') >1) emit(["research"], 1);
     if (doc.text.indexOf('rubric') >1) emit(["rubric"], 1);
     if (doc.text.indexOf('scholarship') >1) emit(["scholarship"], 1);
     if (doc.text.indexOf('science') >1) emit(["science"], 1);
     if (doc.text.indexOf('technology') >1) emit(["technology"], 1);
     if (doc.text.indexOf('engineering') >1) emit(["engineering"], 1);
     if (doc.text.indexOf('mathematics') >1) emit(["mathematics"], 1);
     if (doc.text.indexOf('study') >1) emit(["study"], 1);
     if (doc.text.indexOf('syllabus') >1) emit(["syllabus"], 1);
     if (doc.text.indexOf('textbook') >1) emit(["textbook"], 1);
     if (doc.text.indexOf('understand') >1) emit(["understand"], 1);
     if (doc.text.indexOf('writing') >1) emit(["writing"], 1);
     if (doc.text.indexOf('write') >1) emit(["write"], 1);
}
'''

reduce_word_hist_edu = "_count"


map_year_hist_edu = '''function (doc) {
    emit(doc.year, 1);
  }
'''

reduce_year_hist_edu = "_count"


history_edu_tweet = {
        "_id": f"_design/view",
        "views": {
            "suburb": {
                "map": map_suburb_hist_edu,
                "reduce": reduce_suburb_hist_edu
            },
            "word": {
                "map": map_word_hist_edu,
                "reduce": reduce_word_hist_edu
            },
            "year": {
                "map": map_year_hist_edu,
                "reduce": reduce_year_hist_edu
            }
        },
        "language": "javascript",
        "options": {"partitioned": False}
}

db.save(history_edu_tweet)


# history_data_environment

db = couch["history_data_environment"]

map_suburb_hist_envir = '''function (doc) {
    emit(doc.suburb, 1);
    }
'''

reduce_suburb_hist_envir = "_count"

map_word_hist_envir = '''function(doc) {
     if (doc.text.indexOf('atmosphere') >1) emit(["atmosphere"], 1);
     if (doc.text.indexOf('biodegradable') >1) emit(["biodegradable"], 1);
     if (doc.text.indexOf('biodiversity') >1) emit(["biodiversity"], 1);
     if (doc.text.indexOf('carbon') >1) emit(["carbon"], 1);
     if (doc.text.indexOf('dioxide') >1) emit(["dioxide"], 1);
     if (doc.text.indexOf('carcinogen') >1) emit(["carcinogen"], 1);
     if (doc.text.indexOf('climate') >1) emit(["climate"], 1);
     if (doc.text.indexOf('coal') >1) emit(["coal"], 1);
     if (doc.text.indexOf('compost') >1) emit(["compost"], 1);
     if (doc.text.indexOf('conservation') >1) emit(["conservation"], 1);
     if (doc.text.indexOf('contaminant') >1) emit(["contaminant"], 1);
     if (doc.text.indexOf('deforestation') >1) emit(["deforestation"], 1);
     if (doc.text.indexOf('deforest') >1) emit(["deforest"], 1);
     if (doc.text.indexOf('disposable') >1) emit(["disposable"], 1);
     if (doc.text.indexOf('diversity') >1) emit(["diversity"], 1);
     if (doc.text.indexOf('ecology') >1) emit(["ecology"], 1);
     if (doc.text.indexOf('ecosystem') >1) emit(["ecosystem"], 1);
     if (doc.text.indexOf('emission') >1) emit(["emission"], 1);
     if (doc.text.indexOf('endangered') >1) emit(["endangered"], 1);
     if (doc.text.indexOf('energy') >1) emit(["energy"], 1);
     if (doc.text.indexOf('environment') >1) emit(["environment"], 1);
     if (doc.text.indexOf('erosion') >1) emit(["erosion"], 1);
     if (doc.text.indexOf('extinct') >1) emit(["extinct"], 1);
     if (doc.text.indexOf('fossil') >1) emit(["fossil"], 1);
     if (doc.text.indexOf('fuel') >1) emit(["fuel"], 1);
     if (doc.text.indexOf('landfill') >1) emit(["landfill"], 1);
     if (doc.text.indexOf('recycle') >1) emit(["recycle"], 1);
     if (doc.text.indexOf('sewerage') >1) emit(["sewerage"], 1);
     if (doc.text.indexOf('air') >1) emit(["air"], 1);
     if (doc.text.indexOf('temp') >1) emit(["temp"], 1);
     if (doc.text.indexOf('waste') >1) emit(["waste"], 1);
     if (doc.text.indexOf('eco') >1) emit(["eco"], 1);
     if (doc.text.indexOf('environs') >1) emit(["environs"], 1);
     if (doc.text.indexOf('relict') >1) emit(["relict"], 1);
     if (doc.text.indexOf('hotbed') >1) emit(["hotbed"], 1);
     if (doc.text.indexOf('green') >1) emit(["green"], 1);
     if (doc.text.indexOf('habitat') >1) emit(["habitat"], 1);
     if (doc.text.indexOf('ambiance') >1) emit(["ambiance"], 1);
     if (doc.text.indexOf('aciduricr') >1) emit(["aciduric"], 1);
     if (doc.text.indexOf('site') >1) emit(["site"], 1);
     if (doc.text.indexOf('effect') >1) emit(["effect"], 1);
     if (doc.text.indexOf('community') >1) emit(["community"], 1);
     if (doc.text.indexOf('produce') >1) emit(["produce"], 1);
     if (doc.text.indexOf('consume') >1) emit(["consume"], 1);
     if (doc.text.indexOf('decompose') >1) emit(["decompose"], 1);
     if (doc.text.indexOf('adapt') >1) emit(["adapt"], 1);
     if (doc.text.indexOf('habitat') >1) emit(["habitat"], 1);
     if (doc.text.indexOf('weather') >1) emit(["weather"], 1);
     if (doc.text.indexOf('impact') >1) emit(["impact"], 1);
     if (doc.text.indexOf('global') >1) emit(["global"], 1);
     if (doc.text.indexOf('change') >1) emit(["change"], 1);
     if (doc.text.indexOf('precipitation') >1) emit(["precipitation"], 1);
     if (doc.text.indexOf('gas') >1) emit(["gas"], 1);
     if (doc.text.indexOf('ems') >1) emit(["ems"], 1);
     if (doc.text.indexOf('pollution') >1) emit(["pollution"], 1);
     if (doc.text.indexOf('green') >1) emit(["green"], 1);   
}
'''

reduce_word_hist_envir = "_count"

map_year_hist_envir = '''function (doc) {
    emit(doc.year, 1);
    }
'''

reduce_year_hist_envir = "_count"

history_envir_tweet = {
    "_id": f"_design/view",
    "views": {
        "suburb": {
            "map": map_suburb_hist_envir,
            "reduce": reduce_suburb_hist_envir
        },
        "word": {
            "map": map_word_hist_envir,
            "reduce": reduce_word_hist_envir
        },
        "year": {
            "map": map_year_hist_envir,
            "reduce": reduce_year_hist_envir
        }
    },
    "language": "javascript",
    "options": {"partitioned": False}
}

db.save(history_envir_tweet)


# local_data_place_edu

db = couch["local_data_place_edu"]

map_word_local_edu = '''function(doc) {
     if (doc.text.indexOf('student') >1) emit(["student"], 1);
     if (doc.text.indexOf('fee') >1) emit(["fee"], 1);
     if (doc.text.indexOf('tuition') >1) emit(["tuition"], 1);
     if (doc.text.indexOf('teacher') >1) emit(["teacher"], 1);
     if (doc.text.indexOf('mentor') >1) emit(["mentor"], 1);
     if (doc.text.indexOf('professor') >1) emit(["professor"], 1);
     if (doc.text.indexOf('project') >1) emit(["project"], 1);
     if (doc.text.indexOf('assignment') >1) emit(["assignment"], 1);
     if (doc.text.indexOf('exam') >1) emit(["exam"], 1);
     if (doc.text.indexOf('academic') >1) emit(["academic"], 1);
     if (doc.text.indexOf('accessibility') >1) emit(["accessibility"], 1);
     if (doc.text.indexOf('achievement') >1) emit(["achievement"], 1);
     if (doc.text.indexOf('activities') >1) emit(["activities"], 1);
     if (doc.text.indexOf('andragogy') >1) emit(["andragogy"], 1);
     if (doc.text.indexOf('attention') >1) emit(["attention"], 1);
     if (doc.text.indexOf('attitude') >1) emit(["attitude"], 1);    
     if (doc.text.indexOf('challenge') >1) emit(["challenge"], 1);
     if (doc.text.indexOf('case') >1) emit(["case"], 1);
     if (doc.text.indexOf('class') >1) emit(["class"], 1);
     if (doc.text.indexOf('college') >1) emit(["college"], 1);
     if (doc.text.indexOf('collaborative') >1) emit(["collaborative"], 1);
     if (doc.text.indexOf('college') >1) emit(["college"], 1);
     if (doc.text.indexOf('communication') >1) emit(["communication"], 1);
     if (doc.text.indexOf('learn') >1) emit(["learn"], 1);
     if (doc.text.indexOf('teach') >1) emit(["teach"], 1);
     if (doc.text.indexOf('confidentiality') >1) emit(["confidentiality"], 1);
     if (doc.text.indexOf('grade') >1) emit(["grade"], 1);
     if (doc.text.indexOf('grading') >1) emit(["grading"], 1);
     if (doc.text.indexOf('course') >1) emit(["course"], 1);
     if (doc.text.indexOf('curriculum') >1) emit(["curriculum"], 1);
     if (doc.text.indexOf('discussions') >1) emit(["discussions"], 1);
     if (doc.text.indexOf('exams') >1) emit(["exams"], 1);
     if (doc.text.indexOf('evaluation') >1) emit(["evaluation"], 1);
     if (doc.text.indexOf('explanation') >1) emit(["explanation"], 1);
     if (doc.text.indexOf('faculty') >1) emit(["faculty"], 1);
     if (doc.text.indexOf('feedback') >1) emit(["feedback"], 1);
     if (doc.text.indexOf('graduate') >1) emit(["graduate"], 1);
     if (doc.text.indexOf('goal') >1) emit(["goal"], 1);
     if (doc.text.indexOf('instructor') >1) emit(["instructor"], 1);
     if (doc.text.indexOf('internship') >1) emit(["internship"], 1);
     if (doc.text.indexOf('knowledge') >1) emit(["knowledge"], 1);
     if (doc.text.indexOf('objectives') >1) emit(["objectives"], 1);
     if (doc.text.indexOf('participation') >1) emit(["participation"], 1);
     if (doc.text.indexOf('peer') >1) emit(["peer"], 1);
     if (doc.text.indexOf('plagiarism') >1) emit(["plagiarism"], 1);
     if (doc.text.indexOf('doctor') >1) emit(["doctor"], 1);
     if (doc.text.indexOf('question') >1) emit(["question"], 1);
     if (doc.text.indexOf('quiz') >1) emit(["quiz"], 1);
     if (doc.text.indexOf('reading') >1) emit(["reading"], 1);
     if (doc.text.indexOf('report') >1) emit(["report"], 1);
     if (doc.text.indexOf('research') >1) emit(["research"], 1);
     if (doc.text.indexOf('rubric') >1) emit(["rubric"], 1);
     if (doc.text.indexOf('scholarship') >1) emit(["scholarship"], 1);
     if (doc.text.indexOf('science') >1) emit(["science"], 1);
     if (doc.text.indexOf('technology') >1) emit(["technology"], 1);
     if (doc.text.indexOf('engineering') >1) emit(["engineering"], 1);
     if (doc.text.indexOf('mathematics') >1) emit(["mathematics"], 1);
     if (doc.text.indexOf('study') >1) emit(["study"], 1);
     if (doc.text.indexOf('syllabus') >1) emit(["syllabus"], 1);
     if (doc.text.indexOf('textbook') >1) emit(["textbook"], 1);
     if (doc.text.indexOf('understand') >1) emit(["understand"], 1);
     if (doc.text.indexOf('writing') >1) emit(["writing"], 1);
     if (doc.text.indexOf('write') >1) emit(["write"], 1);
}
'''

reduce_word_local_edu = "_count"

map_year_local_edu = '''function (doc) {
    emit(doc.year, 1);
  }
'''

reduce_year_local_edu = "_count"


local_edu_tweet = {
        "_id": f"_design/view",
        "views": {
            "word": {
                "map": map_word_local_edu,
                "reduce": reduce_word_local_edu
            },
            "year": {
                "map": map_year_local_edu,
                "reduce": reduce_year_local_edu
            }
        },
        "language": "javascript",
        "options": {"partitioned": False}
}
db.save(local_edu_tweet)


# local_data_place_envir

db = couch["local_data_place_environment"]

map_word_local_envir = '''function(doc) {
     if (doc.text.indexOf('atmosphere') >1) emit(["atmosphere"], 1);
     if (doc.text.indexOf('biodegradable') >1) emit(["biodegradable"], 1);
     if (doc.text.indexOf('biodiversity') >1) emit(["biodiversity"], 1);
     if (doc.text.indexOf('carbon') >1) emit(["carbon"], 1);
     if (doc.text.indexOf('dioxide') >1) emit(["dioxide"], 1);
     if (doc.text.indexOf('carcinogen') >1) emit(["carcinogen"], 1);
     if (doc.text.indexOf('climate') >1) emit(["climate"], 1);
     if (doc.text.indexOf('coal') >1) emit(["coal"], 1);
     if (doc.text.indexOf('compost') >1) emit(["compost"], 1);
     if (doc.text.indexOf('conservation') >1) emit(["conservation"], 1);
     if (doc.text.indexOf('contaminant') >1) emit(["contaminant"], 1);
     if (doc.text.indexOf('deforestation') >1) emit(["deforestation"], 1);
     if (doc.text.indexOf('deforest') >1) emit(["deforest"], 1);
     if (doc.text.indexOf('disposable') >1) emit(["disposable"], 1);
     if (doc.text.indexOf('diversity') >1) emit(["diversity"], 1);
     if (doc.text.indexOf('ecology') >1) emit(["ecology"], 1);
     if (doc.text.indexOf('ecosystem') >1) emit(["ecosystem"], 1);
     if (doc.text.indexOf('emission') >1) emit(["emission"], 1);
     if (doc.text.indexOf('endangered') >1) emit(["endangered"], 1);
     if (doc.text.indexOf('energy') >1) emit(["energy"], 1);
     if (doc.text.indexOf('environment') >1) emit(["environment"], 1);
     if (doc.text.indexOf('erosion') >1) emit(["erosion"], 1);
     if (doc.text.indexOf('extinct') >1) emit(["extinct"], 1);
     if (doc.text.indexOf('fossil') >1) emit(["fossil"], 1);
     if (doc.text.indexOf('fuel') >1) emit(["fuel"], 1);
     if (doc.text.indexOf('landfill') >1) emit(["landfill"], 1);
     if (doc.text.indexOf('recycle') >1) emit(["recycle"], 1);
     if (doc.text.indexOf('sewerage') >1) emit(["sewerage"], 1);
     if (doc.text.indexOf('air') >1) emit(["air"], 1);
     if (doc.text.indexOf('temp') >1) emit(["temp"], 1);
     if (doc.text.indexOf('waste') >1) emit(["waste"], 1);
     if (doc.text.indexOf('eco') >1) emit(["eco"], 1);
     if (doc.text.indexOf('environs') >1) emit(["environs"], 1);
     if (doc.text.indexOf('relict') >1) emit(["relict"], 1);
     if (doc.text.indexOf('hotbed') >1) emit(["hotbed"], 1);
     if (doc.text.indexOf('green') >1) emit(["green"], 1);
     if (doc.text.indexOf('habitat') >1) emit(["habitat"], 1);
     if (doc.text.indexOf('ambiance') >1) emit(["ambiance"], 1);
     if (doc.text.indexOf('aciduricr') >1) emit(["aciduric"], 1);
     if (doc.text.indexOf('site') >1) emit(["site"], 1);
     if (doc.text.indexOf('effect') >1) emit(["effect"], 1);
     if (doc.text.indexOf('community') >1) emit(["community"], 1);
     if (doc.text.indexOf('produce') >1) emit(["produce"], 1);
     if (doc.text.indexOf('consume') >1) emit(["consume"], 1);
     if (doc.text.indexOf('decompose') >1) emit(["decompose"], 1);
     if (doc.text.indexOf('adapt') >1) emit(["adapt"], 1);
     if (doc.text.indexOf('habitat') >1) emit(["habitat"], 1);
     if (doc.text.indexOf('weather') >1) emit(["weather"], 1);
     if (doc.text.indexOf('impact') >1) emit(["impact"], 1);
     if (doc.text.indexOf('global') >1) emit(["global"], 1);
     if (doc.text.indexOf('change') >1) emit(["change"], 1);
     if (doc.text.indexOf('precipitation') >1) emit(["precipitation"], 1);
     if (doc.text.indexOf('gas') >1) emit(["gas"], 1);
     if (doc.text.indexOf('ems') >1) emit(["ems"], 1);
     if (doc.text.indexOf('pollution') >1) emit(["pollution"], 1);
     if (doc.text.indexOf('green') >1) emit(["green"], 1);
}
'''

reduce_word_local_envir = "_count"

map_year_local_envir = '''function (doc) {
    emit(doc.year, 1);
    }
'''

reduce_year_local_envir = "_count"


local_envir_tweet = {
        "_id": f"_design/view",
        "views": {
            "word": {
                "map": map_word_local_envir,
                "reduce": reduce_word_local_envir
            },
            "year": {
                "map": map_year_local_envir,
                "reduce": reduce_year_local_envir
            }
        },
        "language": "javascript",
        "options": {"partitioned": False}
}
db.save(local_envir_tweet)


