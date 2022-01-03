from .. import ma
from .models import Footballer


class FootballerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Footballer
