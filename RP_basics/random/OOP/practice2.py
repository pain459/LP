# Apartment data
class Apartment:
    floor = 1
    maid = 1
    security = 1
    vehicle = 1
    kids = 0
    pets = 0
    own_flat = "No"

    def __init__(self, name, total_people, flat_no):
        self.name = name
        self.total_people = total_people
        self.flat_no = flat_no

    def pets_status(self):
        if self.pets == 0:
            return f"{self.name} doesn't have pets."
        else:
            return f"{self.name} have pets"


ravi = Apartment("Ravi", 2, 304)
raju = Apartment("Raju", 3, 404)
brave = Apartment("Brave", 1, 305)

ravi.floor = 3
ravi.own_flat = "No"
raju.floor = 4
raju.maid = 0
raju.kids = 2
raju.total_people = 4
raju.vehicle = 0

print(ravi.pets_status())

