from src.game import Game

def start_db():
    from flask.ext.mongoengine import MongoEngine
    db = MongoEngine()
    return db

def start():
    db = start_db()
    game = Game(db)
    game.start()
