"""
from car import Car, EletricCar

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = EletricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
"""

# agora importando car inteiro ao invés de módulo por módulo

import car

my_mustang = car.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = car.EletricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())