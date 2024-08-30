from flask import Blueprint

bp = Blueprint(name='questions', import_name=__name__)

from app.questions import routes