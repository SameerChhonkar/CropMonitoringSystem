import csv
from pymongo import MongoClient
import time

connection_string = "mongodb+srv://Sameer:1234testing@cluster0.tyrcgn5.mongodb.net/"

# Connect to MongoDB Atlas
mongo_client = MongoClient(connection_string)
db = mongo_client.CMSDB  # Use your database name
collection = db.CMSCL  # Use your collection name

csv_file_path = "/Users/sameerchhonkar/Documents/CM-system/Data.csv"

while True:
    # Read data from CSV file
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            # Extract values from the row
            value1, value2, value3, value4 = row
            
            # Create a dictionary with column names and values
            data = {
                "temperature": float(value1),   # Assuming the first value is an integer
                "humidity": float(value2),   # Assuming the second value is an integer
                "soilmoisture": float(value3), # Assuming the third value is a float
                "uvindex": float(value4)    # Assuming the fourth value is an integer
            }
            
            # Insert data into MongoDB
            collection.insert_one(data)

    # Wait for 5 seconds before the next iteration
    time.sleep(5)
