class Vehicle:
    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed

    def get_name(self) -> str:
        return f'The vehicle name {self.name}'
    
    def get_speed(self) -> str:
        return f'The vehicle speed {self.speed}'


class VehicleWithEngine(Vehicle):
    def engine(self):
        pass

    def start_engine(self):
        self.engine()


class VehicleWithoutEngine(Vehicle):
    def start_moving(self):
        pass


class Bicycle(VehicleWithoutEngine):
    def start_engine(self):
        pass


class Car(VehicleWithEngine):
    def start_engine(self):
        pass
