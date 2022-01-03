from flask_sqlalchemy import Model
from flask_sqlalchemy import SQLAlchemy


class TaskModel(Model):
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self


db = SQLAlchemy(model_class=TaskModel)
