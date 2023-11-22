from flask import Flask, request
import pymongo , json
from bson.objectid import ObjectId
from bson import json_util

#Creating the Flask app
app=Flask(__name__)

#Connecting to the Database
client = pymongo.MongoClient("mongodb+srv://Project:bmnp12105@cluster0.vgwcjai.mongodb.net/")
db = client.VaccinationProject


# To get the manufacturer of vaccines based on the selected vaccine name
@app.route('/manufacterer', methods=['GET'])
def get_manufacturer():
    vaccine = request.args.get('vaccine')
    vaccines = db.Vaccination_category.find({"name": vaccine})
    output = json.loads(json_util.dumps(vaccines))
    return output






if __name__ == '__main__':
    app.run()
    