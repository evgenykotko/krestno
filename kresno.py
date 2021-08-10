# -*- coding: utf-8 -*-
def create():
    pole = [["."]*3 for i in range(3)]
    return pole

def pole_reload(pole):
    print("\n" * 10)
    for i in range(len(pole)):
        for j in range(len(pole[i])):
            print(pole[i][j], end=' ')
        print()
    proverka_1(pole)
    proverka(pole)
    hod(pole)

def hod(pole):
    a, b, c = input("Введите координаты и символ: ").split()
    if 1 <= int(a) <= 3 and 1 <= int(b) <= 3:
        if pole[int(a) - 1][int(b) - 1] == ".":
            pole[int(a) - 1][int(b) - 1] = str(c)
        else:
            print("Квадрат занят, попробуйте другой")
            hod(pole)
    else:
        print("Координаты вне игрового поля, попробуйте еще раз")
        hod(pole)
    pole_reload(pole)

def proverka_1(pole):
    count = 0
    for i in range(len(pole)):
        for j in range(len(pole[i])):
            if pole[i][j] == ".":
                count += 1
    if count == 0:
        print("Ходы закончились")
        menu()


def proverka(pole):
    if pole[0][0] == pole[1][1] == pole[2][2] != ".":
        print("Победа!")
        menu()
    elif pole[0][2] == pole[1][1] == pole[2][0] != ".":
        print("Победа!")
        menu()
    elif pole[0][0] == pole[0][1] == pole[0][2] != ".":
        print("Победа!")
        menu()
    elif pole[1][0] == pole[1][1] == pole[1][2] != ".":
        print("Победа!")
        menu()
    elif pole[2][0] == pole[2][1] == pole[2][2] != ".":
        print("Победа!")
        menu()
    elif pole[0][0] == pole[1][0] == pole[2][0] != ".":
        print("Победа!")
        menu()
    elif pole[0][1] == pole[1][1] == pole[2][1] != ".":
        print("Победа!")
        menu()
    elif pole[0][2] == pole[1][2] == pole[2][2] != ".":
        print("Победа!")
        menu()
    else:
        hod(pole)

def menu():
    pole=create()
    if input("Хотите сыграть? (y / n): ") == "y":
        pole_reload(pole)
    else:
        print("Жаль, всего хорошего!")
        exit()

menu()