from abc import ABC, abstractmethod

class Servicable(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def needs_service(self) -> bool:
        pass
