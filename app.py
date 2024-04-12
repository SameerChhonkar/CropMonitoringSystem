from flask import Flask, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
connection_string = "mongodb+srv://Sameer:1234testing@cluster0.tyrcgn5.mongodb.net/"
mongo_client = MongoClient(connection_string)
db = mongo_client.CMSDB  # Use your database name
collection = db.CMSCL  # Use your collection name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    # Fetch latest data from MongoDB
    latest_data = collection.find_one(sort=[('_id', -1)])
    if latest_data:
        return jsonify({
            'temperature': latest_data['temperature'],
            'humidity': latest_data['humidity'],
            'soil_moisture': latest_data['soilmoisture'],
            'uv_index': latest_data['uvindex']
        })
    else:
        return jsonify({})  # Return empty JSON if no data is found

