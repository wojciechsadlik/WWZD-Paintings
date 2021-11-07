from flask_restful import Resource, reqparse, fields, marshal_with, abort
from database import PaintingModel
from painting import marshal_painting

class Paintings_list(Resource):
    @marshal_with(marshal_painting)
    def get(self):
        result = PaintingModel.query.all()
        
        if not result:
            abort(404, message='Error occured while getting paintings')
        
        return result, 200
