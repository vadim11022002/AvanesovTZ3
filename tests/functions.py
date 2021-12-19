import sys

def minimalNumber(spisok):
    minimal = spisok[0]
    for i in range(len(spisok)):
        if spisok[i] < minimal:
            minimal = spisok[i]
    return minimal

def maximalNumber(spisok):
    maximal = spisok[0]
    for i in range(len(spisok)):
        if spisok[i] > maximal:
            maximal = spisok[i]
    return maximal

def summaNumbers(spisok):
    summa = 0
    for i in spisok:
        summa = summa + i
    return summa

def proizvNumbers(spisok):
    proizv = 1
    for i in spisok:
        proizv *= i
    return proizv

def main_func(file):
    with open(file, "r") as file:
        spisokChisel = file.read()
        spisokChisel_int = spisokChisel.split(",")
    for i in range(len(spisokChisel_int)):
        spisokChisel_int[i] = int(spisokChisel_int[i])
    minimal = minimalNumber(spisokChisel_int)
    maximal = maximalNumber(spisokChisel_int)
    summa = summaNumbers(spisokChisel_int)
    try:
        minimalNumber(spisokChisel_int)
    except ArithmeticError:
        print("Ошибка переполнения")
        sys.exit(1)
    else:
        proizvedenie = proizvNumbers(spisokChisel_int)
    return maximal, minimal, summa, proizvedenie