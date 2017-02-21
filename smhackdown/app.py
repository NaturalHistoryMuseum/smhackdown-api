from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Images(Resource):
    def get(self):
        return [
            {},
            {}
        ]
    def post(self):
        return 

class TopTen(Resource):
    def get(self):
        return []       

api.add_resource(Images, '/images')
api.add_resource(TopTen, '/topten')

if __name__ == '__main__':
    app.run(debug=True)