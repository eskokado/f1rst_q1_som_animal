from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Cat(Animal):
    id = 1

    def make_sound(self):
        return "Miau"

class Dog(Animal):
    id = 2

    def make_sound(self):
        return "Auau"

class AnimalSoundSingleton:
    _instance = None
    history = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AnimalSoundSingleton, cls).__new__(cls)
        return cls._instance

    def record_sound(self, animal):
        sound = animal.make_sound()
        self.history.append((type(animal).id, sound))
        return sound

    def get_history(self):
        return '\n'.join([' '.join(map(str, entry)) for entry in self.history])
