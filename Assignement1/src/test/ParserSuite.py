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
                    emches : integer = 5635465; // A C++ style comment"""
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
                    emches: function void () inherit ABC {
                        length,width : float;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_PS226(self):
        input = """ emches : integer = 5635465;
                    main: function void () {
                        while (z <= a) {
                            z = z + 1;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_PS227(self):
        input = """ emches : integer = 5635465;
                    main: function void () {
                        for (i = 1, i < a, i + 1) {
                            writeInt(i);
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_PS228(self):
        input = """ emches : integer = 5635465;
                    main: function void () {
                        do {
                            a = a + 1;
                        } while (a < 10);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_PS229(self):
        input = """ emches : integer = 5635465;
                    main: function void () {
                        do {
                            a = a + 1
                        } while (a < 10);
                    }
                """
        expect = "Error on line 5 col 24: }"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_PS230(self):
        input = """ emches : integer = 5635465;
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
        input = """ emches : integer = 5635465;
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
        input = """ emches : integer = 5635465;
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
        input = """ emches : integer = 5635465;
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

    def test_PS238(self):
        input = """
                emches: function void (a: integer, b: integer, c: integer, d: string, e: boolean) {
                    for (a = 5, a <= 10, a + 1){
                        for (b = 15, b >= 1, b - 1){
                            for (c = 0, c >= -10, c - 1){
                                if (c == 0){
                                    if (d == ""){
                                        if (e==false){
                                            if (a == b + c % c){
                                                c = -1.12e+12;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    } 
                }
                """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_PS239(self):
        input = """ 
                emches: function void (a: integer, b: integer, c: integer, d: string, e: boolean) {
                    for (a = 5, a <= 10, a + 1){
                        for (b = 15, b >= 1, b - 1){
                            for (c = 0, c >= -10, c - 1){
                                if (c == 0){
                                    if (d == ""){
                                        if (e==false){
                                            if (a == b + c  c){
                                                c = -1;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    } 
                }
                """
        expect = "Error on line 9 col 60: c"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_PS240(self):
        input = """
                ma_in: function float()
                {
                    return a[b[2]]*a[b]+dasfadsf+widsafdth / 2456 * foo(please,give,me,hehe) + foo(2,3,4);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_PS241(self):
        input = """ func1: function integer () {
                        if (true) {
                            return 1;
                        } else {
                            return 2;
                        }
                        return 3;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_PS242(self):
        input = """ unc1: function integer (inherit func2: float, param1: integer, param2: auto) {
                        return param1 + param2;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_PS243(self):
        input = """ func1: function void () {
                        func2: function integer {
                            return 42;
                        }
                    }"""
        expect = "Error on line 2 col 31: function"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_PS244(self):
        input = """ var1, var2: integer = 42, 84;
                    var3: string = "hello";
                    var4: auto = var1 + var2;
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_PS245(self):
        input = """ test: string = "depressed";
                    stringconcat:  function string () {
                        for ( i = 0, i <= 10, i + 1){
                            concattest = test :: "z";
                        }
                        return concattest;
                    }
                    emches: function void () {
                        // i sadfhgafewfklmkaweyjtrcasdf
                        a: string = stringconcat();
                        /*dgsdfgsdfgsdfg
                        hjsdgfdshgjdsf
                        sadfghasdfas*/
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_PS246(self):
        input = """ emches : integer = 5635465;
                    main: function void () {
                        while (z <= a) {
                            if (z % a != 5){
                                printString("hehe");
                                continue;
                            }
                            z = z + 1;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_PS247(self):
        input = """ a: boolean = !true;
                    print: function void (){
                        do{
                            printString("hehe");
                        } while (a == true);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_PS248(self):
        input = """ a: boolean = true;
                    print: function void (){
                        do{
                            printString("hehe");
                        } while (a = true);
                    }
                """
        expect = "Error on line 5 col 35: ="
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_PS249(self):
        input = """ emches : integer = 5635465;
                    main: function void () {
                        do {
                            a = b < c;
                            a = b > c;
                            a = b <= c;
                            a = b >= c;
                        } while (a < 10);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_PS250(self):
        input = """ emches : integer = 5635465;
                    main: function void () {
                        do {
                            a = b + c;
                            a = b - c;
                            a = b * c;
                            a = b / c;
                            a = b % c;
                        } while (a < 10);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_PS251(self):
        input = """ emches : integer = 5635465;
                    main: function void () {
                        do {
                            a = b && c;
                            a = b || c;
                            // a = b * c;
                            // a = b / c;
                        } while (a < 10);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))
    
    def test_PS252(self):
        input = """ emches : integer = 5635465;
                    main: function void () {
                        do {
                            a = b :: d :: t::e:: c;/*
                            a = b - c;
                            a = b * c;
                            a = b / c;
                            a = b % c;*/
                        } while (a < 10);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_PS253(self):
        input = """ emches : integer = 5635465;
                    main: function void () {
                        do {
                            a = !b;/*
                            a = b - c;
                            a = b * c;
                            a = b / c;
                            a = b % c;*/
                        } while (a < 10);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_PS254(self):
        input = """ emches : integer = 5635465;
                    main: function void () {
                        do {
                            a = b == c;
                            a = b != c;/*
                            a = b - c;
                            a = b * c;
                            a = b / c;
                            a = b % c;*/
                        } while (a < 10);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_PS255(self):
        input = """ test: string = "depressed";
                    stringconcat:  function string () {
                        for ( i = 0, i <= 10, i + 1){
                            concattest = test :: "z" :: "asd" :: "sadasd";
                        }
                        return concattest;
                    }
                    emches: function void () {
                        a: string = stringconcat();
                        if ((a && a+a && a-a) != "awsedaw"){
                            break;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_PS256(self):
        input = """ emches : integer = 5635465;
                    main: function boolean () {
                        while (z <= a) {
                            if (z % a != 5){
                                return true;
                                //continue;
                            }
                            z = z + 1;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_PS257(self):
        input = """ a: boolean = !true;
                    print: function integer (){
                        do{
                            return 1;
                        } while (a == true);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_PS258(self):
        input = """ a: boolean = true;
                    print: function string (){
                        do{
                            printString("hehe");
                        } while (a == true);
                        return "hehe";
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_PS259(self):
        input = """ emches : integer = 5635465;
                    main: function float () {
                        do {
                            a = b < c;
                            a = b > c;
                            a = b <= c;
                            a = b >= c;
                        } while (a < 10);
                        return a;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_PS260(self):
        input = """ emches : integer = 5635465;
                    main: function float () {
                        board[43252345] = {
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                        };
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

        