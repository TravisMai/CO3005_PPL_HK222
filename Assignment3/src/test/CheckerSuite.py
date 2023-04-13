import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_basicUndeclared_Identifier_Param(self):
        """Test basicUndeclared_Identifier_Param"""
        input = Program([
	FuncDecl("main", VoidType(), [], None, BlockStmt([]))
])
        #  """
        #     bds: function integer () {
        #         return a; 
        #     }
        #     main: function void () {
        # }"""
 
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 404))
        
    def test_basicUndeclared_Identsdfifier_Param(self):
        """Test basicUndeclared_Identifier_Param"""
        input = Program([
	VarDecl("x", AutoType),
	FuncDecl("main", VoidType(), [], None, BlockStmt([]))
])
        #  """
        #     bds: function integer () {
        #         return a; 
        #     }
        #     main: function void () {
        # }"""
 
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 404))