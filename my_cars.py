from car import Car
from eletric_car import EletricCar as EC
import eletric_car as ec

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = EC('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

my_leaf1 = ec.EletricCar('nissan', 'leaf', 2024)
print(my_leaf1.get_descriptive_name())