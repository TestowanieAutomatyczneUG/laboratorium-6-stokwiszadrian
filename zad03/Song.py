class Song:
    def __init__(self):
        self.parts = [
            "a Partridge in a Pear Tree.",
            "two Turtle Doves, and ",
            "three French Hens, ",
            "four Calling Birds, ",
            "five Gold Rings, ",
            "six Geese-a-Laying, ",
            "seven Swans-a-Swimming, ",
            "eight Maids-a-Milking, ",
            "nine Ladies Dancing, ",
            "ten Lords-a-Leaping, ",
            "eleven Pipers Piping, ",
            "twelve Drummers Drumming, "
            ]
        self.numerals = [
            "first",
            "second",
            "third",
            "fourth",
            "fifth",
            "sixth",
            "seventh",
            "eighth",
            "ninth",
            "tenth",
            "eleventh",
            "twelfth"
        ]

    def verse(self, n):
        if not isinstance(n, int):
            raise TypeError("Numer wersu musi być liczba całkowitą")

        if n > 12 or n < 1:
            raise ValueError("Dostepne sa tylko wersy o numerach 1-12")

        result = "On the "+self.numerals[n-1]+" day of Christmas my true love gave to me: "
        for i in range(n-1, -1, -1):
            result += self.parts[i]
        return result

    def range(self, a, b):
        if a > b:
            raise ValueError("1. argument musi byc mniejszy/rowny od 2.")
        else:
            result = ""
            if a == b:
                return self.verse(a)

            for i in range(a, b+1):
                result += self.verse(i)+"\n"
            return result

    def whole(self):
        return self.range(1, 12)


