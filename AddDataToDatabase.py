import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-39b44-default-rtdb.firebaseio.com/"
})
ref=db.reference('Students')
data={
    "12345":{
        "name":"John Cena",
        "major":"Wrestling",
        "starting_year":2002,
        "total_attendance":6,
        "standing":"G",
        "year":4,
        "last_attendance_time":"2022-11-12 00:54:34"

    },
    "23456":{
        "name":"Roman Reigns",
        "major":"Wrestling",
        "starting_year":2012,
        "total_attendance":8,
        "standing":"B",
        "year":2,
        "last_attendance_time":"2022-10-12 00:54:34"

    },
    "34567":{
        "name":"Manav Shah",
        "major":"Wrestling",
        "starting_year":2022,
        "total_attendance":6,
        "standing":"C",
        "year":1,
        "last_attendance_time":"2024-04-04 00:54:34"

    },
    "56789":{
        "name":"Dev Bhuva",
        "major":"Panchaat",
        "starting_year":2003,
        "total_attendance":5,
        "standing":"B",
        "year":4,
        "last_attendance_time":"2022-11-12 00:54:34"
    }
    
}
for key,value in data.items():
    ref.child(key).set(value)


