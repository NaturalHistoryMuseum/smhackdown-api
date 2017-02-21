from flask import Flask
import os
from flask_restful import Resource, Api
from flask_cors import CORS
import dataset
import random

db = dataset.connect(os.environ['DATABASE_URL'])
app = Flask(__name__)
api = Api(app)

class Objects(Resource):
    def get(self):
        objects = db['objects']

        # FIXME: This doesn't order by number of likes
        result = db.query('SELECT DISTINCT ON (institution) id, name, institution, image_url FROM objects ORDER BY institution, random()')
        ret = list()
        for row in result:
            ret.append(row)
        # Return random 2
        return random.sample(ret, 2)

    def post(self):
        """
        Save a like to the database
        """
        return {}

class TopTen(Resource):
    def get(self):
        return []       

api.add_resource(Objects, '/objects')
api.add_resource(TopTen, '/topten')

if __name__ == '__main__':
    app.run(debug=True)