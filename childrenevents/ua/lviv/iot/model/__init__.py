import doctest

from childrenevents.ua.lviv.iot.model.children_event_option import ChildrenEventOption


class TestClass:

    def __init__(self, a = 2):
        self.a = a

    def pow(self, n):
        """
        >>> obj = TestClass(2)
        >>> obj.pow(3)
        8
        """
        print(self.a ** n)


if __name__ == '__main__':
    doctest.testmod(verbose=True, extraglobs={'obj': TestClass()})

