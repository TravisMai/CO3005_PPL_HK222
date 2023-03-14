import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_AST301(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_AST302(self):
        input = """x, y, z: integer;"""
        expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, IntegerType)
	VarDecl(z, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_AST303(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_AST304(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;
        d,e,f: boolean;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
	VarDecl(d, BooleanType)
	VarDecl(e, BooleanType)
	VarDecl(f, BooleanType)
])"""
        self.assertTrue(TestAST.test(input, expect, 304))
        
    def test_AST305(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b, z: float = 1.2, 1.2e3, 4.e4;
        c,d,e: boolean;
        f,h,i,j: string;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType, FloatLit(1.2))
	VarDecl(b, FloatType, FloatLit(1200.0))
	VarDecl(z, FloatType, FloatLit(40000.0))
	VarDecl(c, BooleanType)
	VarDecl(d, BooleanType)
	VarDecl(e, BooleanType)
	VarDecl(f, StringType)
	VarDecl(h, StringType)
	VarDecl(i, StringType)
	VarDecl(j, StringType)
])"""
        self.assertTrue(TestAST.test(input, expect, 305))
        
    def test_AST306(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b, z: float = 1.2, 1.2e3, 4.e4;
        c,d,e: boolean = true, false, true;
        f: string;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType, FloatLit(1.2))
	VarDecl(b, FloatType, FloatLit(1200.0))
	VarDecl(z, FloatType, FloatLit(40000.0))
	VarDecl(c, BooleanType, BooleanLit(True))
	VarDecl(d, BooleanType, BooleanLit(False))
	VarDecl(e, BooleanType, BooleanLit(True))
	VarDecl(f, StringType)
])"""
        self.assertTrue(TestAST.test(input, expect, 306))
        
    def test_AST307(self):
        input = """x: integer = 123123;
        a: float = 1.2345;
        c: boolean = true;
        f: array[5,5,2,1] of integer;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(123123))
	VarDecl(a, FloatType, FloatLit(1.2345))
	VarDecl(c, BooleanType, BooleanLit(True))
	VarDecl(f, ArrayType([5, 5, 2, 1], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))
        
    def test_AST308(self):
        input = """x: integer = 123123;
        a: float = 1.2345;
        c: boolean = true;
        f: array[5] of integer = {1,2,3,4,5};"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(123123))
	VarDecl(a, FloatType, FloatLit(1.2345))
	VarDecl(c, BooleanType, BooleanLit(True))
	VarDecl(f, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))
        
    def test_AST309(self):
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_AST310(self):
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))
        
    def test_AST311(self):
        input = """x: integer = 123123;
        a: float = 1.2345;
        c: auto = true;
        f: array[5] of integer = {1,2,3,4,5};
        main: function void () {}
        test: function integer(){}"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(123123))
	VarDecl(a, FloatType, FloatLit(1.2345))
	VarDecl(c, AutoType, BooleanLit(True))
	VarDecl(f, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	FuncDecl(test, IntegerType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))
        
    def test_AST312(self):
        input = """
        f: array[5] of integer = {1,2,3,4,5};
        main: function void () {}
        MaiHuuNghia2052612: function void ( inherit out x : float, out lmeo: integer) inherit fact {}"""
        expect = """Program([
	VarDecl(f, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	FuncDecl(MaiHuuNghia2052612, VoidType, [InheritOutParam(x, FloatType), OutParam(lmeo, IntegerType)], fact, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))
        
    def test_AST313(self):
        input = """ /* Mai Huu Nghia 2052612 */
        f: array[5] of integer = {1,2,3,4,5};
        main: function void () {
            r, s: integer;
            r = 2.0;
            b: float = 6.5;
            a: array[5] of string;
        }
        MaiHuuNghia2052612: function void ( inherit out x : float, out lmeo: integer) inherit fact {

        }"""
        expect = """Program([
	VarDecl(f, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(r, IntegerType), VarDecl(s, IntegerType), AssignStmt(Id(r), FloatLit(2.0)), VarDecl(b, FloatType, FloatLit(6.5)), VarDecl(a, ArrayType([5], StringType))]))
	FuncDecl(MaiHuuNghia2052612, VoidType, [InheritOutParam(x, FloatType), OutParam(lmeo, IntegerType)], fact, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))
        
    def test_AST314(self):
        input = """ /* Mai Huu Nghia 2052612 */
        f: array[5] of integer = {1,2,3,4,5};
        main: function void () {
            r, s: integer;
            r = 2.0;
            b: float = 6.5;
            a: array[5] of string;
        }
        MaiHuuNghia2052612: function void ( inherit out x : float, out lmeo: integer) inherit fact {
            x = MaiHuuNghia2052612(10,10,10,10);
        }"""
        expect = """Program([
	VarDecl(f, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(r, IntegerType), VarDecl(s, IntegerType), AssignStmt(Id(r), FloatLit(2.0)), VarDecl(b, FloatType, FloatLit(6.5)), VarDecl(a, ArrayType([5], StringType))]))
	FuncDecl(MaiHuuNghia2052612, VoidType, [InheritOutParam(x, FloatType), OutParam(lmeo, IntegerType)], fact, BlockStmt([AssignStmt(Id(x), FuncCall(MaiHuuNghia2052612, [IntegerLit(10), IntegerLit(10), IntegerLit(10), IntegerLit(10)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))
        
    def test_AST315(self):
        input = """ /* Mai Huu Nghia 2052612 */
        f: array[5] of integer = {1,2,3,4,5};
        main: function void ( inherit out x : float, out lmeo: integer) inherit fact {
            if (n == 0) x = 1;
            else x = 0;
        }"""
        expect = """Program([
	VarDecl(f, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))
	FuncDecl(main, VoidType, [InheritOutParam(x, FloatType), OutParam(lmeo, IntegerType)], fact, BlockStmt([IfStmt(BinExpr(==, n, IntegerLit(0)), AssignStmt(Id(x), IntegerLit(1)), AssignStmt(Id(x), IntegerLit(0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))
        
    def test_AST316(self):
        input = """ /* Mai Huu Nghia 2052612 */
        f: array[5] of integer = {1,2,3,4,5};
        main: function void ( inherit out x : float, out lmeo: integer) inherit fact {
            if(x<y && y < 9 && z != 10) z = 456;
            else z = 34576;
        }
        asd: integer =10;
        asdfsd: float;"""
        expect = """Program([
	VarDecl(f, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))
	FuncDecl(main, VoidType, [InheritOutParam(x, FloatType), OutParam(lmeo, IntegerType)], fact, BlockStmt([IfStmt(BinExpr(&&, BinExpr(&&, BinExpr(<, x, y), BinExpr(<, y, IntegerLit(9))), BinExpr(!=, z, IntegerLit(10))), AssignStmt(Id(z), IntegerLit(456)), AssignStmt(Id(z), IntegerLit(34576)))]))
	VarDecl(asd, IntegerType, IntegerLit(10))
	VarDecl(asdfsd, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 316))
        
    def test_AST316(self):
        input = """ /* Mai Huu Nghia 2052612 */
        f: array[5] of integer = {1,2,3,4,5};
        main: function void ( inherit out x : float, out lmeo: integer) inherit fact {
            if(x<y && y < 9 && z != 10) z = 456;
            else z = 34576;
            if (i % 2 == 0){
                result: integer = 2 + 3 * 4 / (5 - 1);
                arr: array[3,5] of integer;
                break;
            }
        }
        asd: integer =10;
        asdfsd: function auto() {}"""
        expect = """Program([
	VarDecl(f, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))
	FuncDecl(main, VoidType, [InheritOutParam(x, FloatType), OutParam(lmeo, IntegerType)], fact, BlockStmt([IfStmt(BinExpr(&&, BinExpr(&&, BinExpr(<, x, y), BinExpr(<, y, IntegerLit(9))), BinExpr(!=, z, IntegerLit(10))), AssignStmt(Id(z), IntegerLit(456)), AssignStmt(Id(z), IntegerLit(34576))), IfStmt(BinExpr(==, BinExpr(%, i, IntegerLit(2)), IntegerLit(0)), BlockStmt([VarDecl(result, IntegerType, BinExpr(+, IntegerLit(2), BinExpr(/, BinExpr(*, IntegerLit(3), IntegerLit(4)), BinExpr(-, IntegerLit(5), IntegerLit(1))))), VarDecl(arr, ArrayType([3, 5], IntegerType)), BreakStmt()]))]))
	VarDecl(asd, IntegerType, IntegerLit(10))
	FuncDecl(asdfsd, AutoType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))
        
    def test_AST317(self):
        input = """ /* Mai Huu Nghia 2052612 */
        main: function void ( inherit out x : float, out lmeo: integer) inherit fact {
            if(x<y && y < 9 && z != 10) z = 456;
            else z = 34576;
            if (i % 2 == 0){
                result: integer = 2 + 3 * 4 / (5 - 1);
                arr: array[3,5] of integer;
                break;
            }
        }
        asd: integer =10;
        asdfsd: function auto()
        {
            return a[b[2]]*a[b]+dasfadsf+widsafdth / 2456 * foo(please,give,me,hehe) + foo(2,3,4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(x, FloatType), OutParam(lmeo, IntegerType)], fact, BlockStmt([IfStmt(BinExpr(&&, BinExpr(&&, BinExpr(<, x, y), BinExpr(<, y, IntegerLit(9))), BinExpr(!=, z, IntegerLit(10))), AssignStmt(Id(z), IntegerLit(456)), AssignStmt(Id(z), IntegerLit(34576))), IfStmt(BinExpr(==, BinExpr(%, i, IntegerLit(2)), IntegerLit(0)), BlockStmt([VarDecl(result, IntegerType, BinExpr(+, IntegerLit(2), BinExpr(/, BinExpr(*, IntegerLit(3), IntegerLit(4)), BinExpr(-, IntegerLit(5), IntegerLit(1))))), VarDecl(arr, ArrayType([3, 5], IntegerType)), BreakStmt()]))]))
	VarDecl(asd, IntegerType, IntegerLit(10))
	FuncDecl(asdfsd, AutoType, [], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(*, ArrayCell(a, [ArrayCell(b, [IntegerLit(2)])]), ArrayCell(a, [b])), dasfadsf), BinExpr(*, BinExpr(/, widsafdth, IntegerLit(2456)), FuncCall(foo, [please, give, me, hehe]))), FuncCall(foo, [IntegerLit(2), IntegerLit(3), IntegerLit(4)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))
    
    def test_AST318(self):
        input = """ /* Mai Huu Nghia 2052612 */
        emches : integer = 2052612;
        fib: function void(n:integer) {
            if (n == 1 || n == 0) {} 
            else{
                a,b : integer = 0,1;
                for ( i = 2, i < n+1, i+1 ){
                    c = a + b;
                    a = b;
                    b = c;
                }
                return b;
            }
        }
        print: function void (){
            print(fib(3+1));
        }"""
        expect = """Program([
	VarDecl(emches, IntegerType, IntegerLit(2052612))
	FuncDecl(fib, VoidType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(==, n, IntegerLit(1)), BinExpr(==, n, IntegerLit(0))), BlockStmt([]), BlockStmt([VarDecl(a, IntegerType, IntegerLit(0)), VarDecl(b, IntegerType, IntegerLit(1)), ForStmt(AssignStmt(i, IntegerLit(2)), BinExpr(<, i, BinExpr(+, n, IntegerLit(1))), BinExpr(+, i, IntegerLit(1)), BlockStmt([AssignStmt(Id(c), BinExpr(+, a, b)), AssignStmt(Id(a), b), AssignStmt(Id(b), c)])), ReturnStmt(b)]))]))
	FuncDecl(print, VoidType, [], None, BlockStmt([CallStmt(print, FuncCall(fib, [BinExpr(+, IntegerLit(3), IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))
        
    def test_AST319(self):
        input = """ /* Mai Huu Nghia 2052612 */
        main: function void () {
            for (i = 1, i < -2052612, i + 1) {
                writeInt(i);
            }
            y = !x;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(i, IntegerLit(1)), BinExpr(<, i, UnExpr(-, IntegerLit(2052612))), BinExpr(+, i, IntegerLit(1)), BlockStmt([CallStmt(writeInt, i)])), AssignStmt(Id(y), UnExpr(!, x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))
        
    def test_AST320(self):
        input = """ /* Mai Huu Nghia 2052612 */
        main: function void () {
            for (i = 1, i < a, i + 1) {
                if (i % 2 == 0){
                    arr: array[3,5] of integer;
                    break;
                }
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(i, IntegerLit(1)), BinExpr(<, i, a), BinExpr(+, i, IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, i, IntegerLit(2)), IntegerLit(0)), BlockStmt([VarDecl(arr, ArrayType([3, 5], IntegerType)), BreakStmt()]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))
        
    def test_AST321(self):
        input = """ /* Mai Huu Nghia 2052612 */
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
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(i, IntegerLit(1)), BinExpr(<, i, a), BinExpr(+, i, IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, i, IntegerLit(2)), IntegerLit(0)), BlockStmt([VarDecl(arr, ArrayType([3, 5], IntegerType)), BreakStmt()]))])), ForStmt(AssignStmt(i, IntegerLit(1)), BinExpr(<, i, a), BinExpr(+, i, IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(j, i), BinExpr(<, j, a), BinExpr(+, j, IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, j, IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(ArrayCell(Id(arr), [IntegerLit(1), IntegerLit(3)]), IntegerLit(3)), BreakStmt()]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))
        
    def test_AST322(self):
        input = """ /* Mai Huu Nghia 2052612 */
        mna: function void (a: integer, b: integer, c: integer, d: string, e: boolean) {
            a = 0;
            b = 0;
            for (a = 5, a <= 10, a + 1){
                for (b = 15, b >= 1, b - 1){
                    for (c = 0, c >= -10, c - 1){
                        if (c == 0){
                            if (d == 75){
                                if (e==false){
                                    d = !d;
                                }
                            }
                        }
                    }
                }
            } 
        }"""
        expect = """Program([
	FuncDecl(mna, VoidType, [Param(a, IntegerType), Param(b, IntegerType), Param(c, IntegerType), Param(d, StringType), Param(e, BooleanType)], None, BlockStmt([AssignStmt(Id(a), IntegerLit(0)), AssignStmt(Id(b), IntegerLit(0)), ForStmt(AssignStmt(a, IntegerLit(5)), BinExpr(<=, a, IntegerLit(10)), BinExpr(+, a, IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(b, IntegerLit(15)), BinExpr(>=, b, IntegerLit(1)), BinExpr(-, b, IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(c, IntegerLit(0)), BinExpr(>=, c, UnExpr(-, IntegerLit(10))), BinExpr(-, c, IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, c, IntegerLit(0)), BlockStmt([IfStmt(BinExpr(==, d, IntegerLit(75)), BlockStmt([IfStmt(BinExpr(==, e, BooleanLit(False)), BlockStmt([AssignStmt(Id(d), UnExpr(!, d))]))]))]))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))
        
    def test_AST323(self):
        input = """ /* Mai Huu Nghia 2052612 */
        main: function void () {
            while (z <= a_5) {
                z = z + 1;
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<=, z, a_5), BlockStmt([AssignStmt(Id(z), BinExpr(+, z, IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))
        
    def test_AST324(self):
        input = """ /* Mai Huu Nghia 2052612 */
        emches : integer = 2052612;
        main: function void () {
            while (z <= a) {
                if (z % a != 5){
                    printString(hehe);
                    continue;
                }
                z = z + 1;
            }
        }"""
        expect = """Program([
	VarDecl(emches, IntegerType, IntegerLit(2052612))
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<=, z, a), BlockStmt([IfStmt(BinExpr(!=, BinExpr(%, z, a), IntegerLit(5)), BlockStmt([CallStmt(printString, hehe), ContinueStmt()])), AssignStmt(Id(z), BinExpr(+, z, IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))
        
    def test_AST325(self):
        input = """ /* Mai Huu Nghia 2052612 */
        main: function void () {
            while(i < 10) {while(i < 9) {while(i < 8) {while(i < 7) {while(i < 6) {while(i < 5) {while(i < 4) {while(i < 3) {while(i < 2) {while(i < 1) {while(i < 0) {i = i + 1; j = j - 1;}}}}}}}}}}}
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, i, IntegerLit(10)), BlockStmt([WhileStmt(BinExpr(<, i, IntegerLit(9)), BlockStmt([WhileStmt(BinExpr(<, i, IntegerLit(8)), BlockStmt([WhileStmt(BinExpr(<, i, IntegerLit(7)), BlockStmt([WhileStmt(BinExpr(<, i, IntegerLit(6)), BlockStmt([WhileStmt(BinExpr(<, i, IntegerLit(5)), BlockStmt([WhileStmt(BinExpr(<, i, IntegerLit(4)), BlockStmt([WhileStmt(BinExpr(<, i, IntegerLit(3)), BlockStmt([WhileStmt(BinExpr(<, i, IntegerLit(2)), BlockStmt([WhileStmt(BinExpr(<, i, IntegerLit(1)), BlockStmt([WhileStmt(BinExpr(<, i, IntegerLit(0)), BlockStmt([AssignStmt(Id(i), BinExpr(+, i, IntegerLit(1))), AssignStmt(Id(j), BinExpr(-, j, IntegerLit(1)))]))]))]))]))]))]))]))]))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))
        
    def test_AST326(self):
        input = """ /* Mai Huu Nghia 2052612 */
        emches: function void () {
            for (i = 1, i <= 10, i+2) { while (j < i && k >= 0) { j=j+1; k=k-1; } }
        }"""
        expect = """Program([
	FuncDecl(emches, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(i, IntegerLit(1)), BinExpr(<=, i, IntegerLit(10)), BinExpr(+, i, IntegerLit(2)), BlockStmt([WhileStmt(BinExpr(&&, BinExpr(<, j, i), BinExpr(>=, k, IntegerLit(0))), BlockStmt([AssignStmt(Id(j), BinExpr(+, j, IntegerLit(1))), AssignStmt(Id(k), BinExpr(-, k, IntegerLit(1)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))
        
    def test_AST327(self):
        input = """ /* Mai Huu Nghia 2052612 */
        print: function void (){
            while (i < 10 && j > 0 && k != 5) { 
                if ((i + j + k) % 2 == 0) { 
                    j=j-1; k=k+1; 
                } 
                else { 
                    i=i+1; 
                    k=k-1; 
                } 
                if (j == 0 || k == 0) break;  
            }
        }"""
        expect = """Program([
	FuncDecl(print, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(&&, BinExpr(&&, BinExpr(<, i, IntegerLit(10)), BinExpr(>, j, IntegerLit(0))), BinExpr(!=, k, IntegerLit(5))), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, BinExpr(+, BinExpr(+, i, j), k), IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(Id(j), BinExpr(-, j, IntegerLit(1))), AssignStmt(Id(k), BinExpr(+, k, IntegerLit(1)))]), BlockStmt([AssignStmt(Id(i), BinExpr(+, i, IntegerLit(1))), AssignStmt(Id(k), BinExpr(-, k, IntegerLit(1)))])), IfStmt(BinExpr(||, BinExpr(==, j, IntegerLit(0)), BinExpr(==, k, IntegerLit(0))), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))
        
    def test_AST328(self):
        input = """ /* Mai Huu Nghia 2052612 */
        main: function void () {
            if ((2+2) == 4 && (3*3) > 8) {
                x: integer = 0;
                for (i = 0, i < 5, i+1) {
                    while (x < 10) {
                        x=x+1;
                        if (x % 2 == 0 || x == 5) {
                            continue;
                        } else{
                            break;
                        }
                    }
                }
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(&&, BinExpr(==, BinExpr(+, IntegerLit(2), IntegerLit(2)), IntegerLit(4)), BinExpr(>, BinExpr(*, IntegerLit(3), IntegerLit(3)), IntegerLit(8))), BlockStmt([VarDecl(x, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, i, IntegerLit(5)), BinExpr(+, i, IntegerLit(1)), BlockStmt([WhileStmt(BinExpr(<, x, IntegerLit(10)), BlockStmt([AssignStmt(Id(x), BinExpr(+, x, IntegerLit(1))), IfStmt(BinExpr(||, BinExpr(==, BinExpr(%, x, IntegerLit(2)), IntegerLit(0)), BinExpr(==, x, IntegerLit(5))), BlockStmt([ContinueStmt()]), BlockStmt([BreakStmt()]))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))
        
    def test_AST329(self):
        input = """ /* Mai Huu Nghia 2052612 */
        main: function void () {
            while(i < 10 || j > 5) {i = i + 1; j = j - 1;}
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(||, BinExpr(<, i, IntegerLit(10)), BinExpr(>, j, IntegerLit(5))), BlockStmt([AssignStmt(Id(i), BinExpr(+, i, IntegerLit(1))), AssignStmt(Id(j), BinExpr(-, j, IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))
        
    def test_AST330(self):
        input = """ /* Mai Huu Nghia 2052612 */
        main: function void () {
            if (a < b && c < d && e > f || g > h && i <= j && k >= l || m != n && o == p) {x=1;} else {x=2;}
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(&&, BinExpr(||, BinExpr(&&, BinExpr(&&, BinExpr(||, BinExpr(&&, BinExpr(&&, BinExpr(<, a, b), BinExpr(<, c, d)), BinExpr(>, e, f)), BinExpr(>, g, h)), BinExpr(<=, i, j)), BinExpr(>=, k, l)), BinExpr(!=, m, n)), BinExpr(==, o, p)), BlockStmt([AssignStmt(Id(x), IntegerLit(1))]), BlockStmt([AssignStmt(Id(x), IntegerLit(2))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))
        
    def test_AST331(self):    
        input = """ /* Mai Huu Nghia 2052612 */
        test: string = "depressed";
        stringconcat:  function string () {
            for ( i = 0, i <= 10, i + 1){
                hehe:string = "12`1";
                concattest = test :: "z" :: "asd" :: "sadasd";
            }
            return concattest;
        }
        lmeo: string = stringconcat(test);"""
        expect = """Program([
	VarDecl(test, StringType, StringLit(depressed))
	FuncDecl(stringconcat, StringType, [], None, BlockStmt([ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<=, i, IntegerLit(10)), BinExpr(+, i, IntegerLit(1)), BlockStmt([VarDecl(hehe, StringType, StringLit(12`1)), AssignStmt(Id(concattest), BinExpr(::, BinExpr(::, BinExpr(::, test, StringLit(z)), StringLit(asd)), StringLit(sadasd)))])), ReturnStmt(concattest)]))
	VarDecl(lmeo, StringType, FuncCall(stringconcat, [test]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))
        
    def test_AST332(self):    
        input = """ /* Mai Huu Nghia 2052612 */
        test: string = "depressed";
        stringconcat:  function string () {
            for ( i = 0, i <= 10, hehe(i+1)){
                hehe:string = "12`1";
                concattest = test :: "z" :: "asd" :: "sadasd";
                hehe("wqeqewqeqwe");
            }
            return concattest;
        }
        lmeo: string = stringconcat(test);"""
        expect = """Program([
	VarDecl(test, StringType, StringLit(depressed))
	FuncDecl(stringconcat, StringType, [], None, BlockStmt([ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<=, i, IntegerLit(10)), FuncCall(hehe, [BinExpr(+, i, IntegerLit(1))]), BlockStmt([VarDecl(hehe, StringType, StringLit(12`1)), AssignStmt(Id(concattest), BinExpr(::, BinExpr(::, BinExpr(::, test, StringLit(z)), StringLit(asd)), StringLit(sadasd))), CallStmt(hehe, StringLit(wqeqewqeqwe))])), ReturnStmt(concattest)]))
	VarDecl(lmeo, StringType, FuncCall(stringconcat, [test]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))
        
    def test_AST333(self):    
        input = """ /* Mai Huu Nghia 2052612 */
        main: function void () {
            do {
                a = a + 1;
            } while (a < 10);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, a, IntegerLit(10)), BlockStmt([AssignStmt(Id(a), BinExpr(+, a, IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))
        
    def test_AST334(self):    
        input = """ /* Mai Huu Nghia 2052612 */
        a: boolean = !true;
        print: function void (){
            do{
                printString("hehe");
            } while (a == true);
        }"""
        expect = """Program([
	VarDecl(a, BooleanType, UnExpr(!, BooleanLit(True)))
	FuncDecl(print, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, a, BooleanLit(True)), BlockStmt([CallStmt(printString, StringLit(hehe))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))
        
    def test_AST335(self):    
        input = """ /* Mai Huu Nghia 2052612 */
        emches : integer = 2052612;
        main: function void () {
            do {
                a = b < c;
                a = b > c;
                a = b <= c;
                a = b >= c;
            } while (a < 10);
        }"""
        expect = """Program([
	VarDecl(emches, IntegerType, IntegerLit(2052612))
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, a, IntegerLit(10)), BlockStmt([AssignStmt(Id(a), BinExpr(<, b, c)), AssignStmt(Id(a), BinExpr(>, b, c)), AssignStmt(Id(a), BinExpr(<=, b, c)), AssignStmt(Id(a), BinExpr(>=, b, c))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))
        
    def test_AST336(self):    
        input = """ /* Mai Huu Nghia 2052612 */
        emches : integer = 2052612;
        main: function void () {
            do {
                a = b + c;
                a = b - c;
                a = b * c;
                a = b / c;
                a = b % c;
            } while (a < 10);
        }"""
        expect = """Program([
	VarDecl(emches, IntegerType, IntegerLit(2052612))
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, a, IntegerLit(10)), BlockStmt([AssignStmt(Id(a), BinExpr(+, b, c)), AssignStmt(Id(a), BinExpr(-, b, c)), AssignStmt(Id(a), BinExpr(*, b, c)), AssignStmt(Id(a), BinExpr(/, b, c)), AssignStmt(Id(a), BinExpr(%, b, c))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))
        
    def test_AST336(self):    
        input = """ /* Mai Huu Nghia 2052612 */
        emches : integer = 2052612;
        main: function void () {
            do {
                a = b && c;
                a = b || c;
                a = b * c;
                a = b / c;
            } while (a < 10);
        }"""
        expect = """Program([
	VarDecl(emches, IntegerType, IntegerLit(2052612))
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, a, IntegerLit(10)), BlockStmt([AssignStmt(Id(a), BinExpr(&&, b, c)), AssignStmt(Id(a), BinExpr(||, b, c)), AssignStmt(Id(a), BinExpr(*, b, c)), AssignStmt(Id(a), BinExpr(/, b, c))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))
        
    def test_AST337(self):    
        input = """ /* Mai Huu Nghia 2052612 */
        emches : integer = 2052612;
        main: function void () {
            do {
                a = b :: d :: t::e:: c;
                a = !b;
            } while (a != !10);
        }"""
        expect = """Program([
	VarDecl(emches, IntegerType, IntegerLit(2052612))
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(!=, a, UnExpr(!, IntegerLit(10))), BlockStmt([AssignStmt(Id(a), BinExpr(::, BinExpr(::, BinExpr(::, BinExpr(::, b, d), t), e), c)), AssignStmt(Id(a), UnExpr(!, b))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))
        
    def test_AST338(self):    
        input = """ /* Mai Huu Nghia 2052612 */
        emches : integer = 2052612;
        main: function auto () {
            do {
                a = b :: d :: t::e:: c;
                a = !b;
                a = b == c;
                a = b != c;
                printString("hehe");
                return 1;
            } while (a != !10);
        }"""
        expect = """Program([
	VarDecl(emches, IntegerType, IntegerLit(2052612))
	FuncDecl(main, AutoType, [], None, BlockStmt([DoWhileStmt(BinExpr(!=, a, UnExpr(!, IntegerLit(10))), BlockStmt([AssignStmt(Id(a), BinExpr(::, BinExpr(::, BinExpr(::, BinExpr(::, b, d), t), e), c)), AssignStmt(Id(a), UnExpr(!, b)), AssignStmt(Id(a), BinExpr(==, b, c)), AssignStmt(Id(a), BinExpr(!=, b, c)), CallStmt(printString, StringLit(hehe)), ReturnStmt(IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))
        
    def test_AST339(self):    
        input = """ /* Mai Huu Nghia 2052612 */
        emches : integer = 2052612;
        main: function auto () {
            dividend, divisor: integer = 25,4;
            if ((a && a+a && a-a) != "awsedaw"){
                ba[2,3] = "3rdty";
            }
            quotient: integer = dividend / divisor;
            remainder:integer = dividend % divisor;
        }"""
        expect = """Program([
	VarDecl(emches, IntegerType, IntegerLit(2052612))
	FuncDecl(main, AutoType, [], None, BlockStmt([VarDecl(dividend, IntegerType, IntegerLit(25)), VarDecl(divisor, IntegerType, IntegerLit(4)), IfStmt(BinExpr(!=, BinExpr(&&, BinExpr(&&, a, BinExpr(+, a, a)), BinExpr(-, a, a)), StringLit(awsedaw)), BlockStmt([AssignStmt(ArrayCell(Id(ba), [IntegerLit(3), IntegerLit(2)]), StringLit(3rdty))])), VarDecl(quotient, IntegerType, BinExpr(/, dividend, divisor)), VarDecl(remainder, IntegerType, BinExpr(%, dividend, divisor))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))
        
    def test_AST340(self):    
        input = """ /* Mai Huu Nghia 2052612 */
        emches : integer = 2052612;
        main: function float () {
            {}{}{}{}{}{}{}{}{}{}
            do {a = b < c;a = b > c;a = b <= c;a = b >= c;} while (a < 10);
            return a;
        }"""
        expect = """Program([
	VarDecl(emches, IntegerType, IntegerLit(2052612))
	FuncDecl(main, FloatType, [], None, BlockStmt([BlockStmt([]), BlockStmt([]), BlockStmt([]), BlockStmt([]), BlockStmt([]), BlockStmt([]), BlockStmt([]), BlockStmt([]), BlockStmt([]), BlockStmt([]), DoWhileStmt(BinExpr(<, a, IntegerLit(10)), BlockStmt([AssignStmt(Id(a), BinExpr(<, b, c)), AssignStmt(Id(a), BinExpr(>, b, c)), AssignStmt(Id(a), BinExpr(<=, b, c)), AssignStmt(Id(a), BinExpr(>=, b, c))])), ReturnStmt(a)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))
        
    def test_AST341(self):    
        input = """ /* Mai Huu Nghia 2052612 */
        emches : integer = 2052612;
        main: function float () {
            do {do {do {do {do {do {do {a = b < c;a = b > c;a = b <= c;a = b >= c;} while (a < 4);} while (a < 5);} while (a < 6);} while (a < 7);} while (a < 8);} while (a < 9);} while (a < 10);
            continue;
        }"""
        expect = """Program([
	VarDecl(emches, IntegerType, IntegerLit(2052612))
	FuncDecl(main, FloatType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, a, IntegerLit(10)), BlockStmt([DoWhileStmt(BinExpr(<, a, IntegerLit(9)), BlockStmt([DoWhileStmt(BinExpr(<, a, IntegerLit(8)), BlockStmt([DoWhileStmt(BinExpr(<, a, IntegerLit(7)), BlockStmt([DoWhileStmt(BinExpr(<, a, IntegerLit(6)), BlockStmt([DoWhileStmt(BinExpr(<, a, IntegerLit(5)), BlockStmt([DoWhileStmt(BinExpr(<, a, IntegerLit(4)), BlockStmt([AssignStmt(Id(a), BinExpr(<, b, c)), AssignStmt(Id(a), BinExpr(>, b, c)), AssignStmt(Id(a), BinExpr(<=, b, c)), AssignStmt(Id(a), BinExpr(>=, b, c))]))]))]))]))]))]))])), ContinueStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))
        
    def test_AST342(self):    
        input = """ /* Mai Huu Nghia 2052612 */
        emches : integer = 2052612;
        main: function float () {
            do {do {do {do {do {do {do {a = b < c;a = b > c;a = b <= c;a = b >= c;} while (a < 4);} while (a < 5);} while (a < 6);} while (a < 7);} while (a < 8);} while (a < 9);} while (a < 10);
            break;
        }"""
        expect = """Program([
	VarDecl(emches, IntegerType, IntegerLit(2052612))
	FuncDecl(main, FloatType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, a, IntegerLit(10)), BlockStmt([DoWhileStmt(BinExpr(<, a, IntegerLit(9)), BlockStmt([DoWhileStmt(BinExpr(<, a, IntegerLit(8)), BlockStmt([DoWhileStmt(BinExpr(<, a, IntegerLit(7)), BlockStmt([DoWhileStmt(BinExpr(<, a, IntegerLit(6)), BlockStmt([DoWhileStmt(BinExpr(<, a, IntegerLit(5)), BlockStmt([DoWhileStmt(BinExpr(<, a, IntegerLit(4)), BlockStmt([AssignStmt(Id(a), BinExpr(<, b, c)), AssignStmt(Id(a), BinExpr(>, b, c)), AssignStmt(Id(a), BinExpr(<=, b, c)), AssignStmt(Id(a), BinExpr(>=, b, c))]))]))]))]))]))]))])), BreakStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))
        
    def test_AST343(self):    
        input = """ /* Mai Huu Nghia 2052612 */
        main: function float () {
            asd = a(2,3)[2,1];
        }"""
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(asd), ArrayCell(FuncCall(a, [IntegerLit(2), IntegerLit(3)]), [IntegerLit(2), IntegerLit(1)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))
        
    def test_AST344(self):    
        input = """ /* Mai Huu Nghia 2052612 */
        main: function float () {
            asd = a(2,3)[2,1];
        }"""
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(asd), ArrayCell(FuncCall(a, [IntegerLit(2), IntegerLit(3)]), [IntegerLit(2), IntegerLit(1)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))
        
    def test_AST345(self):    
        input = """ /* Mai Huu Nghia 2052612 */
        main: function float () {
            {}{}{}{}{}{{}}
            {{}}{}{}{{}}{}{}
            {}{{}}{{}}{}{}{}
            {}{}{{}}{}{}{}{}
            board[43252345] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        }"""
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([BlockStmt([]), BlockStmt([]), BlockStmt([]), BlockStmt([]), BlockStmt([]), BlockStmt([BlockStmt([])]), BlockStmt([BlockStmt([])]), BlockStmt([]), BlockStmt([]), BlockStmt([BlockStmt([])]), BlockStmt([]), BlockStmt([]), BlockStmt([]), BlockStmt([BlockStmt([])]), BlockStmt([BlockStmt([])]), BlockStmt([]), BlockStmt([]), BlockStmt([]), BlockStmt([]), BlockStmt([]), BlockStmt([BlockStmt([])]), BlockStmt([]), BlockStmt([]), BlockStmt([]), BlockStmt([]), AssignStmt(ArrayCell(Id(board), [IntegerLit(43252345)]), ArrayLit([IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))
        
    def test_AST346(self):
        input = """ /* Mai Huu Nghia 2052612 */
        main: function string () {
            a=9;b=c;a=21123+dsfdsfsdf+203123;
        }"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(9)), AssignStmt(Id(b), c), AssignStmt(Id(a), BinExpr(+, BinExpr(+, IntegerLit(21123), dsfdsfsdf), IntegerLit(203123)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))
        
    def test_AST347(self):
        input = """ /* Mai Huu Nghia 2052612 */
        main: function string () {
            break;break;break;break;break;break;break;break;break;
        }"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([BreakStmt(), BreakStmt(), BreakStmt(), BreakStmt(), BreakStmt(), BreakStmt(), BreakStmt(), BreakStmt(), BreakStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))
        
    def test_AST348(self):
        input = """ /* Mai Huu Nghia 2052612 */
        main: function string () {
            continue;continue;continue;continue;continue;continue;continue;continue;
        }"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([ContinueStmt(), ContinueStmt(), ContinueStmt(), ContinueStmt(), ContinueStmt(), ContinueStmt(), ContinueStmt(), ContinueStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))
        
    def test_AST349(self):
        input = """ /* Mai Huu Nghia 2052612 */
        main: function string () {
            return "please more than 90/100"; 
            return "please more than 90/100"; 
            return "please more than 90/100"; 
            return "please more than 90/100"; 
            return "please more than 90/100"; 
            return "please more than 90/100";
        }"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([ReturnStmt(StringLit(please more than 90/100)), ReturnStmt(StringLit(please more than 90/100)), ReturnStmt(StringLit(please more than 90/100)), ReturnStmt(StringLit(please more than 90/100)), ReturnStmt(StringLit(please more than 90/100)), ReturnStmt(StringLit(please more than 90/100))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))
        
    def test_AST350(self):
        input = """ /* Mai Huu Nghia 2052612 */
        main: function void () {
            m,n: integer;
            c: integer = !(a && b || c);
            a: boolean = -(!a + c*2322/5234 + b%2234 + !(a == foo())) ;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(m, IntegerType), VarDecl(n, IntegerType), VarDecl(c, IntegerType, UnExpr(!, BinExpr(||, BinExpr(&&, a, b), c))), VarDecl(a, BooleanType, UnExpr(-, BinExpr(+, BinExpr(+, BinExpr(+, UnExpr(!, a), BinExpr(/, BinExpr(*, c, IntegerLit(2322)), IntegerLit(5234))), BinExpr(%, b, IntegerLit(2234))), UnExpr(!, BinExpr(==, a, FuncCall(foo, []))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))
        
    def test_AST350(self):
        input = """ /* Mai Huu Nghia 2052612 */
        a: boolean = !false;
        print: function integer (){
            please_more_than_90(hsdad(asdasd(SAdasD(ASdasd()))));
        }
        a: boolean = !false;
        print: function integer (){
            please_more_than_90(hsdad(asdasd(SAdasD(ASdasd()))));
        }
        a: boolean = !false;
        print: function integer (){
            please_more_than_90(hsdad(asdasd(SAdasD(ASdasd()))));
        }
        a: boolean = !false;
        print: function integer (){
            please_more_than_90(hsdad(asdasd(SAdasD(ASdasd()))));
        }
        a: boolean = !false;
        print: function integer (){
            please_more_than_90(hsdad(asdasd(SAdasD(ASdasd()))));
        }
        a: boolean = !false;
        print: function integer (){
            please_more_than_90(hsdad(asdasd(SAdasD(ASdasd()))));
        }
        a: boolean = !false;
        print: function integer (){
            please_more_than_90(hsdad(asdasd(SAdasD(ASdasd()))));
        }
        a: boolean = !false;
        print: function integer (){
            please_more_than_90(hsdad(asdasd(SAdasD(ASdasd()))));
        }
        """
        expect = """Program([
	VarDecl(a, BooleanType, UnExpr(!, BooleanLit(False)))
	FuncDecl(print, IntegerType, [], None, BlockStmt([CallStmt(please_more_than_90, FuncCall(hsdad, [FuncCall(asdasd, [FuncCall(SAdasD, [FuncCall(ASdasd, [])])])]))]))
	VarDecl(a, BooleanType, UnExpr(!, BooleanLit(False)))
	FuncDecl(print, IntegerType, [], None, BlockStmt([CallStmt(please_more_than_90, FuncCall(hsdad, [FuncCall(asdasd, [FuncCall(SAdasD, [FuncCall(ASdasd, [])])])]))]))
	VarDecl(a, BooleanType, UnExpr(!, BooleanLit(False)))
	FuncDecl(print, IntegerType, [], None, BlockStmt([CallStmt(please_more_than_90, FuncCall(hsdad, [FuncCall(asdasd, [FuncCall(SAdasD, [FuncCall(ASdasd, [])])])]))]))
	VarDecl(a, BooleanType, UnExpr(!, BooleanLit(False)))
	FuncDecl(print, IntegerType, [], None, BlockStmt([CallStmt(please_more_than_90, FuncCall(hsdad, [FuncCall(asdasd, [FuncCall(SAdasD, [FuncCall(ASdasd, [])])])]))]))
	VarDecl(a, BooleanType, UnExpr(!, BooleanLit(False)))
	FuncDecl(print, IntegerType, [], None, BlockStmt([CallStmt(please_more_than_90, FuncCall(hsdad, [FuncCall(asdasd, [FuncCall(SAdasD, [FuncCall(ASdasd, [])])])]))]))
	VarDecl(a, BooleanType, UnExpr(!, BooleanLit(False)))
	FuncDecl(print, IntegerType, [], None, BlockStmt([CallStmt(please_more_than_90, FuncCall(hsdad, [FuncCall(asdasd, [FuncCall(SAdasD, [FuncCall(ASdasd, [])])])]))]))
	VarDecl(a, BooleanType, UnExpr(!, BooleanLit(False)))
	FuncDecl(print, IntegerType, [], None, BlockStmt([CallStmt(please_more_than_90, FuncCall(hsdad, [FuncCall(asdasd, [FuncCall(SAdasD, [FuncCall(ASdasd, [])])])]))]))
	VarDecl(a, BooleanType, UnExpr(!, BooleanLit(False)))
	FuncDecl(print, IntegerType, [], None, BlockStmt([CallStmt(please_more_than_90, FuncCall(hsdad, [FuncCall(asdasd, [FuncCall(SAdasD, [FuncCall(ASdasd, [])])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))
        
    def test_AST351(self):
        input = """ /* Mai Huu Nghia 2052612 */
        a: integer = !false;
        a: boolean = !false;
        a: float = !false;
        a: auto = !false;
        print: function integer (){}
        print: function boolean (){}
        print: function float (){}
        print: function auto (){}
        print: function void (){}
        """
        expect = """Program([
	VarDecl(a, IntegerType, UnExpr(!, BooleanLit(False)))
	VarDecl(a, BooleanType, UnExpr(!, BooleanLit(False)))
	VarDecl(a, FloatType, UnExpr(!, BooleanLit(False)))
	VarDecl(a, AutoType, UnExpr(!, BooleanLit(False)))
	FuncDecl(print, IntegerType, [], None, BlockStmt([]))
	FuncDecl(print, BooleanType, [], None, BlockStmt([]))
	FuncDecl(print, FloatType, [], None, BlockStmt([]))
	FuncDecl(print, AutoType, [], None, BlockStmt([]))
	FuncDecl(print, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))
        
    def test_AST352(self):
        input = """ /* Mai Huu Nghia 2052612 */
        bubbleSort: function void(arr: array[5] of integer, n: integer)
        {
            for (i = 0, i < n - 1, i+1)
            {
                swapped: boolean = false;
                for (j = 0, j < n - i - 1, j+1)
                {
                    if (arr[j] > arr[j + 1])
                    {
                        swap(arr[j], arr[j + 1]);
                        swapped = true;
                    }
                }
                if (swapped == false)
                    break;
            }
        }
        """
        expect = """Program([
	FuncDecl(bubbleSort, VoidType, [Param(arr, ArrayType([5], IntegerType)), Param(n, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, i, BinExpr(-, n, IntegerLit(1))), BinExpr(+, i, IntegerLit(1)), BlockStmt([VarDecl(swapped, BooleanType, BooleanLit(False)), ForStmt(AssignStmt(j, IntegerLit(0)), BinExpr(<, j, BinExpr(-, BinExpr(-, n, i), IntegerLit(1))), BinExpr(+, j, IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(arr, [j]), ArrayCell(arr, [BinExpr(+, j, IntegerLit(1))])), BlockStmt([CallStmt(swap, ArrayCell(arr, [j]), ArrayCell(arr, [BinExpr(+, j, IntegerLit(1))])), AssignStmt(Id(swapped), BooleanLit(True))]))])), IfStmt(BinExpr(==, swapped, BooleanLit(False)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))
        
    def test_AST353(self):
        input = """ /* Mai Huu Nghia 2052612 */
        selectionSort: function void(arr: array[5] of integer, n: integer)
        {
            i, j, min_idx: integer;

            for (i = 0, i < n - 1, i+1)
            {
                min_idx = i;
                for (j = i + 1, j < n, j+1)
                    if (arr[j] < arr[min_idx])
                        min_idx = j;

                swap(arr[min_idx], arr[i]);
            }
        }

        """
        expect = """Program([
	FuncDecl(selectionSort, VoidType, [Param(arr, ArrayType([5], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(j, IntegerType), VarDecl(min_idx, IntegerType), ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, i, BinExpr(-, n, IntegerLit(1))), BinExpr(+, i, IntegerLit(1)), BlockStmt([AssignStmt(Id(min_idx), i), ForStmt(AssignStmt(j, BinExpr(+, i, IntegerLit(1))), BinExpr(<, j, n), BinExpr(+, j, IntegerLit(1)), IfStmt(BinExpr(<, ArrayCell(arr, [j]), ArrayCell(arr, [min_idx])), AssignStmt(Id(min_idx), j))), CallStmt(swap, ArrayCell(arr, [min_idx]), ArrayCell(arr, [i]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))
        
    def test_AST354(self):
        input = """ /* Mai Huu Nghia 2052612 */
        insertionSort:function void(arr: array[5] of integer, n: integer)
        {
            i, j, j: integer;
            for (i = 1, i < n, i+1)
            {
                
                j = i - 1;
                while (j >= 0 && arr[j] > key)
                {
                    arr[5] = arr[i];
                    j = j - 1;
                }

                swap(arr[min_idx], arr[i]);
            }
        }
        """
        expect = """Program([
	FuncDecl(insertionSort, VoidType, [Param(arr, ArrayType([5], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(j, IntegerType), VarDecl(j, IntegerType), ForStmt(AssignStmt(i, IntegerLit(1)), BinExpr(<, i, n), BinExpr(+, i, IntegerLit(1)), BlockStmt([AssignStmt(Id(j), BinExpr(-, i, IntegerLit(1))), WhileStmt(BinExpr(&&, BinExpr(>=, j, IntegerLit(0)), BinExpr(>, ArrayCell(arr, [j]), key)), BlockStmt([AssignStmt(ArrayCell(Id(arr), [IntegerLit(5)]), ArrayCell(arr, [i])), AssignStmt(Id(j), BinExpr(-, j, IntegerLit(1)))])), CallStmt(swap, ArrayCell(arr, [min_idx]), ArrayCell(arr, [i]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))
        
    def test_AST355(self):
        input = """ /* Mai Huu Nghia 2052612 */
        insertionSort:function void(arr: array[5] of integer, n: integer)
        {
            i, j, j: integer;
            for (i = 1, i < n, i+1)
            {
                j = i - 1;
                while (j >= 0 && arr[j] > key)
                {
                    arr[5] = arr[i];
                    j = j - 1;
                }

                swap(arr[min_idx], arr[i]);
            }
        }
        """
        expect = """Program([
	FuncDecl(insertionSort, VoidType, [Param(arr, ArrayType([5], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(j, IntegerType), VarDecl(j, IntegerType), ForStmt(AssignStmt(i, IntegerLit(1)), BinExpr(<, i, n), BinExpr(+, i, IntegerLit(1)), BlockStmt([AssignStmt(Id(j), BinExpr(-, i, IntegerLit(1))), WhileStmt(BinExpr(&&, BinExpr(>=, j, IntegerLit(0)), BinExpr(>, ArrayCell(arr, [j]), key)), BlockStmt([AssignStmt(ArrayCell(Id(arr), [IntegerLit(5)]), ArrayCell(arr, [i])), AssignStmt(Id(j), BinExpr(-, j, IntegerLit(1)))])), CallStmt(swap, ArrayCell(arr, [min_idx]), ArrayCell(arr, [i]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))
        
    def test_AST356(self):
        input = """ /* Mai Huu Nghia 2052612 */
        a: integer = !false;
        a: boolean = !false;
        a: integer = !false;
        a: boolean = !false;
        print: function integer (){}
        a: float = !false;
        print: function auto (){}
        print: function integer (){}
        print: function void (){}
        a: auto = !false;
        a: integer = !false;
        a: boolean = !false;
        print: function integer (){}
        print: function boolean (){}
        print: function float (){}
        a: integer = !false;
        a: boolean = !false;
        print: function auto (){}
        print: function void (){}
        """
        expect = """Program([
	VarDecl(a, IntegerType, UnExpr(!, BooleanLit(False)))
	VarDecl(a, BooleanType, UnExpr(!, BooleanLit(False)))
	VarDecl(a, IntegerType, UnExpr(!, BooleanLit(False)))
	VarDecl(a, BooleanType, UnExpr(!, BooleanLit(False)))
	FuncDecl(print, IntegerType, [], None, BlockStmt([]))
	VarDecl(a, FloatType, UnExpr(!, BooleanLit(False)))
	FuncDecl(print, AutoType, [], None, BlockStmt([]))
	FuncDecl(print, IntegerType, [], None, BlockStmt([]))
	FuncDecl(print, VoidType, [], None, BlockStmt([]))
	VarDecl(a, AutoType, UnExpr(!, BooleanLit(False)))
	VarDecl(a, IntegerType, UnExpr(!, BooleanLit(False)))
	VarDecl(a, BooleanType, UnExpr(!, BooleanLit(False)))
	FuncDecl(print, IntegerType, [], None, BlockStmt([]))
	FuncDecl(print, BooleanType, [], None, BlockStmt([]))
	FuncDecl(print, FloatType, [], None, BlockStmt([]))
	VarDecl(a, IntegerType, UnExpr(!, BooleanLit(False)))
	VarDecl(a, BooleanType, UnExpr(!, BooleanLit(False)))
	FuncDecl(print, AutoType, [], None, BlockStmt([]))
	FuncDecl(print, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))
        
    def test_AST357(self):
        input = """ /* Mai Huu Nghia 2052612 */
        a: integer = !false;
        print: function integer (){
            if(false) {
                a[2131235] = a[213121] + 2;
                b[9213] = b[5123123] || true;
            } else{}
        }
        """
        expect = """Program([
	VarDecl(a, IntegerType, UnExpr(!, BooleanLit(False)))
	FuncDecl(print, IntegerType, [], None, BlockStmt([IfStmt(BooleanLit(False), BlockStmt([AssignStmt(ArrayCell(Id(a), [IntegerLit(2131235)]), BinExpr(+, ArrayCell(a, [IntegerLit(213121)]), IntegerLit(2))), AssignStmt(ArrayCell(Id(b), [IntegerLit(9213)]), BinExpr(||, ArrayCell(b, [IntegerLit(5123123)]), BooleanLit(True)))]), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))
        
    def test_AST358(self):
        input = """ /* Mai Huu Nghia 2052612 */
        railgfdgdfgfence_encfdgfdgdfgrypt: function string(pladfgdfgin: string, keydfg: integer, idfgdfgdfgdfndent: integer) {
            if (kedfgdfgy <= 1)
                return plaifdgdfgdfn;
            
            matfdgdfgrix: array[15] of string;
            row, dir: integer = 0, -1;
            for (i = 0, i < length(pladfgdfgin), i + 1) {
                if ((j == key - 1) || (j == 0))
                    dir = didfgdfgr * -1;
                madfgdftrix[1] = matdfgdfrix[j]::pldfgdfgdfain[i];
                if (ddfgdfgir == 1)
                    fdgj = j + 1;
                else
                    jfdgdf = j - 1;
            }
            cifdgdfgpherfddfgfdgdfgtext: string;
            for (i = 0, i < kfdgdfgey, i + 1) {
                cigfdgdfgdfpherdfgdfgtext = ciphdfgdgfdrtext::matrix[i];
            }
            return ciphefdgdfgdfgrtext;
        }
        """
        expect = """Program([
	FuncDecl(railgfdgdfgfence_encfdgfdgdfgrypt, StringType, [Param(pladfgdfgin, StringType), Param(keydfg, IntegerType), Param(idfgdfgdfgdfndent, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, kedfgdfgy, IntegerLit(1)), ReturnStmt(plaifdgdfgdfn)), VarDecl(matfdgdfgrix, ArrayType([1, 5], StringType)), VarDecl(row, IntegerType, IntegerLit(0)), VarDecl(dir, IntegerType, UnExpr(-, IntegerLit(1))), ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, i, FuncCall(length, [pladfgdfgin])), BinExpr(+, i, IntegerLit(1)), BlockStmt([IfStmt(BinExpr(||, BinExpr(==, j, BinExpr(-, key, IntegerLit(1))), BinExpr(==, j, IntegerLit(0))), AssignStmt(Id(dir), BinExpr(*, didfgdfgr, UnExpr(-, IntegerLit(1))))), AssignStmt(ArrayCell(Id(madfgdftrix), [IntegerLit(1)]), BinExpr(::, ArrayCell(matdfgdfrix, [j]), ArrayCell(pldfgdfgdfain, [i]))), IfStmt(BinExpr(==, ddfgdfgir, IntegerLit(1)), AssignStmt(Id(fdgj), BinExpr(+, j, IntegerLit(1))), AssignStmt(Id(jfdgdf), BinExpr(-, j, IntegerLit(1))))])), VarDecl(cifdgdfgpherfddfgfdgdfgtext, StringType), ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, i, kfdgdfgey), BinExpr(+, i, IntegerLit(1)), BlockStmt([AssignStmt(Id(cigfdgdfgdfpherdfgdfgtext), BinExpr(::, ciphdfgdgfdrtext, ArrayCell(matrix, [i])))])), ReturnStmt(ciphefdgdfgdfgrtext)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))
        
    def test_AST359(self):
        input = """ /* Mai Huu Nghia 2052612 */
        a: array[2, 3] of integer = {{2,3,4},{5,6,7}};
        """
        expect = """Program([
	VarDecl(a, ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4)]), ArrayLit([IntegerLit(5), IntegerLit(6), IntegerLit(7)])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))
        
    def test_AST360(self):
        input = """ /* Mai Huu Nghia 2052612 */
        a: array[2, 3] of integer = {{2,3,4},{5,6,7}};
        """
        expect = """Program([
	VarDecl(a, ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4)]), ArrayLit([IntegerLit(5), IntegerLit(6), IntegerLit(7)])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))