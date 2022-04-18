from database import Database
from coffeeshop import CoffeeHouse
database_object = Database('localhost', 'root', '14481488Russia!', 'coffee_house_django')
coffeshop_object = CoffeeHouse(database_object)
coffeshop_object.run_coffee_shop()

