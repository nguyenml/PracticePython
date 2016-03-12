
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

