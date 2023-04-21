import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
#     def test_CS400(self):
#         input = Program([
#  	FuncDecl("main", VoidType(), [], None, BlockStmt([]))
# ])
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 400))
        
#     def test_CS401(self):
#         input = Program([
# 	VarDecl("x", AutoType()),
# 	FuncDecl("main", VoidType(), [], None, BlockStmt([]))
# ])
#         expect = "Invalid Variable: x"
#         self.assertTrue(TestChecker.test(input, expect, 401))
        
#     def test_CS402(self):
#         input = Program([
# 	VarDecl("x", IntegerType(), IntegerLit(1)),
# 	FuncDecl("main", VoidType(), [], None, BlockStmt([]))
# ])
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 402))
        
#     def test_CS403(self):
#         input = Program([
# 	VarDecl("x", IntegerType(), IntegerLit(1))
# ])
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 403))
        
    # def test_CS999(self):
    #     input = """/*
    #     x: integer = 3;
    #     //foo1: function void( x:float,inherit y: string){}
    #     foo2: function auto(){return 2.3;}
    #     main:function void () {
    #         n: integer;
    #         x,y,z: float;
    #         {
    #             {
                    
    #             }
    #             x = n;
    #         }
    #         if((x<y) && (y < 9) && (z != 10)) z = 456;
    #         else z = 34576;
    #         foo1(2.3,"abc");
            
    #     }*/
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
    
    def test_CS999(self):
        input = """
        main:function void () {
            f: array[3] of float;
            f[4.3] = 1;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 999))