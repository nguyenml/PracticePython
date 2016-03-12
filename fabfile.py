from src.game import Game

def start_db():
    from pymongo import MongoClient
    client = MongoClient('localhost', 27016)
    return client

def start():
    client = start_db()
    game = Game(client)
    game.start()
