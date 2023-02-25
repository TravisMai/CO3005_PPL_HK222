import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_PS201(self):
        """Simple program: int main() {} """
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_PS202(self):
        input = """x,y,t: integer = 65, 97, 87;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_PS203(self):
        input = """ x: integer = 43;
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

    def test_PS204(self):
        input = """a, b, c, d: integer = 3, 5, 4;"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_PS205(self):
        input = """a, b: integer = 3, 5, 4;"""
        expect = "Error on line 1 col 20: ,"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_PS206(self):
        input = """ x: integer = 43;
                    fact: function integer (n: integer) {
                        if (n == 0) return 1;
                        else return n * fact(n - 1);
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_PS207(self):
        input = """ inc: function void(out n: integer, delta: integer) {
                        n = n + delta;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_PS208(self):
        input = """ main: function void() {
                        delta: integer = fact(3);
                        inc(x, delta);
                        printInteger(x);
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_PS209(self):
        input = """ /* A C-style comment */
                    a: integer = 5; // A C++ style comment"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_PS210(self):
        input = """a: = 5; // A C++ style comment"""
        expect = "Error on line 1 col 3: ="
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_PS211(self):
        input = """a: interger = 5; // A C++ style comment"""
        expect = "Error on line 1 col 3: interger"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_PS212(self):
        input = """a: void = 5; // A C++ style comment"""
        expect = "Error on line 1 col 3: void"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_PS213(self):
        input = """a: interger = 5; // A C++ style comment"""
        expect = "Error on line 1 col 3: interger"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_PS214(self):
        input = """// A C++ style comment"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_PS215(self):
        input = """A C++ style comment"""
        expect = "Error on line 1 col 2: C"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_PS216(self):
        input = """/* A C++ style comment */"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_PS217(self):
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_PS218(self):
        input = """ x: integer;
                    fact: function integer (n: integer) {
                        if (n == 0) x = 1;
                        else x = 0;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_PS219(self):
        input = """ x:integer=90;
                    if(x>=5) return 1;
                    else return 0;
                """
        expect = "Error on line 2 col 20: if"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_PS220(self):
        input = """
                main: function void()
                {
                    r, s: integer;
                    r = 2.0;
                    b: float = 6.5;
                    a: array[5] of string;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_PS221(self):
        input = """hehe: function void ( inherit out x : float, out lmeo: integer) inherit fact {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_PS222(self):
        input = """+"""
        expect = "Error on line 1 col 0: +"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_PS223(self):
        input = """main: function void () {x:auto = 5;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_PS224(self):
        input = """ main: function void () {
                        if(x<y && y < 9 && z != "lmeo") z = "hehe lmeo";
                        else z = "hehe ko lmeo";
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_PS225(self):
        input = """ getArea: function float() {}
                    Geometry: function void(length : float, alo: integer, str: string){}
                    main: function void () {}
                    Example: function void () inherit ABC {
                        length,width : float;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_PS226(self):
        input = """ a: integer = 5;
                    main: function void () {
                        while (z <= a) {
                            z = z + 1;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_PS227(self):
        input = """ a: integer = 5;
                    main: function void () {
                        for (i = 1, i < a, i + 1) {
                            writeInt(i);
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_PS228(self):
        input = """ a: integer = 5;
                    main: function void () {
                        do {
                            a = a + 1;
                        } while (a < 10);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_PS229(self):
        input = """ a: integer = 5;
                    main: function void () {
                        do {
                            a = a + 1
                        } while (a < 10);
                    }
                """
        expect = "Error on line 5 col 24: }"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_PS230(self):
        input = """ a: integer = 5;
                    main: function void () {
                        for (i = 1, i < a, i + 1) {
                            if (i % 2 == 0){
                                result: integer = 2 + 3 * 4 / (5 - 1);
                            }
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_PS231(self):
        input = """ a: integer = 5;
                    main: function void () {
                        for (i = 1, i < a, i + 1) {
                            if (i % 2 == 0){
                                arr: array[3,5] of integer;
                                break;
                            }
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_PS232(self):
        input = """ a: integer = 5;
                    main: function void () {
                        for (i = 1, i < a, i + 1) {
                            if (i % 2 == 0){
                                arr: array[3,5] of integer;
                                break;
                            }
                        }
                        for (i = 1, i < a, i + 1) {
                            for (j = i, j < a, j + 1) {
                                if (j % 2 == 0){
                                    arr[3,1] = 3;
                                    break;
                                }
                            }
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_PS233(self):
        input = """ a: integer = 5;
                    main: function void () {
                        for (i = 1, i < a, i + 1) {
                            if (i % 2 == 0){
                                arr: array[3,5] of integer;
                                break;
                            }
                        }
                        for (i = 1, i < a, i + 1) {
                            for (j = i, j < a, j + 1) {
                                if (j % 2 == 0){
                                    result: integer = 2 + 3 * 4 / (5 - 1);
                                    break;
                                }
                            }
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_PS234(self):
        input = """
                    WAP: function void (a: integer, b: integer, c: integer, d: string, e: boolean) {
                        a = 0;
                        b = 0;
                        for (a = 5, a <= 10, a + 1){
                            for (b = 15, b >= 1, b - 1){
                                for (c = 0, c >= -10, c - 1){
                                    if (c == 0){
                                        if (d == ""){
                                            if (e==false){
                                                d = d :: "abc";
                                            }
                                        }
                                    }
                        } 
                            
                    }
                """
        expect = "Error on line 18 col 16: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_PS235(self):
        input = """ mna: function void (a: integer, b: integer, c: integer, d: string, e: boolean) {
                        a = 0;
                        b = 0;
                        for (a = 5, a <= 10, a + 1){
                            for (b = 15, b >= 1, b - 1){
                                for (c = 0, c >= -10, c - 1){
                                    if (c == 0){
                                        if (d == ""){
                                            if (e==false){
                                                d = d :: "abc";
                                            }
                                        }
                                    }
                                }
                            }
                        } 
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_PS236(self):
        input = """ add: function integer(x: integer, y: integer) {
                        return x + y;
                    }
                    a: integer;
                    main: function void () {
                        add(3,4);
                        a = add(1,3);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_PS237(self):
        input = """ mna: function void (a: integer, b: integer, c: integer, d: string, e: boolean) {
                        a = 0;
                        b = 0;
                        for (a = 5, a <= 10, a + 1){
                            if (b == 0){
                                return a[b[c[2]]] + 3;
                            }
                            else return a[b + foo(a)] + 3;
                        } 
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

    # def test_PS238(self):
    #     input = """ a: integer = 5;
    #                 main: function void () {
    #                     do {
    #                         a = a + 1;
    #                     } while (a < 10);
    #                 }
    #             """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 238))

    # def test_PS239(self):
    #     input = """ a: integer = 5;
    #                 main: function void () {
    #                     do {
    #                         a = a + 1
    #                     } while (a < 10);
    #                 }
    #             """
    #     expect = "Error on line 5 col 24: }"
    #     self.assertTrue(TestParser.test(input, expect, 239))

    