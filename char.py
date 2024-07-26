from clases import*
from quests import*
from classes2 import*


print("Доступные классы: Маг, Асасин, Мечник")
name, age, hight, clas = map(str, input("Введи имя, возраст, рост и класс:").split())
print("Персонаж создан:" f'{name=}, {age=}, {hight=}, {clas=}')
if clas == "Маг" and int(age) > 50:
    print("Вы выбрали класс - ", clas)
    print(mag())
    my_char = Mage()
if clas == "Маг" and int(age) < 50:
    print("Ваш возраст не позволяет стать магом")

if clas == "Асасин":
    print("Вы выбрали класс - ", clas)
    print(asasin())
    my_char = Asasin()

if clas == "Мечник" and int(hight) > 165:
    print("Вы выбрали класс - ", clas)
    print(sword())
    my_char = Sword()

if clas == "Мечник" and int(hight) < 165:
    print("Ваш рост не позволяет стать мечником")


print("Вы появились в гильдии, возьмите задание на доске")
print("на доске 3 задания какое хотите посмотреть?")
a = int(input())
if a == 1:
    a = q1(clas,a)
if a == 2:
    a = q2(clas,a)
if a == 3:
    a = q3(clas,a)