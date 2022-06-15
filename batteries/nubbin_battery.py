from abc import ABC
from datetime import datetime
from battery import Battery

class NubbinBattery(Battery, ABC):
     def __init__(self, last_service_date: datetime, current_date: datetime):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
     def needs_service(self)->bool:
        self.current_date = datetime.today().date()
        return self.current_date > self.last_service_date + 4
            