import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PaintingModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.Float, nullable=False)
    y = db.Column(db.Float, nullable=False)
    style = db.Column(db.String(25), nullable=False)
    file_path = db.Column(db.Text)

    def __init__(self, x, y, style, image_file):
        upload_folder = db.get_app().config['UPLOAD_FOLDER']
        file_path = os.path.join(upload_folder, style, image_file.filename)
        
        image_file.save(file_path)

        super(PaintingModel, self).__init__(x=x, y=y, style=style, file_path=file_path)


def db_init(app):
    db.init_app(app)
    upload_folder = app.config['UPLOAD_FOLDER']

    if not os.path.isfile(app.config['SQLALCHEMY_DATABASE_URI']):
        create_db(app)

    if not os.path.isdir(upload_folder):
        create_upload_folder(upload_folder)

    
def db_clear():
    os.remove(db.get_app().config['SQLALCHEMY_DATABASE_URI'])

    upload_folder = db.get_app().config['UPLOAD_FOLDER']
    for dirpath, dirnames, files in os.walk(upload_folder):
        for file_name in files:
            os.remove(os.path.join(dirpath, file_name))


def create_db(app):
    with app.app_context():
        db.create_all()


def create_upload_folder(upload_folder):
    os.mkdir(upload_folder)
    for dirpath, dirnames, files in os.walk('dataset'):
        for dirname in dirnames:
            os.mkdir(os.path.join(upload_folder, dirname))


