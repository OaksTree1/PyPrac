import pymongo

class dataBase(object):
    URI = 123
    DATABASE = None

    @staticmethod
    def initialize():
        Client = pymongo.MongoClient(dataBase.URI)
        dataBase.DATABASE = Client['admin']

    @staticmethod
    def insert(collection, data):
        dataBase.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return dataBase.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return dataBase.DATABASE[collection].find_one(query)

    @staticmethod
    def insertquery(collection, query):
        dataBase.DATABASE[collection].insert(query)

