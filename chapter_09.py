from random import randint, choice

class Restaurant:
    def  __init__(self, name, type):
        # inicializa os atriubutos do restaurante
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f"{self.name} is {self.type}.")
    
    def open_restaurant(self):
        print(f"{self.name} is open.")


chinese = Restaurant("lig lig", "chinese")

chinese.describe_restaurant()
print(chinese.name)

class IceCreamStand(Restaurant):
    def __init__(self):
        super().__init__('Ice Cream Truck', 'Ice Cream')

    def flavors(self):
        flavors = ('Chocolate', 'Strawberry', 'Pistachio', 'Orange')
        return flavors
    
ice = IceCreamStand() 
print(ice.flavors())
ice.describe_restaurant()

class User:
    def __init__(self, first, last):
        self.first = first.title()
        self.last = last.title()
        self.login_attempts = 0

    def describe_user(self):
        return f"First name: {self.first}, last name: {self.last}."
    
    def greet_user(self):
        return f"Salutations {self.first} {self.last}."

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        return self.privileges

class Admin(User):
    def __init__(self, first, last):
        super().__init__(first, last)
        self.privileges = Privileges()  # começa com vazio

# Teste
gunha = Admin('gunha', 'silva')
gunha.privileges = Privileges(("can add post", "can delete post", "can ban user"))

print(gunha.describe_user())
print(gunha.privileges.show_privileges())  # 👍 funciona agora

class Battery:
    def __init__(self, battery_size=40):
        """Inicializa os atributos da bateria"""
        self.battery_size = battery_size

    def describe_battery(self):
        return f'This car has a {self.battery_size}-kWH battery.'
    
    def get_range(self):
        """Return the range on base of the batterys size"""
        ranges = {40: 150, 65: 225}
        return ranges.get(self.battery_size, "Unknown range")
    
    def return_range(self):
        range_info = self.get_range()
        return f"This car has a range of {range_info}." 
       
    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65
    
pingas = Battery()
print(pingas.describe_battery())
print(pingas.return_range())

pingas.upgrade_battery()
print(pingas.describe_battery())
print(pingas.return_range())

print(randint(1, 6))

players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        return randint(1, self.sides)
    

die1 = Die(20)
print(die1.roll_die())

lotery = ['c', 'z', 1, 5, 12, 26, 7, 'p', 14, 19, 'a', 28, 22,  'r', 3]
numbers = set()

while len(numbers) < 4:
    numbers.add(choice(lotery))

print(f"Here's the winner numbers: {numbers}")

my_ticket = {'z', 3, 'r', 26}
times = 0

while True:
    numbers = set()

    while len(numbers) < 4:
        numbers.add(choice(lotery))

    times += 1

    if numbers == my_ticket:
        break

print(times)
    