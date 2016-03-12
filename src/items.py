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

