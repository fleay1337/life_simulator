"""Модуль управления экосистемой."""
from organism import Organism, Herbivore, Predator

class Ecosystem:
    """Класс, моделирующий среду обитания."""
    def __init__(self):
        self.population = []

    def add_organism(self, org: Organism):
        """Добавление организма в симуляцию."""
        self.population.append(org)
        print(f"✅ В экосистему добавлен: {org.name}")

    def update(self):
        """Один цикл (день) жизни экосистемы."""
        if not self.population:
            print("Экосистема пуста.")
            return

        print("\n--- События дня ---")
        for org in self.population[:]:
            if not org.is_alive():
                continue

            # Логика поведения в зависимости от типа
            if isinstance(org, Herbivore):
                org.move()
                org.eat_grass()
            
            elif isinstance(org, Predator):
                # Хищник ищет жертву среди всех в популяции
                potential_targets = [o for o in self.population if o != org and o.is_alive()]
                if potential_targets:
                    org.hunt(potential_targets[0])
                else:
                    org.energy -= 10  # Трата энергии на безуспешные поиски
                    print(f"🥀 {org.name} не нашел добычу и проголодался.")

        # Очистка экосистемы от погибших
        self.cleanup()

    def cleanup(self):
        """Удаление мертвых организмов из списка."""
        dead_count = 0
        for org in self.population[:]:
            if not org.is_alive():
                print(f"💀 {org.name} удален из системы.")
                self.population.remove(org)
                dead_count += 1
        
        if dead_count == 0:
            print("Сегодня никто не погиб.")

    def status(self):
        """Вывод текущего состояния популяции."""
        print("\nТекущее состояние:")
        for org in self.population:
            print(org)