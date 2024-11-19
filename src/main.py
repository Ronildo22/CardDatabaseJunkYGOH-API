from flask import Flask, request, send_file
from flask_pydantic_spec import FlaskPydanticSpec


app = Flask(__name__)
spec = FlaskPydanticSpec(
    backend_name='flask', 
    title='Card Database Yu-gi-Oh Monster Archetype "Junk"', 
    version='v1.0',
    path="doc"
)
spec.register(app)


@app.get('/cardDatabase/<card_name>')
def get_card_image(card_name: str):

    return send_file(f'../card_database/{card_name}.jpg')


if __name__ == '__main__':

    app.run(
        debug=False, load_dotenv=True
    )
