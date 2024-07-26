from typing import List
class Perc:
    name = None
    order: int = None

    def __str__(self):
        return f'{self.order}. {self.name}'

    def __repr__(self):
        return f'{self.order}. {self.name}'

class Healing(Perc):
    name = 'Исцеление'
    order: int = 1


class FireBall(Perc):
    name = 'Огненный шар'
    order: int = 2


class Stels_step(Perc):
    name = 'Скртытая ходьба'
    order: int = 3


class stels_hit(Perc):
    name = 'Удар со спины'
    order: int = 4


class Strong_hit(Perc):
    name = 'Сильный замах'
    order: int = 5


class Storm(Perc):
    name = 'Ураган'
    order: int = 6


class Levitation(Perc):
    name = 'Левитация'
    order: int = 7


class Water_walk(Perc):
    name = 'Хождение по воде'
    order: int = 8


class Smoke(Perc):
    name = 'Дымовая завеса'
    order: int = 9


class Rooth_hit(Perc):
    name = 'Удар с крыши'
    order: int = 10


class poison_blade(Perc):
    name = 'Ядовитый клинок'
    order: int = 11


class deadly_poison(Perc):
    name = 'Смертельный яд'
    order: int = 12


class Eskalibur(Perc):
    name = 'Эскалибур'
    order: int = 13


class Better_armor(Perc):
    name = 'Улучшеная броня'
    order: int = 14


class Shield(Perc):
    name = 'Щит'
    order: int = 15


class Char:

    available_perks = []

    def __init__(self):
        self.perks = list()


class Mage(Char):
    available_perks = [Healing(), FireBall()]


class Asasin(Char):
    available_perks = [stels_hit(),Stels_step()]


class Sword(Char):
    available_perks = [Storm(),Strong_hit()]


# if __name__ == '__main__':
#     my_char = Mage()
#
#     for p in my_char.available_perks:
#         print(p)
#
#     prc = input('Выбери перк:')
#
#     perc = None
#
#
#     for p in my_char.available_perks:
#         if prc == str(p.order) or prc == p.name:
#             my_char.perks.append(p)
#             break
#
#     print(my_char.perks)