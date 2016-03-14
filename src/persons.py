class Person(object):
    def __init__(self, first="FIRSTNAME", last="LASTNAME", location =None, hp = None, sp = None):
        # Values
        self.first = first
        self.last = last
        self.hp = hp
        self.sp = sp

        # References
        self.location = location
        self.x = self.location.x
        self.y = self.location.y

    def update(self,location,hp,sp):
        self.location = location
        self.hp = hp
        self.sp = sp
        pass

