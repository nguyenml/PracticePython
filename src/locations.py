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

