from flask import Flask, request
import pymongo , json
from bson.objectid import ObjectId
from bson import json_util

#Creating the Flask app
app=Flask(__name__)

#Connecting to the Database
client = pymongo.MongoClient("mongodb+srv://Project:bmnp12105@cluster0.vgwcjai.mongodb.net/")
db = client.VaccinationProject

#Post Request to insert a new record
@app.route('/patients', methods=['POST'])
def patients_record():
    json = request.json
    id = db.Patients.insert_one(json)
    return "Patient Record was created sucessfully"


# Get patients details from patients collection.
@app.route('/allPatients', methods=['GET'])
def get_patients():
    patients = db.Patients.find()
    output = json.loads(json_util.dumps(patients))
    return output


@app.route('/patients/<id>', methods=['GET'])
def get_patient(id):
    patient = db.Patients.find_one({"_id": ObjectId(id)})
    output = json.loads(json_util.dumps(patient))
    return output


if __name__ == '__main__':
    app.run()