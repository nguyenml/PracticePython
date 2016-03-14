RESOURCES = ["Air", "Water", "Food"]

from random import choice

class Location(object):

    def __init__(self, x=0, y=0, capacity=15, resources=[], desc="An empty room"):
        """
        Create a location
        """
        self.x = x
        self.y = y
        self.desc = desc
        self.capacity = capacity
        self.things = []
        self.resources = [choice(RESOURCES)]
    def is_full(self):
        if(len(self.things == self.capacity)):
            return True
        return False

    def update(self,filled):
        self.space_filled = space_filled

