def file_opening(file):
    with open(file, "r") as file:
        spisokChisel = file.read()
        spisokChisel_int = spisokChisel.split(",")
    for i in range(len(spisokChisel_int)):
        spisokChisel_int[i] = int(spisokChisel_int[i])
    return spisokChisel_int

def test_file_one():
    assert file_opening("tests/1.txt") == [1,2,3,3,4,5,22,1,5,6]

def test_file_one():
    assert file_opening("tests/2.txt") == [5,5,5,5,525,65,1,2,3,4]