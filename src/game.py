from base import Item, Person, Gamestate, Location
from random import choice, randint
from time import sleep
FIRSTNAMEPOOL = ["Matt","Ben","Kyle","Mel","Joey"]
LASTNAMEPOOL = ["Leblanc","Stiller","Hannon","Pratt","Carter"]
class Game(object):
    DEFAULT_WIDTH = 10
    DEFAULT_LENGTH = 10

    def __init__(self):
        self.gamestate = Gamestate()
        self.is_running = True

        # Initialize the locations
        temp_world = [[Location(x,y,"An arena") for x in range(self.DEFAULT_WIDTH)] for y in range(self.DEFAULT_LENGTH)]
        temp_people = [Person(choice(FIRSTNAMEPOOL),
                        choice(LASTNAMEPOOL),
                        location=temp_world[randint(0,9)][randint(0,9)]) for x in range(20)]
        self.gamestate.place = temp_world
        self.gamestate.people = temp_people

    def start(self):
        STOP_COUNTER = 10
        counter = 0
        while(self.is_running):
            sleep(1)
            self.update()
            counter += 1
            if(counter == STOP_COUNTER):
                self.is_running = False
            
    def update(self):
            
        for person in self.gamestate.people:
            x_delta = choice([-1, 0, 1])
            y_delta = choice([-1, 0, 1])
            
            p_x, p_y = person.location.x_coord, person.location.y_coord
            
            new_room_x = (x_delta + person.location.x_coord) % 10
            new_room_y = (y_delta + person.location.y_coord) % 10
           
            n_r_x = new_room_x
            n_r_y = new_room_y
           
            print("Person is moving from %s-%s to %s-%s" % (p_x, p_y, n_r_x, n_r_y)) 
            person.update(self.gamestate.place[new_room_x][new_room_y], person.hp, person.sp)

if __name__ == "__main__":
    a = Game()
    a.start()
    