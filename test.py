import unittest


def myfunc():
    return False


a = 1
b = 2


class testtruth(unittest.TestCase):

    def test_myfunc(self):
        self.assertFalse(myfunc())

    def test(self):
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
