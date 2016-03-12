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

