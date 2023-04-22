import unittest
from TestUtils import TestChecker, TestAST
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_SC400(self):
        input = Program([
            FuncDecl("main", VoidType(), [], None, BlockStmt([]))
        ])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_SC401(self):
        input = Program([
            VarDecl("x", AutoType()),
            FuncDecl("main", VoidType(), [], None, BlockStmt([]))
        ])
        expect = "Invalid Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_SC402(self):
        input = Program([
            VarDecl("x", IntegerType(), IntegerLit(1)),
            FuncDecl("main", VoidType(), [], None, BlockStmt([]))
        ])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_SC403(self):
        input = Program([
            VarDecl("x", IntegerType(), IntegerLit(1))
        ])
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_SC404(self):
        input = """
        foo: function void() inherit ain{
            super(14);        
        }
        ain:function void (inherit y: auto) {
            f: array[3] of float;
            f[4.3] = 1;
        }"""
        expect = "Type mismatch in expression: ArrayCell(f, [FloatLit(4.3)])"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_SC405(self):
        input = Program([VarDecl("a", IntegerType()),
                        VarDecl("c", FloatType())])
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_SC406(self):
        input = """
        foo: function void() inherit ain{
            super(14);        
        }
        ain:function void (inherit y: auto) {
            f: array[3] of float;
        }"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_SC407(self):
        input = """
        foo: function void() inherit ain{
            super(14);        
        }
        ain:function void (inherit y: auto) {
            f: array[3] of float;
        }
        main: function float(){        
        }"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_SC408(self):
        input = """
        foo: function void() inherit ain{
            super(14);        
        }
        ain:function void (inherit y: auto) {
            f: array[3] of float;
        }
        main: function void(x: auto){        
        }"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_SC409(self):
        input = """
        foo: function void() inherit ain{
            super(14);        
        }
        ain:function void (inherit y: auto) {
            f: array[3] of float;
        }
        main: function void(){        
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_SC410(self):
        input = """
        foo: function void() inherit ain{
            super(14,1);        
        }
        ain:function void (inherit y: auto) {
            f: array[3] of float;
        }
        main: function auto(){        
        }"""
        expect = "Type mismatch in expression: IntegerLit(1)"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_SC411(self):
        input = """
        foo: function void() inherit ain{
            super(1);        
        }
        ain:function void ( y: integer) {
            f: array[3] of float;
        }
        main: function auto(){        
        }"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_SC412(self):
        input = """
        foo: function void(){
            super(1);        
        }
        ain:function void (inherit y: float, inherit y: integer) {
            f: array[3] of float;
        }
        main: function void(){        
        }"""
        expect = "Type mismatch in statement: CallStmt(super, IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_SC413(self):
        input = """
        foo: function void(){
            in(1.2, 1);        
        }
        ain:function void (inherit y: float, inherit y: integer) {
            f: array[3] of float;
        }
        main: function void(){        
        }"""
        expect = "Undeclared Function: in"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_SC414(self):
        input = """
        foo: function void(){
            ain(1.2, 1, "");        
        }
        ain:function void (inherit x: float, inherit y: integer) {
            f: array[3] of float;
        }
        main: function void(){        
        }"""
        expect = "Type mismatch in statement: CallStmt(ain, FloatLit(1.2), IntegerLit(1), StringLit())"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_SC415(self):
        input = """
        main: function void(){
            f: array[5] of integer = {1,2,3,4};        
        }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(f, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]))"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_SC416(self):
        input = """
        foo: function void() inherit ain{
            super(1);
        }
        ain:function void (inherit y: float, inherit y: integer) {
            f: array[3] of float;
        }
        main: function void(){
        }"""
        expect = "Redeclared Parameter: y"
        self.assertTrue(TestChecker.test(input, expect, 416))
        
    def test_SC417(self):
        input = """
        main: function void(){
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of integer = {{{1,2,3},{4,5,6}}};
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 417))
    
    def test_SC418(self):
        input = """
        main: function void(){
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of integer = {{{1,2},{4,5,6}}};
        }"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)])])])"
        self.assertTrue(TestChecker.test(input, expect, 418))
        
    def test_SC419(self):
        input = """
        main: function void(){
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of integer = {{{1,2,"34"},{4,5,6}}};
        }"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), StringLit(34)]), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)])])])"
        self.assertTrue(TestChecker.test(input, expect, 419))
        
    def test_SC420(self):
        input = """
        main: function void(){
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6","7"}}};
        }"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([ArrayLit([StringLit(1), StringLit(2), StringLit(34)]), ArrayLit([StringLit(4), StringLit(5), StringLit(6), StringLit(7)])])])"
        self.assertTrue(TestChecker.test(input, expect, 420))
        
    def test_SC421(self):
        input = """
        x: integer = 1;
        main: function void(){
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
            g[1,2,2] = "1";
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 421))
        
    def test_SC422(self):
        input = """
        x: integer = 1;
        main: function void(){
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
            g[x,e,r] = "1";
        }"""
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input, expect, 422))
        
    def test_SC423(self):
        input = """
        x: integer = 1;
        main: function void(){
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
            g[x,f,r] = "1";
        }"""
        expect = "Type mismatch in expression: ArrayCell(g, [Id(x), Id(f), Id(r)])"
        self.assertTrue(TestChecker.test(input, expect, 423))
        
    def test_SC424(self):
        input = """
        x: integer = 1;
        main: function void(){
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
            g[x,1] = "1";
        }"""
        expect = "Type mismatch in statement: AssignStmt(ArrayCell(g, [Id(x), IntegerLit(1)]), StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 424))
        
    def test_SC425(self):
        input = """
        x: integer = 1;
        main: function void() inherit foo{
            super(10);
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
            g[x,1,x] = "1";            
        }
        foo: function float(inherit x: float){}"""
        expect = "Type mismatch in expression: ArrayCell(g, [Id(x), IntegerLit(1), Id(x)])"
        self.assertTrue(TestChecker.test(input, expect, 425))
        
    def test_SC426(self):
        input = """
        x: integer = 1;
        main: function void() inherit foo{
            preventDefault();
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
            g[x,1,x] = "1";            
        }
        foo: function float(inherit x: float){}"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 426))
    
    def test_SC427(self):
        input = """
        x: integer = 1;
        main: function void() inherit foo{
            //preventDefault();
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
            g[x,1,x] = "1";            
        }
        foo: function float(inherit x: float){}"""
        expect = "Invalid statement in function: main"
        self.assertTrue(TestChecker.test(input, expect, 427))
        
    def test_SC428(self):
        input = """
        x: integer = 1;
        main: function void() inherit foo{
            //preventDefault();
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
            g[x,1,x] = "1";            
        }
        foo: function float(){}"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 428))
        
    def test_SC429(self):
        input = """
        x: integer = 1;
        main: function void() inherit foo{
            super("!");
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
        }
        foo: function float(inherit x: float){}"""
        expect = "Type mismatch in expression: StringLit(!)"
        self.assertTrue(TestChecker.test(input, expect, 429))
        
    def test_SC430(self):
        input = """
        x: string = "1";
        main: function void() inherit foo{
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
            if (x == "1") x = 1;            
        }
        foo: function float(){}"""
        expect = "Type mismatch in expression: BinExpr(==, Id(x), StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 430))
        
    def test_SC431(self):
        input = """
        x: integer = 1;
        main: function void() inherit foo{
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of integer = {{{"1","2","34"},{"4","5","6"}}};            
        }
        foo: function float(){}"""
        expect = "Type mismatch in Variable Declaration: VarDecl(g, ArrayType([1, 2, 3], IntegerType), ArrayLit([ArrayLit([ArrayLit([StringLit(1), StringLit(2), StringLit(34)]), ArrayLit([StringLit(4), StringLit(5), StringLit(6)])])]))"
        self.assertTrue(TestChecker.test(input, expect, 431))
        
    def test_SC432(self):
        input = """
        x: integer = 1;
        main: function void() inherit foo{
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of integer = {{{1,2,3},{4,3,2}}};
            if (x >= 1) x = 1;            
        }
        foo: function float(){}"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 432))
        
    def test_SC432(self):
        input = """
        x: string = "1";
        main: function void() inherit foo{
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
            if (x :: "1") x = 1;            
        }
        foo: function float(){}"""
        expect = "Type mismatch in statement: IfStmt(BinExpr(::, Id(x), StringLit(1)), AssignStmt(Id(x), IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 432))
        
    def test_SC433(self):
        input = """
        x: string = "1";
        main: function void() inherit foo{
            preventDefault(1);
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
            if (x :: "1") x = 1;
        }
        foo: function float(){}"""
        expect = "Type mismatch in expression: IntegerLit(1)"
        self.assertTrue(TestChecker.test(input, expect, 433))
        
    def test_SC434(self):
        input = """
        x: boolean;
        main: function void() inherit foo{
            super(1);
            f: array[5] of integer = {1,2,3,4,5};
            if (!x) x = !x;            
        }
        foo: function float(x: integer){
            main(1);
        }"""
        expect = "Type mismatch in statement: CallStmt(main, IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 434))
        
    def test_SC435(self):
        input = """
        x: boolean;
        main: function void() inherit foo{
            super(1);
            f: array[5] of integer = {1,2,3,4,5};
            if (!x) x = !x;            
        }
        foo: function float(x: integer){
            main();
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 435))
        
    def test_SC436(self):
        input = """
        x: boolean;
        main: function void() inherit foo{
            super(1);
            f: array[5] of integer = {1,2,3,4,5};
            if (!x) x = !x;            
        }
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            do{
                printInteger(x);
            } while (bar() > 0);
        }"""
        expect = "Undeclared Function: bar"
        self.assertTrue(TestChecker.test(input, expect, 436))
        
    def test_SC437(self):
        input = """
        x: boolean;
        main: function void() inherit foo{
            super(1);
            f: array[5] of integer = {1,2,3,4,5};
            if (!x) x = !x;            
        }
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            do{
                printInteger(x);
            } while (boo()/10*345.6+4 > 0);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 437))
        
    def test_SC438(self):
        input = """
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            do{
                x = printInteger();
            } while (boo()/10*345.6+4 > 0);
        }"""
        expect = "Type mismatch in expression: FuncCall(printInteger, [])"
        self.assertTrue(TestChecker.test(input, expect, 438))
        
    def test_SC439(self):
        input = """
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            do{
                x = boo();
            } while (boo()/10*345.6+4 > 0);
        }"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 439))
        
    def test_SC440(self):
        input = """
        pool: function void() inherit foo{}
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            for (i = 0, i < 10, i + 1){
                pool();
                i = pool();
            }
        }"""
        expect = "Invalid statement in function: pool"
        self.assertTrue(TestChecker.test(input, expect, 440))
        
    def test_SC441(self):
        input = """
        pool: function void() inherit foo{super(1);}
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            i: integer;
            for (i = -0, i < 10, i + 1){
                pool(1);
            }
        }"""
        expect = "Type mismatch in statement: CallStmt(pool, IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 441))
    
    def test_SC442(self):
        input = """
        pool: function void() inherit foo{super(1);}
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            i: integer;
            for (i = -0, i < 10, i + 1){
                i = pool();
            }
        }"""
        expect = "Type mismatch in statement: AssignStmt(Id(i), FuncCall(pool, []))"
        self.assertTrue(TestChecker.test(input, expect, 442))
        
    def test_SC443(self):
        input = """
        pool: function void() inherit foo{super(1);}
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            i: integer;
            for (i = -0, i != -10, i == 1){
                i = pool();
            }
        }"""
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), UnExpr(-, IntegerLit(0))), BinExpr(!=, Id(i), UnExpr(-, IntegerLit(10))), BinExpr(==, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(i), FuncCall(pool, []))]))"
        self.assertTrue(TestChecker.test(input, expect, 443))
        
    def test_SC444(self):
        input = """
        pool: function void() inherit foo{super(1);}
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            while ( x < 10) return x+1;
        }"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 444))
        
    def test_SC445(self):
        input = """
        pool: function void() inherit foo{
            super(1);
            while(boo()>0) continue;
        }
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            while ( x < 10) break;
        }"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 445))
        
    def test_SC446(self):
        input = """
        pool: function void() inherit foo{
            super(1);
            while(boo()>0) continue;
        }
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            break;
        }"""
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 447))
        
    def test_SC447(self):
        input = """
        pool: function void() inherit foo{
            super(1);
            continue;
        }
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            break;
        }"""
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 447))
        
    def test_SC448(self):
        input = """
        pool: function void() inherit foo{
            super(1);
        }
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            return "";
        }"""
        expect = "Type mismatch in statement: ReturnStmt(StringLit())"
        self.assertTrue(TestChecker.test(input, expect, 448))
        
    def test_SC449(self):
        input = """
        pool: function void() inherit foo{
            super(1);
        }
        boo: function integer(){
            return 1;
        }
        foo: function float(x: integer){
            if(x == 1) return 1;
            return "";
            return "ashjdgkf";
        }"""
        expect = "Type mismatch in statement: ReturnStmt(StringLit())"
        self.assertTrue(TestChecker.test(input, expect, 449))
        
    def test_SC450(self):
        input = """
        f:array[1,2,3] of float;
        g: array[1,2,3] of integer = f;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(g, ArrayType([1, 2, 3], IntegerType), Id(f))"
        self.assertTrue(TestChecker.test(input, expect, 450))
        
    def test_SC451(self):
        input = """
        f:array[1,2,3] of integer;
        g: array[1,2,3] of float = f;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 451))
        
    def test_SC452(self):
        input = """
        x: integer = 3;
        foo1: function void( x:float,inherit y: string){}
        foo2: function auto(){return 2.3;}
        main:function void () {
            n: integer;
            x,y,z: float;
            {
                {

                }
                x = n;
            }
            if((x<y) && (y < 9) && (z != 10)) z = 456;
            else z = 34576;
            foo1(2.3,"abc");
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 452))
        
    def test_SC453(self):
        input = """
        main:function void () {}
        poo: function void(n: auto) {
            n = 1;
            if(n>0) n = n + 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 453))
    
    def test_SC454(self):
        input = """
        poo: function auto(n: auto) {
            n = 1;
            if(n>0) n = n + 1;
        }
        main:function void () {
            x: integer = 1;
            x = poo(1);
            
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 454))
        
    def test_SC455(self):
        input = """
        main:function void () {
            x: integer = 1;
            x = poo(1);
            
        }
        poo: function auto(n: auto) {
            //n = 1;
            if(n>0) n = n + 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 455))
    
    def test_SC456(self):
        input = """
        main:function void () {
            x: integer = 1;
            x = poo(1);
            
        }
        poo: function auto(n: auto) {
            //n = 1;
            if(n>0) n = n + 1;
        }
        boo: function void(){
            if (poo("1") < 10){
                printInteger(poo(1));
            }
        }
        """
        expect = "Type mismatch in expression: FuncCall(poo, [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 456))
    
    def test_SC457(self):
        input = """
        main:function void () {
            x: integer = 1;
            hehe(poo(""),"");
        }
        hehe: function float(x: integer, y : string){}
        poo: function auto(n: auto) {
            //n = 1;
            if(n>0) n = n + 1;
        }
        boo: function void(){
            if (poo("1") < 10){
                printInteger(poo(1));
            }
        }
        """
        expect = "Type mismatch in expression: BinExpr(>, Id(n), IntegerLit(0))"
        self.assertTrue(TestChecker.test(input, expect, 457))
        
    def test_SC458(self):
        input = """
        main:function void () {
        }
        hehe: function float(x: integer, y : string){
            x = 1;
            
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 458))
        
    def test_SC459(self):
        input = """
        main:function void () {
        }
        hehe: function float(inherit x: integer, y : string) inherit aaa{
            super(3);
            b = 1;
        }
        aaa: function float(inherit a: integer) inherit bbb{
            super(2,1);
            b = 1;
        }
        bbb: function float(inherit b: integer, inherit c: float){
            
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 999))
        
        
    # def test_SC999(self):
    #     input = """/*
        
    #     x: auto = foo2(2);
    #     //foo1: function void( x:float,inherit y: string){}
    #     foo2: function integer(b:auto){}
    #     foo:function void(t: integer, q : float){
    #         //super(1.2 , "12");
    #         r: float = 3.2;
    #         //r = foo2(r);
    #         r = readFloat();
    #         f: array[3,2,1] of integer = {{{3}, {1}}, {{3}, {1}}, {{4}, {5}}};
    #         //y = "1";

    #         //x = readInteger();
    #     }
    #     main:function void () {
    #         foo(1,1.2);
    #     }"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 999))
