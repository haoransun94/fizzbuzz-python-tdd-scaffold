import unittest


class FizzBuzz(object):
    @classmethod
    def read(cls, num):
        res = ""
        if num % 3 == 0:
            res += "Fizz"
        if num % 5 == 0:
            res += "Buzz"
        if res == "":
            return str(num)
        return res


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(FizzBuzz.read(1), "1")
        self.assertEqual(FizzBuzz.read(3), "Fizz")
        self.assertEqual(FizzBuzz.read(5), "Buzz")
        self.assertEqual(FizzBuzz.read(15), "FizzBuzz")


if __name__ == '__main__':
    unittest.main()
