from flask import Flask
from flask_restful import Api
from painting import Painting
import database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

database.db_init(app)

api.add_resource(Painting, '/painting')

if __name__ == '__main__':
    app.run(debug=True)