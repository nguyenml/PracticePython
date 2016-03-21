from Queue import Queue as q

from items import Item
from persons import Person
from locations import Location

from random import randint
from pprint import pprint as p
WIDTH = 1
LENGTH = 1
POPULATION = 100
FIRSTNAMEPOOL = ["Matt","Ben","Kyle","Mel","Joey"]
LASTNAMEPOOL = ["Leblanc","Stiller","Hannon","Pratt","Carter"]

from random import choice
class Gamestate(object):
    def __init__(self, db):
        """
        Represents the actual game
        """
        # Python constructor
        self.locations = None
        self.persons = [] # Index by Name 2D hashmap indexed by lastname, and firstname
        self.things = None # Simple Sparse Array
        self.serial_counter = 0 # this is for the item serialization process
        self.q = q()
        self.db = db

    def init_locations(self):
        temp_world = [[Location(x,y,"An arena") for x in range(WIDTH)] for y in range(LENGTH)]
        self.locations = temp_world

    def init_persons(self):
        x,y = randint(0,WIDTH-1), randint(0,LENGTH-1)
        temp_people = [Person(choice(FIRSTNAMEPOOL), choice(LASTNAMEPOOL), location=self.locations[x][y]) for _ in range(POPULATION)]
        POPULATIONself.persons = temp_people

    def init_items(self):
        pass

    def update(self):
        pass
