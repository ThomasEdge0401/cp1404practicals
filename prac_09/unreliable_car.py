from car import Car
from random import randint

class UnreliableCar(Car):
    """specialised car that might not drive depending on reliability"""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        number = randint(0, 100)
        if number < self.reliability:
            return super().drive(distance)
        return 0
