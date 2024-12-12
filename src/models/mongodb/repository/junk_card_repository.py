import pymongo


class JunkCardRepository:

    def __init__(self, db_connection) -> None:

        self.__db_connection = db_connection
        self.__collection = self.__db_connection.get_collection("junk_card")


    def insert_document(self, document: dict) -> None:
        self.__collection.insert_one(document)


    def insert_list_of_documents(self, list_documents: list) -> None:

        self.__collection.insert_many(list_documents)

        
    def select_one(self, document_filter: dict) -> dict:
        
        response = self.__collection.find_one(document_filter)
        
        return response


    def select_many(self, document_filter: dict) -> pymongo.CursorType:

        response = self.__collection.find(document_filter)
        
        return response
