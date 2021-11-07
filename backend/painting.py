from flask_restful import Resource, reqparse, fields, marshal_with, abort
from database import db, PaintingModel

marshal_painting = {
    'id': fields.Integer,
    'x': fields.Float,
    'y': fields.Float,
    'style': fields.String
}

class Painting(Resource):
    @marshal_with(marshal_painting)
    def get(self, painting_id):
        """
        Get painting info
        ---
        parameters:
          - in: path
            name: painting_id
            type: integer
            required: true
        responses:
          200:
            description: Painting information
            schema:
              id: Painting
              properties:
                id:
                  type: integer
                x:
                  type: number
                y:
                  type: number
                style:
                  type: string
          404:
            description: Painting not found
        """

        result = PaintingModel.query.filter_by(id=painting_id).all()
        
        if not result:
            abort(404, message='Painting with id {} does not exist'.format(painting_id))
        
        return result, 200

