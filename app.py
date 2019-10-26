from flask import Flask
from flask_cors import CORS
import json
import db

app = Flask(__name__)
CORS(app)

class Rating:
    def __init__(self, id, name, entries):
        self.id = id
        self.name = name
        self.entries = entries

class RatingEntry:
    def __init__(self, person_id, person_name, rating_value):
        self.person_id = person_id
        self.person_name = person_name
        self.rating_value = rating_value

@app.route('/rating/all')
def all_ratings():
    db.declarations.find()
    return json.dumps([Rating(1, "Pidor Rating", [{"name": "pidor", "rating_value": 0.1337}, {"name": "ebaniy", "rating_value": 0.1228}]).__dict__])

@app.route('/rating/<id>')
def get_rating(id):
    return Rating(1, "Pidor Rating", [{"name": "pidor", "rating_value": 0.1337}, {"name": "ebaniy", "rating_value": 0.1228}]).__dict__

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
