# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math as m


class Dog:
    def __init__(self):
        self.__name = "joe"

    def getName(self):
        return self.__name

    @staticmethod
    def test():
        return "df"


def print_hi(name):
    cao = Dog()
    print(cao.getName())
    print(name)
    print(cao.test())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm'.__len__())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
