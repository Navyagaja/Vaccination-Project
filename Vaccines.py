from flask import Flask, request
import pymongo , json
from bson.objectid import ObjectId
from bson import json_util

#Creating the Flask app
app=Flask(__name__)

#Connecting to the Database
client = pymongo.MongoClient("mongodb+srv://Project:bmnp12105@cluster0.vgwcjai.mongodb.net/")
db = client.VaccinationProject

# To get the recommended and required vaccines based on the age 
@app.route('/vaccines', methods=['GET'])
def get_vaccines():
    age = request.args.get('age')
    age = int(age)
    vaccines = db.Vaccines.find({"ageGroup.min": {"$lte": age}, "ageGroup.max": {"$gte": age}})
    recommended = []
    required = []
    for vaccine in vaccines:
        if vaccine["required"]:
            required.append({
                "name": vaccine["name"],
                "description": vaccine["description"],
                "requiredDoses": vaccine["requiredDoses"],
                "price": vaccine["price"]
            })
        if vaccine["recommended"]:
            recommended.append({
                "name": vaccine["name"],
                "description": vaccine["description"],
                "requiredDoses": vaccine["requiredDoses"],
                "price": vaccine["price"]
            })  
    output = json.loads(json_util.dumps({"recommended": recommended, "required": required}))
    return output





if __name__ == '__main__':
    app.run()