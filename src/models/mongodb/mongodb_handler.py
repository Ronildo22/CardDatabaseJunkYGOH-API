from pymongo import MongoClient


class MongoDBHandler:


    def __init__(self) -> None:

        self.__connection_string = 'mongodb://{}:{}/?authsource=admin'.format(
            'localhost',    # host
            '27017',        # port
        )

        self.__database_name = 'YGOHCardBase'
        self.__client= None
        self.__db_connection = None


    def connect_database(self) -> None:

        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client[self.__database_name]


    def get_db_connection(self):

        return self.__db_connection


    def disconnect_database(self) -> None:
        
        self.__client.close()
