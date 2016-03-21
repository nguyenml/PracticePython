from random import choice
from time import sleep

from gamestate import Gamestate

class Game(object):
    """
    Represents the application as a game.
    """

    def __init__(self, db):
        self.gamestate = Gamestate(db)
        self.gamestate.init_locations(db)
        self.gamestate.init_persons(db)
        self.gamestate.init_items(db)
        self.is_running = True
        self.db = db

        self.start()
    def start(self):
        while(self.is_running):
            self.update()

    def update(self):
        self.gamestate.update()
