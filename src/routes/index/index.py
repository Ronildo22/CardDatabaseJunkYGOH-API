from flask import Blueprint, redirect


index_bp = Blueprint('index_bp', __name__)


@index_bp.get('/')
def redirect_documentation():

    return redirect('doc/swagger', code=302)

