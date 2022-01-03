from flask import Blueprint

from .views import FootballerListCreateView
from .views import FootballerDeleteView


blueprint = Blueprint('core', __name__)


blueprint.add_url_rule(
    '/footballers',
    view_func=FootballerListCreateView.as_view('footballer_list_create')
)
blueprint.add_url_rule(
    '/footballers/<int:id>/delete',
    view_func=FootballerDeleteView.as_view('footballer_delete')
)
