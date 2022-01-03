from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

from .db import db


ma = Marshmallow()
migrate = Migrate()


def create_app():
    app = Flask('task')
    app.config.from_object('task.config')

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    from .core.routes import blueprint as core

    app.register_blueprint(core, url_prefix='/api')

    import task.core.models

    return app
