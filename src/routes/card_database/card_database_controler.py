from flask import Blueprint, send_file


card_database_bp = Blueprint('card_database_bp', __name__)


@card_database_bp.get('/cardDatabase/<card_name>')
def get_card_image(card_name: str):

    return send_file(f'../../../card_database/{card_name}.jpg')
