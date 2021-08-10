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
    while True:
        coord = input("Введите координаты: ").split()
        if len(coord) != 2:
            print("Введите 2 координата.")
            continue

        a, b = coord

        if not (a.isdigit()) or not (b.isdigit()):
            print("Введите числа!")
            continue
        a, b = int(a), int(b)
        if 1 > a > 3 and 1 > b > 3:
            print("Координаты вне игрового поля, попробуйте еще раз")
            continue

        if pole[a - 1][b - 1] != ".":
            print("Квадрат занят, попробуйте другой")
            continue
        return a, b
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