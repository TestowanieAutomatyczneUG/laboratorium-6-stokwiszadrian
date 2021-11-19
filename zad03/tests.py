import unittest
from Song import Song


class RomanNumeralsTest(unittest.TestCase):
    def setUp(self):
        self.song = Song()

    def test_first(self):
        self.assertEqual(self.song.verse(1), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")

    def test_second(self):
        self.assertEqual(self.song.verse(2), "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_third(self):
        self.assertEqual(self.song.verse(3), "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_fourth(self):
        self.assertEqual(self.song.verse(4), "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_fifth(self):
        self.assertEqual(self.song.verse(5), "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_sixth(self):
        self.assertEqual(self.song.verse(6), "On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_seventh(self):
        self.assertEqual(self.song.verse(7), "On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_eighth(self):
        self.assertEqual(self.song.verse(8), "On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_ninth(self):
        self.assertEqual(self.song.verse(9), "On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_tenth(self):
        self.assertEqual(self.song.verse(10), "On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_eleventh(self):
        self.assertEqual(self.song.verse(11), "On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_twelfth(self):
        self.assertEqual(self.song.verse(12), "On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_verse_wrongtype_string(self):
        self.assertRaises(TypeError, self.song.verse, "3")

    def test_verse_wrongtype_float(self):
        self.assertRaises(TypeError, self.song.verse, 2.0)

    def test_verse_wrongtype_list(self):
        self.assertRaises(TypeError, self.song.verse, [5])

    def test_verse_wrongrange1(self):
        self.assertRaises(ValueError, self.song.verse, -1)

    def test_verse_wrongrange2(self):
        self.assertRaises(ValueError, self.song.verse, 20)

    def test_range_1_1(self):
        self.assertEqual(self.song.range(1, 1), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")

    def test_range_2_4(self):
        self.assertEqual(self.song.range(2, 4), "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.\nOn the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\nOn the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n")

    def test_range_equlals_verse(self):
        self.assertEqual(self.song.range(2, 2), self.song.verse(2))

    def test_range_reversed(self):
        self.assertRaises(ValueError, self.song.range, 6, 3)

    def test_range_wrongtype_string1(self):
        self.assertRaises(TypeError, self.song.range, "3", 6)

    def test_range_wrongtype_string2(self):
        self.assertRaises(TypeError, self.song.range, 3, "5")

    def test_range_wrongtype_list(self):
        self.assertRaises(TypeError, self.song.range, [3, 12])

    def test_range_wrongrange1(self):
        self.assertRaises(ValueError, self.song.range, -2, 6)

    def test_range_wrongrange2(self):
        self.assertRaises(ValueError, self.song.range, 4, 30)


    def test_whole(self):
        self.assertEqual(self.song.whole(), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.\nOn the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.\nOn the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\nOn the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\nOn the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\nOn the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\nOn the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\nOn the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\nOn the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\nOn the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\nOn the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\nOn the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n")

    def tearDown(self):
        self.song = None
