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
        
    def test_CS999(self):
        input = """
        x: integer = 3;
        foo: function void(x:float){}
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
            foo(1.3);
            
        }
        
        
        //x:auto = "3";"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 999))