import requests
import json


def test_card_name_exist():
    
    card_name = 'catapult_warrior'
    
    payload = {'cardName': card_name}
    
    response = requests.get(
        url='/cardDatabase', params=payload
    )
    
    assert response.status_code == 200


def test_card_information():
    
    card_name = 'catapult_warrior'
    
    payload = {'cardName': card_name}
    
    response = requests.get(
        url='/cardDatabase', params=payload
    )
    
    assert response.content == {'text': 'teste'}

