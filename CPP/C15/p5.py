# this is a sub class for abstract car class
from p3 import Car


class Santro(Car):
    def steering(self):
        print('Santro uses power steering.')
        print('Drive the car.')

    def braking(self):
        print('Santro uses gas brakes.')
        print('Apply brakes and stop it.')


# Create object Santro and use its features.
s = Santro(7878)
s.openTank()
s.steering()
s.braking()