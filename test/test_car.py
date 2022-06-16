import unittest
from datetime import datetime

from batteries.spindler_battery import SpindlerBattery
from batteries.nubbin_battery import NubbinBattery
from engines.capulet_engine import CapuletEngine
from engines.willoughby_engine import WilloughbyEngine
from engines.sternman_engine import SternmanEngine
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class TestCapuletEngine(unittest.TestCase):
    def test_capulet_needs_service(self):
        last_service_mileage = 0
        current_mileage = 30001
        
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet_engine.needs_service())
        
        
    def test_capulet_does_not_need_service(self):
        last_service_mileage = 0
        current_mileage = 20000
        
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(capulet_engine.needs_service())
        
class TestWilloughByEngine(unittest.TestCase):
    def test_willloughby_needs_service(self):
        last_service_mileage = 0
        current_mileage = 60001
        
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughby_engine.needs_service())
        
        
    def test_willoughby_does_not_need_service(self):
        last_service_mileage = 0
        current_mileage = 15000
        
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughby_engine.needs_service())
    
class TestSternmanEngine(unittest.TestCase):
    def test_sternman_needs_service(self):
        warning_light_is_on = True
        
        sternman_engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(sternman_engine.needs_service())
    
    def test_sternman_does_not_need_service(self):
        warning_light_is_on = False
        
        sternman_engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(sternman_engine.needs_service())
    
class TestSpindlerBattery(unittest.TestCase):
    def test_spindler_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        
        spindler_battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(spindler_battery.needs_service())
    
    def test_spindler_does_not_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        
        spindler_battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(spindler_battery.needs_service())
    
class TestNubbinBattery(unittest.TestCase):
    def test_nubbin_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        
        nubbin_battery = NubbinBattery(last_service_date, today)
        self.assertTrue(nubbin_battery.needs_service())
    
    def test_nubbin_does_not_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        
        nubbin_battery = NubbinBattery(last_service_date, today)
        self.assertFalse(nubbin_battery.needs_service())

class TestCarriganTires(unittest.TestCase):
    def test_carrigan_needs_service(self):
        carrigan_tires1 = CarriganTires([0, 0.1, 0.2, 0.9])
        self.assertTrue(carrigan_tires1.needs_service())
        
        carrigan_tires2 = CarriganTires([0, 0.1, 1, 0.9])
        self.assertTrue(carrigan_tires2.needs_service())
        
        carrigan_tires3 = CarriganTires([0, 0.95, 1, 0.9])
        self.assertTrue(carrigan_tires3.needs_service())
        
        carrigan_tires4 = CarriganTires([0.9, 0.95, 1, 0.9])
        self.assertTrue(carrigan_tires4.needs_service())
    
    def test_carrigan_does_not_need_service(self):
        carrigan_tires = CarriganTires([0,0.5,0.89,0.4])
        self.assertFalse(carrigan_tires.needs_service())
        

class TestOctoprimeTires(unittest.TestCase):
    def test_octoprime_needs_service(self):
        octoprime_tires1 = OctoprimeTires([0.2, 1, 0.9, 0.9])
        self.assertTrue(octoprime_tires1.needs_service())
        
        octoprime_tires2 = OctoprimeTires([1, 1, 1, 1])
        self.assertTrue(octoprime_tires2.needs_service())
    
    def test_octoprime_does_not_need_service(self):
        octoprime_tires1 = OctoprimeTires([0.19, 1, 0.9, 0.9])
        self.assertFalse(octoprime_tires1.needs_service())
        
        octoprime_tires2 = OctoprimeTires([0, 0.1, 0.5, 0.2])
        self.assertFalse(octoprime_tires2.needs_service())


if __name__ == '__main__':
    unittest.main()
