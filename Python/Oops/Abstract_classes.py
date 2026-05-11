from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass         #--> This means yeh funtion abhi kuch nahi karega 


class lion(Animal):
    def make_sound(self):
        print("Roar") 


li = lion()
lion.make_sound(li)