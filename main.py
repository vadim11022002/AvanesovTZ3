import sys
from tests.functions import maximalNumber, minimalNumber, proizvNumbers, summaNumbers


with open('1.txt', "r") as file:
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
