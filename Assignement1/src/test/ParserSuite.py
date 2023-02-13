import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_PS201(self):
        """Simple program: int main() {} """
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_PS202(self):
        input = """x: integer = 65;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_PS203(self):
        input = """ x: integer = 65;
                    fact: function integer (n: integer) {
                        if (n == 0) return 1;
                        else return n * fact(n - 1);
                    }
                    inc: function void(out n: integer, delta: integer) {
                        n = n + delta;
                    }
                    main: function void() {
                        delta: integer = fact(3);
                        inc(x, delta);
                        printInteger(x);
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
