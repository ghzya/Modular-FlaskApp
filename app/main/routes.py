from flask import render_template
from app.main import bp

@bp.route("/")
def index():
    # return "This is The Main Blueprint"
    return render_template("index.html")