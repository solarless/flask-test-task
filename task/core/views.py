from flask import jsonify
from flask import request
from flask.views import MethodView

from ..exceptions import PermissionDenied
from .models import Footballer
from .schemas import FootballerSchema


class FootballerListCreateView(MethodView):
    def get(self):
        footballers = Footballer.query.all()
        schema = FootballerSchema(many=True).dump(footballers)
        return jsonify(schema)

    def post(self):
        data = request.get_json()
        footballer = Footballer(**data)
        schema = FootballerSchema().dump(footballer)
        errors = schema.validate(data)

        if not errors:
            footballer.save()
            return jsonify(schema), 201  # Created
        return jsonify(errors), 400  # Bad Request


class FootballerDeleteView(MethodView):
    def delete(self, id):
        footballer = Footballer.query.get_or_404(id)
        schema = FootballerSchema().dump(footballer)

        if footballer.number == 10:
            raise PermissionDenied(
                'You cannot delete the footballer with number 10.'
            )

        footballer.delete()
        return jsonify(schema), 204  # No Content
