from flask import Flask
from flask_restful import Api
from painting import Painting
import database
import painting_processing

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'

api = Api(app)

painting_processing.fit_pca()

database.db_init(app)


api.add_resource(Painting, '/painting')

if __name__ == '__main__':
    app.run(debug=True)