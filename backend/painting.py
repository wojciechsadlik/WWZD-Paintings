from flask_restful import Resource, reqparse, fields, marshal_with, abort
import werkzeug
from werkzeug.utils import secure_filename
from database import db, PaintingModel
import painting_processing
import os

painting_post_args = reqparse.RequestParser()
painting_post_args.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
painting_post_args.add_argument('style', type=str)

painting_get_args = reqparse.RequestParser()
painting_get_args.add_argument('id', type=int)

painting = {
    'id': fields.Integer,
    'x': fields.Float,
    'y': fields.Float,
    'style': fields.String
}

class Painting(Resource):
    @marshal_with(painting)
    def get(self):
        args = painting_get_args.parse_args()
        result = PaintingModel.query.filter_by(id=args['id']).all()
        
        if not result:
            abort(404, message='Painting with id {} does not exist'.format(args['id']))
        
        return result, 200

    @marshal_with(painting)
    def post(self):
        args = painting_post_args.parse_args()

        image_file = args['file']
        painting_style = args['style']
        print(image_file)

        if image_file is None:
            abort(400, messsage='No file uploaded')

        x, y = painting_processing.get_point(image_file)

        if painting_style is None:
            painting_style = painting_processing.get_style(image_file)

        upload_folder = db.get_app().config['UPLOAD_FOLDER']
        file_path = os.path.join(upload_folder, painting_style, image_file.filename)
        
        image_file.save(file_path)
        
        painting = PaintingModel(x, y, painting_style, file_path)

        db.session.add(painting)
        db.session.commit()

        return painting, 201