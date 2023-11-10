

from abc import ABC, abstractmethod

class ClothingStrategy(ABC):
    @abstractmethod
    def get_clothing_list(self):
        pass

class WomenClothing(ClothingStrategy):
    def get_clothing_list(self):
        return [("Jeans", 50), ("Blouse", 30)]

class MenClothing(ClothingStrategy):
    def get_clothing_list(self):
        return [("Trousers", 70), ("Shirt", 40)]

class KidsClothing(ClothingStrategy):
    def get_clothing_list(self):
        return [("Boots", 60), ("Cap", 15)]

class SportClothing(ClothingStrategy):
    def get_clothing_list(self):
        return [("Running Shoes", 80), ("Sport T-shirt", 35)]
