from flask import Flask, request
import pymongo , json
from bson.objectid import ObjectId
from bson import json_util

#Creating the Flask app
app=Flask(__name__)

#Connecting to the Database
client = pymongo.MongoClient("mongodb+srv://Project:bmnp12105@cluster0.vgwcjai.mongodb.net/")
db = client.VaccinationProject

# Post call to insert an appointment record
@app.route('/appointments', methods=['POST'])
def appointment_record():
    json = request.json
    id = db.Appointments.insert_one(json)
    return "Appointment Record was created sucessfully. ID: " + str(id.inserted_id)


# Get all appointments details from appointment collection.(for admin use)
@app.route('/allAppointments', methods=['GET'])
def get_appointments():
    auth = request.authorization
    if auth and auth.username == 'admin' and auth.password == 'admin':
        appointments = db.Appointments.find()
        output = json.loads(json_util.dumps(appointments))
        return output
    else:
        return "You are not authorized to view this page", 403


# If patient books appointment, in db save it as online booking, if vaccination staff books appointment save status as walkin in db.(check user role and update status)
@app.route('/createAppointment', methods=['POST'])
def create_appointment():
    json = request.json
    if json["user_role"] == "patient":
        json["status"] = "online booking"
    elif json["user_role"] == "vaccination staff":
        json["status"] = "walkin"
    else:
        return "User role is not valid", 400
    id = db.Appointments.insert_one(json)
    return "Appointment Record was created sucessfully. ID: " + str(id.inserted_id)


# Get appointment details based on email of patient
@app.route('/appointmentByEmail', methods=['GET'])
def get_appointment():
    email = request.args.get('email')
    appointments = db.Appointments.find({"email": email})
    output = json.loads(json_util.dumps(appointments))
    return output




if __name__ == '__main__':
    app.run()