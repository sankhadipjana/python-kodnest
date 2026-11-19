from abc import abstractmethod, ABC

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car Starts")

    @abstractmethod
    def stop(self):
        pass

class SportCar(Car):
    def stop(self):
        print("Sport car stops")

# v = Vehicle()  # Cannot instantiate abstract class
sc = SportCar()
sc.start()
sc.stop()