from flask import Flask, render_template, request, redirect, url_for,jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os
import configparser

# Load env vars
load_dotenv()

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.secret_key = os.getenv("SECRET_KEY")

mongo = PyMongo(app)
file_path="D:\\Project_1\\flask_Practice\\configurationFile.txt"
print("DEBUG: File exists?", os.path.exists(file_path))

@app.route('/')
def index():
    # students = mongo.db.students.find()
    return render_template('index.html')



def parse_config(file_path="D:\\Project_1\\flask_Practice\\configurationFile.txt"):
    """
    Parses the configuration file and returns structured data.
    """
    config = configparser.ConfigParser()
    print("comiiiiiiiiiiiiiiiii")
    try:
        config.read(file_path)

        if not config.sections():
            raise FileNotFoundError("Config file is empty or unreadable")

        parsed_data = {}

        for section in config.sections():
            parsed_data[section] = {}
            for key, value in config.items(section):
                parsed_data[section][key] = value

        return parsed_data

    except FileNotFoundError:
        print("Configuration file not found.")
        return None

    except Exception as e:
        print(f"Error reading configuration: {e}")
        return None

def save_to_mongodb(json_data):
    """
    Saves JSON data into MongoDB.
    """
    try:
        mongo.db.students.insert_one(json_data)
        print("Data successfully saved to MongoDB")
    except Exception as e:
        print(f"Failed to save to MongoDB: {e}")


@app.route('/config', methods=['GET'])
def get_config():
    """
    Returns the latest configuration data stored in the DB.
    """

    data = mongo.db.students.find_one(sort=[('_id', -1)], projection={'_id': 0})

    if not data:
        return jsonify({"message": "No configuration found in database"}), 404

    return jsonify({"configuration": data}), 200


if __name__ == '__main__':
    print("first")
    parsed = parse_config()

    if parsed:
        with app.app_context(): 
            save_to_mongodb(parsed)
        print("Parsed Data:", parsed)
    app.run(host="0.0.0.0", debug=True, port=5000)

