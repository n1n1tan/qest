def q1(clas, a):
    print("Задание №1: Зачистить северную пещеру от гоблинов.")
    print("Требуемые статы: Сила > 70")
    print("хотите взять задание?")
    ans1 = input()
    if ans1 == "Да":
        if clas == "Мечник":
            print("Вы выполнили квест")
        else:
            print("Вы провалили квест")
    else:
        a = 2

    return a
def q2(clas, a):
    print("Задание №2: Убить главу мафии.")
    print("Требуемые статы: Ловкость > 50")
    print("хотите взять задание?")
    ans1 = input()
    if ans1 == "Да":
        if clas == "Асасин":
            print("Вы выполнили квест")
        else:
            print("Вы провалили квест")
    else:
        a = 3

    return a


def q3(clas,a):
    print("Задание №3: Вылечить раненых в деревне.")
    print("Требуемый навык: Исцеление")
    print("хотите взять задание?")
    ans1 = input()
    if ans1 == "Да":
        if clas == "Маг":
            print("Вы выполнили квест")
        else:
            print("Вы провалили квест")
    else:
        a = 1
    return a