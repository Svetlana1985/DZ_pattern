from abc import ABC, abstractmethod
from itertools import product
from typing import Any
from typing import List

# Задача №1
class DigitalProduct(ABC):
    @abstractmethod
    def get_details(self)->str:
        pass
    @abstractmethod
    def download(self)->None:
        pass
    @abstractmethod
    def play(self)->None:
        pass

class Game(DigitalProduct):
    pass
class Music(DigitalProduct):
    pass

class ActionGame(Game):
    def get_details(self) ->str:
        return 'Action Game: Call of Duty'
    def download(self) ->None:
        print('Downloading Action Game...')
    def play(self) ->None:
        print('Starting Action Game...')

class PuzzleGame(Game):
    def get_details(self) ->str:
        return 'Puzzle Game: Minecraft'
    def download(self) ->None:
        print('Downloading Puzzle Game...')
    def play(self) ->None:
        print('Starting Puzzle Game...')

class RockMusic(Music):
    def get_details(self) ->str:
        return 'Rock Music: Scorpions - Still loving you'
    def download(self) ->None:
        print('Downloading Rock Music...')
    def play(self) ->None:
        print('Playback Rock Music')

class JazzMusic(Music):
    def get_details(self) ->str:
        return 'Jazz Music: Ray Charles - Hit the Road Jack'
    def download(self) ->None:
        print('Downloading Jazz Music...')
    def play(self) ->None:
        print('Playback Jazz Music')

class DigitalProductFactory(ABC):
    @abstractmethod
    def create_game(self)->Game:
        pass
    @abstractmethod
    def create_music(self)->Music:
        pass

class GameFactory(ABC):
    @abstractmethod
    def create_game(self)->Game:
        pass

class MusicFactory(ABC):
    @abstractmethod
    def create_music(self)->Music:
        pass

class ActionGameFactory(DigitalProductFactory):
    def create_game(self) ->ActionGame:
        return ActionGame()
    def create_music(self) ->None:
        return None

class PuzzleGameFactory(DigitalProductFactory):
    def create_game(self) ->PuzzleGame:
        return PuzzleGame()
    def create_music(self) ->None:
        return None

class RockMusicFactory(DigitalProductFactory):
    def create_game(self) ->None:
        return None
    def create_music(self) ->RockMusic:
        return RockMusic()

class JazzMusicFactory(DigitalProductFactory):
    def create_game(self) ->None:
        return None
    def create_music(self) ->JazzMusic:
        return JazzMusic()

class GenericGameFactory(GameFactory):
    def create_game(self, game_type:str)->Game:
        if game_type == 'action':
            return ActionGame()
        elif game_type == 'puzzle':
            return PuzzleGame()
        else:
            raise ValueError('Invalid game type')
class GenericMusicFactory(MusicFactory):
    def create_music(self, music_type:str)->Music:
        if music_type == 'rock':
            return RockMusic()
        elif music_type == 'jazz':
            return JazzMusic()
        else:
            raise ValueError('Invalid music type')

def show_product(factory:DigitalProductFactory, product_type:str)->None:
    if product_type == 'game':
        product = factory.create_game()
    elif product_type == 'music':
        product = factory.create_music()
    else:
        raise ValueError('Invalid product type')
    if product:
        print(product.get_details())
        product.download()
        product.play()

if __name__ == '__main__':
    action_game_factory = ActionGameFactory()
    puzzle_game_factory = PuzzleGameFactory()
    rock_music_factory = RockMusicFactory()
    jazz_music_factory = JazzMusicFactory()

    show_product(action_game_factory, 'game')
    print('Good luck to play')
    show_product(puzzle_game_factory, 'game')
    print('You are smart, i believe in you')
    show_product(rock_music_factory, 'music')
    print('Dont sleep tonight')
    show_product(jazz_music_factory, 'music')
    print('Relax and have a nice time')

    generic_game_factory = GenericGameFactory()
    generic_music_factory = GenericMusicFactory()

    action_game = generic_game_factory.create_game('action')
    puzzle_game = generic_game_factory.create_game('puzzle')
    rock_music = generic_music_factory.create_music('rock')
    jazz_music = generic_music_factory.create_music('jazz')

    print(f'Generic Action Game: {action_game.get_details()}')
    print(f'Generic Puzzle Game: {puzzle_game.get_details()}')
    print(f'Generic Rock Music: {rock_music.get_details()}')
    print(f'Generic Jazz Music: {jazz_music.get_details()}')

