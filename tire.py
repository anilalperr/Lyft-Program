from abc import ABC, abstractclassmethod


class Tires(ABC):
    def __init__(self, sensor_readings:list):
        if len(sensor_readings) != 4:
            raise Exception("The new tire sensors return exactly 4 sensor readings")
            
        for i in range(len(sensor_readings)):
            if sensor_readings[i] > 1 or sensor_readings[i] < 0:
                raise Exception("Sensor readings should be between 0 and 1 (inclusive)")
        self.sensor_readings = sensor_readings
    
    @abstractclassmethod
    def needs_service() -> bool:
        pass