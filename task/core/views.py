from flask import jsonify
from flask import request
from flask.views import MethodView

from .models import Footballer
from .schemas import FootballerSchema


class FootballerListCreateView(MethodView):
    def get(self):
        footballers = Footballer.query.all()
        schema = FootballerSchema(many=True)
        return jsonify(schema.dump(footballers))
    
    def post(self):
        data = request.get_json()
        footballer = Footballer(
            name=data.get('name'),
            number=data.get('number')
        ).save()
        schema = FootballerSchema()
        return jsonify(schema.dump(footballer)), 201  # Created


class FootballerDeleteView(MethodView):
    def delete(self, id):
        footballer = Footballer.query.get(id)
        schema = FootballerSchema()

        if footballer.number == 10:
            return jsonify({
                'detail': 'You cannot delete the footballer with number 10.'
            }), 403  # Forbidden

        footballer.delete()
        return jsonify(schema.dump(footballer)), 204  # No Content
