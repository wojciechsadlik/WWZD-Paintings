from flask import Flask
from flask_restful import Api
from painting import Painting
from paintings_list import Paintings_list
import database
import painting_processing
from flasgger import Swagger

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'

api = Api(app)

swagger = Swagger(app)

api.add_resource(Painting, '/painting/<painting_id>')
api.add_resource(Paintings_list, '/paintings_list')

painting_processing.fit_pca()

database.db_init(app)

if __name__ == '__main__':
    app.run(debug=True)