# Задача №2
class Pizza:
    def __init__(self):
        self.dough = None
        self.size = None
        self.sauce = None
        self.toppings: List[str] = []

    def display(self):
        print('Pizza Details: ')
        print(f'Dough: {self.dough}')
        print(f'Size: {self.size}')
        print(f'Sauce: {self.sauce}')
        print(f'Toppings: {" , ".join(self.toppings)}')

class Burger:
    def __init__(self):
        self.type_bun = None
        self.patty = None
        self.additions: List[str] = []

    def display(self):
        print('Burger Details: ')
        print(f'Type_bun: {self.type_bun}')
        print(f'Patty: {self.patty}')
        print(f'Additions: {" , ".join(self.additions)}')

class PizzaBuilder(ABC):
    @abstractmethod
    def set_dough(self, dough: str):
        pass

    @abstractmethod
    def set_size(self, size: str):
        pass

    @abstractmethod
    def set_sauce(self, sauce: str):
        pass

    @abstractmethod
    def add_topping(self, topping: str):
        pass

    @abstractmethod
    def get_pizza(self)-> Pizza:
        pass

class BurgerBuilder(ABC):
    @abstractmethod
    def set_type_bun(self, type_bun: str):
        pass

    @abstractmethod
    def set_patty(self, patty: str):
        pass

    @abstractmethod
    def add_addition(self, addition: str):
        pass

    @abstractmethod
    def get_burger(self)->Burger:
        pass

class ConcretePizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def set_dough(self, dough: str):
        self.pizza.dough = dough
        return self

    def set_size(self, size: str):
        self.pizza.size = size
        return self

    def set_sauce(self, sauce: str):
        self.pizza.sauce = sauce
        return self

    def add_topping(self, topping: str):
        self.pizza.toppings.append(topping)
        return self

    def get_pizza(self) -> Pizza:
        return self.pizza

class ConcreteBurgerBuilder(BurgerBuilder):
    def __init__(self):
        self.burger = Burger()

    def set_type_bun(self, type_bun: str):
        self.burger.type_bun = type_bun
        return self

    def set_patty(self, patty: str):
        self.burger.patty = patty
        return self

    def add_addition(self, addition: str):
        self.burger.additions.append(addition)
        return self

    def get_burger(self) -> Burger:
        return self.burger

class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def build_standard_pizza(self):
        if self.builder:
            self.builder.set_dough("Thin").set_size("Medium").set_sauce("Tomato").add_topping("Mozzarella").add_topping("Pepperoni")
            return self.builder
        else:
            raise ValueError("Builder is not set in Director")

    def build_standard_burger(self):
        if self.builder:
            self.builder.set_type_bun("Classic").set_patty("Beef").add_addition("Cheese").add_addition("Bacon")
            return self.builder
        else:
            raise ValueError("Builder is not set in Director")

if __name__ == '__main__':
    director = Director()

    pizza_builder = ConcretePizzaBuilder()
    director.set_builder(pizza_builder)
    standard_pizza_builder = director.build_standard_pizza()
    pizza1 = standard_pizza_builder.get_pizza()
    print("Standard Pizza:")
    pizza1.display()

    pizza_builder = ConcretePizzaBuilder()
    pizza2 = pizza_builder.set_dough("Thick").set_size("Large").set_sauce("Creamy").add_topping("Mushrooms").get_pizza()
    print("\nCustom Pizza:")
    pizza2.display()

    burger_builder = ConcreteBurgerBuilder()
    director.set_builder(burger_builder)
    standard_burger_builder = director.build_standard_burger()
    burger1 = standard_burger_builder.get_burger()
    print("\nStandard Burger:")
    burger1.display()

    burger_builder = ConcreteBurgerBuilder()
    burger2 = burger_builder.set_type_bun("Rye").set_patty("Chicken").add_addition("Lettuce").add_addition("Tomatoes").get_burger()
    print("\nCustom Burger:")
    burger2.display()



