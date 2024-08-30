from flask import Blueprint

bp = Blueprint(name='posts', import_name=__name__)

from app.posts import routes