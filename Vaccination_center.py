from flask import Flask, request
import pymongo , json
from bson.objectid import ObjectId
from bson import json_util

#Creating the Flask app
app=Flask(__name__)

#Connecting to the Database
client = pymongo.MongoClient("mongodb+srv://Project:bmnp12105@cluster0.vgwcjai.mongodb.net/")
db = client.VaccinationProject


# To get the available time slots based on the selected location
@app.route('/timeslots', methods=['GET'])
def get_manufacturer():
    location = request.args.get('location')
    locations = db.Vaccination_center.find({"location": location})
    slots = []
    for location in locations:
        slots.append({location["location"] : location["availableTimeSlots"]})
    output = json.loads(json_util.dumps(slots))
    return output

# To get the available doses based on the selected location
@app.route('/getAvailableDoses', methods=['GET'])
def get_doses():
    location = request.args.get('location')
    locations = db.Vaccination_center.find({"location": location})
    doses = []
    for location in locations:
        doses.append({location["location"] : location["available_Doses"]})
    output = json.loads(json_util.dumps(doses))
    return output


# To get the available locations, available timeslots on the selected date from vaccination center
@app.route('/getAvailableLocationsAndSlots', methods=['GET'])
def get_available_slots():
    date = request.args.get('date')
    # Only get location and availableTimeSlots from the database
    locations = db.Vaccination_center.find({"avaliableDates": {"$in": [date]}}, {"center_name":1, "location": 1, "availableTimeSlots": 1})
    # slots = []
    output = json.loads(json_util.dumps(locations))
    return output


if __name__ == '__main__':
    app.run()
    