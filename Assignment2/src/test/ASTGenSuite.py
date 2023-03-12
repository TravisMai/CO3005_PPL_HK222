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