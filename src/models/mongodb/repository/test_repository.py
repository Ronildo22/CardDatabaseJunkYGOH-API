from src.models.mongodb.mongodb_handler import MongoDBHandler
from .junk_card_repository import JunkCardRepository


mongo_connection_handler = MongoDBHandler()
mongo_connection_handler.connect_database()
conn = mongo_connection_handler.get_db_connection()

def test_select_one_document():

    my_doc = {'cardName': 'Junk Warrior'}
    
    junk_card_repository = JunkCardRepository(db_connection=conn)    
    response = junk_card_repository.select_one(document_filter=my_doc)
    
    assert response['cardName'] == 'Junk Warrior'


def test_select_many_document():

    my_doc = {'type': 'Spell Card'}

    junk_card_repository = JunkCardRepository(db_connection=conn)    
    response = junk_card_repository.select_many(document_filter=my_doc)
    
    # assert response['cardName'] == 'Junk Warrior'
