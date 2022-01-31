import os
from flask_sqlalchemy import SQLAlchemy
import painting_processing

db = SQLAlchemy()


class PaintingModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.Float, nullable=False)
    y = db.Column(db.Float, nullable=False)
    style = db.Column(db.String(25), nullable=False)
    file_path = db.Column(db.Text, nullable=False)


def db_init(app):
    db.init_app(app)
    upload_folder = app.config['UPLOAD_FOLDER']

    if not os.path.isfile('database.db'):
        print(app.config['SQLALCHEMY_DATABASE_URI'])
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
    print('\ncreating database\n')
    with app.app_context():
        db.create_all()

        load_dataset()


def create_upload_folder(upload_folder):
    os.mkdir(upload_folder)


def load_dataset():
    print('\nloading dataset\n')

    for dirpath, dirnames, files in os.walk('dataset'):
        for file_name in files:
            file_path = os.path.join(dirpath, file_name)

            painting_style = os.path.basename(dirpath)

            x, y = painting_processing.get_point(file_path)

            painting = PaintingModel(x=x, y=y, style=painting_style, file_path=file_path)

            db.session.add(painting)

    db.session.commit()

    print('\ndataset loaded\n')


def clear_uploads():
    upload_folder = db.get_app().config['UPLOAD_FOLDER']
    for dirpath, dirnames, files in os.walk(upload_folder):
        for file_name in files:
            os.remove(os.path.join(dirpath, file_name))

    db.session.query(PaintingModel).filter_by(style='uploads').delete()
    db.session.commit()
