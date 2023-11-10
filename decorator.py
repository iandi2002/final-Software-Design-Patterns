from abc import ABC, abstractmethod

class ClothingDecorator(ABC):
    @abstractmethod
    def get_clothing_list(self):
        pass
