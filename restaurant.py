class Restaurant:
    def  __init__(self, name, type):
        # inicializa os atriubutos do restaurante
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f"{self.name} is a {self.type} restaurant.")
    
    def open_restaurant(self):
        print(f"{self.name} is open.")