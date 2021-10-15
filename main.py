"""Основной модуль программы."""
import random

subjects = ('monster', 'apple', 'sword')
monster_counter = 0


class Hero:
    """Класс описывает рыцаря."""

    def __init__(self) -> None:
        """Инициализация героя."""
        self.hp = random.randint(10, 100)
        self.attack = random.randint(10, 50)

    def get_damage(self, down_health: int) -> None:
        """Получение урона."""
        self.hp = self.hp - down_health

    def get_health(self, up_health: int) -> None:
        """Получение ХП."""
        self.hp = self.hp + up_health


class Monster:
    """Класс описывает монстра."""

    def __init__(self) -> None:
        """Инициализация монстра."""
        self.hp = random.randint(10, 50)
        self.attack = random.randint(10, 100)

    def get_damage(self, down_health: int) -> None:
        """Получение урона."""
        self.hp = self.hp - down_health


class Apple:
    """Класс описывает яблоко."""

    def __init__(self) -> None:
        """Инициализация яблока."""
        self.hp = random.randint(0, 20)


class Sword:
    """Класс описывает мечь."""

    def __init__(self) -> None:
        """Инициализация меча."""
        self.attack = random.randint(50, 100)


def input_ch() -> str:
    """Функция обрабатывает ввод.

    :return: choice
    """
    choice = ""
    while choice != '1' and choice != '2':
        if choice != "":
            print('Ошибка ввода. введите 1 или 2:')
        choice = input()
    return choice


def game() -> None:
    """Основная функция игры."""
    global monster_counter
    hero = Hero()
    print(f'Родился новый Герой с {hero.hp} hp и силой {hero.attack}')
    death = False
    while monster_counter < 10:
        event = subjects[random.randint(0, 2)]
        if event == 'apple':
            apl = Apple()
            print(f'Герой встретил Яблоко с {apl.hp} hp ')
            hero.get_health(apl.hp)
            print(f'Теперь у Героя стало {hero.hp} hp ')
        if event == 'monster':
            mns = Monster()
            print(f'БОЙ Герой встретил Монстра с {mns.hp} hp и силой {mns.attack} ')
            print('Введите 1 если хотите Атаковать, либо 2 если Бежать:')
            choice = input_ch()
            if choice == '1':
                print('>>>>>>>>>>>>>>>>>>>>>>Начинается бой<<<<<<<<<<<<<<<<<<<<')
                print(f'Герой наносит урон {hero.attack}')
                mns.get_damage(hero.attack)
                if mns.hp > 0:
                    print(f'У Монстра осталось {mns.hp} hp')
                else:
                    monster_counter += 1
                    print(f'Повержен Монстр №{monster_counter}')
                print(f'Монстр наносит урон {mns.attack}')
                hero.get_damage(mns.attack)
                if hero.hp > 0:
                    print(f'У Героя осталось {hero.hp} hp')
                else:
                    print('Герой убит((((((')
                    death = True
                    break
            elif choice == '2':
                print('>>>>>>>>>>>>>Герой убегает<<<<<<<<<<<<')
        if event == 'sword':
            sw = Sword()
            print(f'Герой встретил МЕЧ силой {sw.attack} ')
            print('Введите 1 если хотите Взять выбросив старый, либо 2 если пройти мимо:')
            choice = input_ch()
            if choice == '1':
                hero.attack = sw.attack
                print(f'Теперь сила Героя {hero.attack}')
            elif choice == '2':
                print('Сила героя осталась прежней')
    if monster_counter < 10 or death:
        print(f'Герой убил {monster_counter} монстров и это ПОРАЖЕНИЕ')
    else:
        print(f'Герой убил {monster_counter} монстров и это ПОБЕДА')


game()
