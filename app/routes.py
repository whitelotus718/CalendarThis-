from flask import render_template, Blueprint

bp = Blueprint('main', __name__, "/")

@bp.route('/')
def main():
    # track_views() 
    return "Calendar Working"