from base import Item, Person, Gamestate, Location
from random import choice
from time import sleep
FIRSTNAMEPOOL = ["Matt","Ben","Kyle","Mel","Joey"]
LASTNAMEPOOL = ["Leblanc","Stiller","Hannon","Pratt","Carter"]
class Game(object):
    DEFAULT_WIDTH = 10
    DEFAULT_LENGTH = 10

    def __init__(self,client):
        self.gamestate = Gamestate()
        self.is_running = True
        self.client = client
        # Initialize the locations
        temp_world = [Location(x,y,"An arena") for x in range(self.DEFAULT_WIDTH) for y in range(self.DEFAULT_LENGTH)]
        temp_people = [Person(choice(FIRSTNAMEPOOL),choice(LASTNAMEPOOL)) for x in range(20)]
        self.gamestate.place = temp_world
        self.gamestate.people = temp_people

    def start(self):
        while(self.is_running):
            sleep(5)
            self.update()

    def update(self):
        direction = ["N","S","W","E"]
        MOVE = 1
        for x in self.gamestate.people:
            x.direction = choice(direction)
            x.location = x.location.x
            x.update(self.location,self.hp,self.sp)
