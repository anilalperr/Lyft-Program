from abc import ABC
from tire import Tires

class CarriganTires(Tires, ABC):
    def __init__(self, sensor_readings:list):
        super().__init__(sensor_readings)
    
    def needs_service(self):
        for i in range(len(self.sensor_readings)):
            if self.sensor_readings[i] >= 0.9:
                return True
        return False
