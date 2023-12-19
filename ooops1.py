
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False
    def start(self):
        if not self.is_running:
            print(f"The {self.year} {self.make} {self.model} is now running.")
            self.is_running = True
        else:
            print("The car is already running.")
    def stop(self):
        if self.is_running:
            print(f"The {self.year} {self.make} {self.model} has been stopped.")
            self.is_running = False
        else:
            print("The car is already stopped.")

my_car = Car(make="Toyota", model="Camry", year=2020)

print(f"My car is a {my_car.year} {my_car.make} {my_car.model}.")
my_car.start()
my_car.stop()

