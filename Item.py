class Item:
    def __init__(self, name, usable, description, potency):
        self.name = name
        self.usable = usable
        self.description = description
        self.potency = potency 
    
    def print_item(self, location):
        if location in self.usable:
            print(f"{self.name} - {self.description}")
    
    def check_item(self, item_input, location):
        if self.name == item_input and location in self.usable:
            return True
        return False
        


