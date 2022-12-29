class Time(object):
    def __init__(self, hour=0, minute=0, seconds=0):
        self.__hour = hour
        self.__minute = minute
        self.__seconds = seconds

    def __repr__(self):
        return 'Class Time: {:02d}:{:02d}:{:02d}'.format(self.__hour,
                                                         self.__minute,
                                                         self.__seconds)

    def __str__(self):
        return '{:02d}:{:02d}:{:02d}'.format(self.__hour,
                                             self.__minute,
                                             self.__seconds)

    def from_str(self, string):
        hour, minute, seconds = string.split(':')
        self.__hour = int(hour)
        self.__minute = int(minute)
        self.__seconds = int(seconds)


def main():
    A = Time(12, 25, 30)

    print(A)
    print(repr(A))
    print(str(A))
    print()

    B = Time(2, 25, 3)

    print(B)
    print(repr(B))
    print(str(B))
    print()

    C = Time(2, 25)

    print(C)
    print(repr(C))
    print(str(C))
    print()

    D = Time()

    print(D)
    print(repr(D))
    print(str(D))
    print()

    D.from_str("03:09:19")

    print(D)
    print(repr(D))
    print(str(D))


if __name__ == "__main__":
    main()
