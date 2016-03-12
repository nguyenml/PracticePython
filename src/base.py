
# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import random

# <codecell>

class Gamestate(object):
    # This is a comment
    """
    """
    def __init__(self, persons=[[]], items=[]):
        """
        This is what a docstring is.
        """
        # Python constructor
        self.place = None # Index by x,y coordinates  2D array
        self.people = [] # Index by Name 2D hashmap indexed by lastname, and firstname
        self.things = None # Simple Sparse Array
        self.serial_counter = 0 # this is for the item serialization process
        self.update = None
# <codecell>

class Person(object):
    # Class variables
    DEFAULT_FIRSTNAME = "FIRSTNAME"
    DEFAULT_LASTNAME = "LASTNAME"

    def __init__(self, first=None, last=None, location =None, hp = None, sp = None):
        """
        Create a person object
        """
        # Object variables
        if(first and last):
            self.first_name = first
            self.last_name = last
        else:
            # Defaults
            self.first_name = Person.DEFAULT_FIRSTNAME
            self.last_name = Person.DEFAULT_LASTNAME
        self.location = location
        self.hp = hp
        self.sp = sp

    def update(self,location,hp,sp):
        self.location = location
        self.hp = hp
        self.sp = sp
        pass

# <codecell>

class Location(object):
    DEFAULT_X_COOR = 0
    DEFAULT_Y_COOR = 0
    DEFAULT_DESC = None

    def __init__(self, x_coord, y_coord, space_filled, desc="An empty room"):
        """
        Create a location
        """
        if(x_coord and y_coord and desc):
            self.x_coord = x_coord
            self.y_coord = y_coord
            self.desc = desc
        else:
            self.x_coord = Location.DEFAULT_X_COOR
            self.y_coord = Location.DEFAULT_Y_COOR
            self.desc = self.DEFAULT_DESC
        self.space_filled = space_filled

    def update(self,filled):
        self.space_filled = space_filled


# <codecell>

class Item(object):
    """
    Items have a serial number, a one word string describing it, and a quality
    score from 1 to 100
    """
    DEFAULT_ITEM_NAME = ""
    def __init__(self,item_name=None):
        """
        Create an Item
        """
        if(name and itemID):
            self.item_name = item_name
        else:
            self.item_name = Item.DEFAULT_ITEM_NAME

    def set_serial_number(self, serial):
        self.serial = serial

# <codecell>

def start_gamestate():
    """
    Initializes game objects
    """
    # generate 30 people here where first name is a number
    # and last name is a number
    DEFAULT_SIZE = 30
    # Create persons
    persons = []
    for x in range(DEFAULT_SIZE):
        person.append(Person(str(x),str(x+1)))
    # Create items
    items = []
    for x in range(DEFAULT_SIZE):
        temporary = Item(str(x))
        temporary.set_serial_number(my_starting_gamestate.serial_counter) # Assigns a serial
        my_starting_gamestate.serial_counter += 1 # Increments the counter
    # Create locations
    # We create a bare array consisting of 0's first
    locations = [[0 for _ in range(DEFAULT_SIZE)] for _ in range(DEFAULT_SIZE)]
    for x in range(DEFAULT_SIZE):
        for y in range(DEFAULT_SIZE):
            # Overwritin the 0's with an actual object
            locations[x][y] = Location(x,y,str(random.randint(1, 100)))
    # Finally initialize
    my_starting_gamestate = Gamestate(persons, items)

