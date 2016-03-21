from random import choice
from time import sleep
import uuid
from gamestate import Gamestate

class Game(object):
    """
    Represents the application as a game.
    """

    def __init__(self, db):
        ts = uuid.uuid4().int
        self.db = db[str(ts)]
        self.gamestate = Gamestate(db[str(ts)])
        self.gamestate.init_locations(db[str(ts)])
        self.gamestate.init_persons(db[str(ts)])
        self.gamestate.init_items(db[str(ts)])
        self.is_running = True
        self.start()
    def start(self):
        while(self.is_running):
            self.update()

    def update(self):
        self.gamestate.update()
