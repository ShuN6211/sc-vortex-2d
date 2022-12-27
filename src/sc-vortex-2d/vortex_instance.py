from abc import ABC, abstractmethod

class VortexInstance(ABC):
    
    @abstractmethod
    def get(self) -> None:
        pass


