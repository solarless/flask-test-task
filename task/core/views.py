from flask import jsonify
from flask import request
from flask.views import MethodView

from .models import Footballer
from .schemas import FootballerSchema


class FootballerListCreateView(MethodView):
    def get(self):
        footballers = Footballer.query.all()
        schema = FootballerSchema(many=True).dump(footballers)
        return jsonify(schema)

    def post(self):
        data = request.get_json()
        schema = FootballerSchema()
        errors = schema.validate(data)

        if not errors:
            footballer = Footballer(**data).save()
            return jsonify(schema.dump(footballer)), 201  # Created
        return jsonify(errors), 400  # Bad Request


class FootballerDeleteView(MethodView):
    def delete(self, id):
        footballer = Footballer.query.get_or_404(id)
        schema = FootballerSchema()

        if footballer.number == 10:
            return jsonify({
                'detail': 'You cannot delete the footballer with number 10.'
            }), 403  # Forbidden

        footballer.delete()
        return jsonify(schema.dump(footballer)), 204  # No Content
