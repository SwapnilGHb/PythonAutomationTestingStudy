from abc import ABC, abstractmethod

class Gearbox(ABC):
    @abstractmethod
    def set_gear(self):
        pass

class Engine(Gearbox):
    @abstractmethod
    def start(self):
        super().set_gear()
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Engine):
    def start(self):
        print("Starting")

    def stop(self):
        print("Stopping")

    def set_gear(self):
        print("Gearbox is ready.")


    def drive(self):
        self.start()
        self.stop()

car_obj = Car()
car_obj.drive()