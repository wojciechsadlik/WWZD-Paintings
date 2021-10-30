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
        file_path = os.path.join('./uploads', style, image_file.filename)
        print(image_file, file_path)
        image_file.save(file_path)

        super(PaintingModel, self).__init__(x=x, y=y, style=style, file_path=file_path)

def db_init(app):
    db.init_app(app)

    if (not os.path.isfile('./database.db')):
        with app.app_context():
            db.create_all()

def db_clear():
    os.remove('./database.db')
    for dirpath, dirnames, files in os.walk('./uploads'):
        for file_name in files:
            os.remove(os.path.join(dirpath, file_name))