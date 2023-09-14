"""
Функции, которые 'используют базовый тип', должны иметь возможность
'использовать подтипы' базового типа, не зная об этом.
"""

# Допустим у нас есть класс транспортного средства
# Плохой пример
class Vehicle:
    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed

    def get_name(self) -> str:
        return f"The vehicle name {self.name}"
    
    def get_speed(self) -> str:
        return f"The vehicle speed {self.speed}"
    
    def engine(self):
        pass

    def start_engine(self):
        self.engine()
    

class Car:
    def start_engine(self):
        pass


class Bicycle(Vehicle):
    def start_engine(self):
        pass


# Пример хороший
class Vehicle:
    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed

    def get_name(self) -> str:
        return f"The vehicle name {self.name}"
    
    def get_speed(self) -> str:
        return f"The vehicle speed {self.speed}"
    

class VehicleWithoutEngine(Vehicle):
    def start_moving(self):
        raise NotImplemented
    

class VehicleWithEngine(Vehicle):
    def engine(self):
        pass

    def start_engine(self):
        self.engine()


class Car(VehicleWithEngine):
    def start_engine(self):
        pass


class Bicycle(VehicleWithoutEngine):
    def start_engine(self):
        pass
    