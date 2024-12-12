from flask import Flask
from flask_pydantic_spec import FlaskPydanticSpec

from ..routes.card_database.card_database_controler import card_database_bp
from ..routes.index.index import index_bp

app = Flask(__name__)

spec = FlaskPydanticSpec(
    backend_name='flask',
    title='Card Database Yu-gi-Oh Monster Archetype "Junk"',
    version='v1.0',
    path="doc"
)
spec.register(app)

app.register_blueprint(card_database_bp)
app.register_blueprint(index_bp)
