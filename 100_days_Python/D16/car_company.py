class factory_preset:
    car = 'factory_preset'
    gears = 5
    engine = 1.5
    fuel = 'petrol'
    transmission = 'manual'
    seats = 'leather'

    def description(self):
        return f"{self.car} runs with {self.fuel} and contains {self.engine}hp engine with {self.transmission} transmission. This contains {self.seats} seats."


ford_car = factory_preset()
ford_car.car = 'Ford'
ford_car.seats = 'Custom Design'
ford_car.engine = 2.5

print(ford_car.description())