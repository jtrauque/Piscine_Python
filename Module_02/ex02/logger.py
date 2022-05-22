import time
from random import randint
import os
import logging


def log(function):
    def printer(self, water_level=None):
        start = time.time()
        if not water_level:
            ret = function(self)
        else:
            ret = function(self, water_level)
        end = time.time() - start
        if end <= 1:
            end *= 1000
        name = os.environ['USER']
        Log_Format = ""
        logging.basicConfig(filename="console.log", filemode="w",
                            format=Log_Format, level=logging.INFO)
        logging.info(f"({name})Running: {function.__name__.capitalize(): <19}\
            [ exec-time = {end:.3f} {'ms' if end < 1 else 's'} ]")
        return ret
    return printer


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
