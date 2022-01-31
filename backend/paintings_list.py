from flask_restful import Resource, reqparse, fields, marshal_with, abort
import werkzeug
from werkzeug.utils import secure_filename
import os
from database import PaintingModel, db, clear_uploads
from painting import marshal_painting
import painting_processing

painting_post_args = reqparse.RequestParser()
painting_post_args.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')


class Paintings_list(Resource):
    @marshal_with(marshal_painting)
    def get(self):
        """
        Get list of paintings
        ---
        responses:
          200:
            description: List of painting infos
            schema:
              id: Paintings_list
              type: array
              items:
                $ref: '#/definitions/Painting'
          404:
            description: Error occured while getting paintings
        """

        result = PaintingModel.query.all()
        
        if not result:
            abort(404, message='Error occured while getting paintings')
        
        return result, 200

    @marshal_with(marshal_painting)
    def post(self):
        """
        Upload a painting
        ---
        consumes:
          - multipart/form-data
        parameters:
          - in: formData
            name: file
            type: file
            required: true
        responses:
          201:
            description: File uploaded
          400:
            description: No file uploaded
          409:
            description: File already exists
        """

        args = painting_post_args.parse_args()

        image_file = args['file']
        painting_style = 'uploads'

        if image_file is None:
            abort(400, messsage='No file uploaded')

        upload_folder = db.get_app().config['UPLOAD_FOLDER']
        file_path = os.path.join(upload_folder, image_file.filename)

        if (os.path.isfile(file_path)):
            abort(409, message='File already exists')

        image_file.save(file_path)

        x, y = painting_processing.get_point(file_path)
        
        painting = PaintingModel(x=x, y=y, style=painting_style, file_path=file_path)

        db.session.add(painting)
        db.session.commit()

        return 201

    def delete(self):
        clear_uploads()

        return 200
    
