from flask import Flask, request
import os
from flask_restful import Resource, Api
from flask_cors import CORS
import dataset
import random

db = dataset.connect(os.environ['DATABASE_URL'])
app = Flask(__name__)

PREFIX = "/api"

api = Api(app, prefix=PREFIX)

cors = CORS(app, resources={r"{0}/*".format(PREFIX): {"origins": "*"}})

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
        object_id = request.json.get('object_id', None)
        if object_id:
            likes_tbl = db['likes']
            likes_tbl.insert(dict(object_id=object_id))

        return {}

class TopTen(Resource):
    def get(self):
        result = db.query('select objects.*, (select count(*) from likes where likes.object_id = id) as likes_count from objects order by likes_count desc limit 10')
        return list(result)

class TopInstitutions(Resource):
    def get(self):
        result = db.query('select institution as code, count(l.*) as likes_count from objects o left join likes l on l.object_id = o.id group by institution order by likes_count desc')
        ret = list()

        institution_info = {
            'BM': {
                'name': 'British Museum',
                'logo': 'British_Museum_Logo.jpg'
            },
            'V&A': {
                'name': 'Victoria & Albert Museum',
                'logo': 'vanda.png'
            },
            'SM': {
                'name': 'Science Museum',
                'logo': 'ScienceMuseum.png'
            },
            'NHM': {
                'name': 'Natural History Museum',
                'logo': 'new-nhm-logo.gif'
            }                 
        }

        for row in result:
            # Merge in extra info
            row.update(institution_info[row['code']])
            ret.append(row)

        return ret

api.add_resource(Objects, '/objects')
api.add_resource(TopTen, '/top-ten')
api.add_resource(TopInstitutions, '/institutions')

if __name__ == '__main__':
    app.run(debug=True)