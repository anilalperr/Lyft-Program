from car import Car
from datetime import datetime
from spindler_battery import SpindlerBattery
from nubbin_battery import NubbinBattery
from capulet_engine import CapuletEngine
from willoughby_engine import WilloughbyEngine
from sternman_engine import SternmanEngine

class CarFactory():
    def __init__(self):
        pass
    def  create_calliope(self, current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        battery = SpindlerBattery(last_service_date, current_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)
    
    def  create_glissade(self, current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        battery = SpindlerBattery(last_service_date, current_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)
    
    def  create_palindrome(self, current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        battery = SpindlerBattery(last_service_date, current_date)
        engine = SternmanEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)
    
    def  create_rorschach(self, current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        battery = NubbinBattery(last_service_date, current_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)
    
    def  create_thovex(self, current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        battery = NubbinBattery(last_service_date, current_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)