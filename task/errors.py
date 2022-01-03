from flask import jsonify
from werkzeug.exceptions import HTTPException


def init_app(app):
    @app.errorhandler(HTTPException)
    def handle(e):
        return jsonify({
            'detail': e.description
        }), e.code
