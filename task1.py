# task1
import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str):
        self.make: str = make
        self.model: str = model

    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str):
        self.make: str = make
        self.model: str = model

    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, f"{model} (US Spec)")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, f"{model} (US Spec)")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, f"{model} (EU Spec)")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, f"{model} (EU Spec)")


us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

custom_us_car = us_factory.create_car("Ford", "Mustang")
custom_us_bike = us_factory.create_motorcycle("Harley", "Star")
custom_eu_bike = eu_factory.create_motorcycle("Ducati", "Monster")

custom_us_car.start_engine()
custom_us_bike.start_engine()
custom_eu_bike.start_engine()
