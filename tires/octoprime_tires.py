from abc import ABC
from tire import Tires

class OctoprimeTires(Tires, ABC):
    def __init__(self, sensor_readings:list):
        super().__init__(sensor_readings)
    
    def needs_service(self):
        return sum(self.sensor_readings) >= 3