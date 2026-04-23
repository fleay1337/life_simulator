"""Точка входа в симулятор."""
from ecosystem import Ecosystem
from organism import Herbivore, Predator

def main():
    # Создаем мир
    world = Ecosystem()

    # Заселяем мир
    rabbit = Herbivore("Заяц", 20.0)
    deer = Herbivore("Олень", 30.0)
    wolf = Predator("Волк", 40.0)

    world.add_organism(rabbit)
    world.add_organism(deer)
    world.add_organism(wolf)

    # Симуляция на 3 хода
    for turn in range(1, 4):
        print(f"\n===== ХОД {turn} =====")
        world.update()
        world.status()

if __name__ == "__main__":
    main()