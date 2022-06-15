from abc import ABC, abstractclassmethod


class Engine(ABC):
    def __init__():
        pass
    
    @abstractclassmethod
    def needs_service() -> bool:
        pass