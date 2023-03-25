from Visitor import Visitor
from AST import *
from StaticError import *
from functools import *


class MT22SupFunc:
    @staticmethod
    def compare(typ1, typ2):
        if type(typ1) == ArrayType and type(typ2) == ArrayType:
            return typ1.dimensions == typ2.dimensions and MT22SupFunc.compare(typ1.typ, typ2.typ)
        return type(typ1) == type(typ2)

    def coercion(typ1, typ2, inherit):
        if type(typ1) == FloatType and type(typ2) == IntegerType:
            return True
        elif (type(typ1) == IntegerType
              or type(typ1) == FloatType
              or type(typ1) == StringType
              or type(typ1) == ArrayType
              or type(typ1) == VoidType) and isinstance(typ2, FuncDecl) and type(typ2) == AutoType:
            return True
        elif (type(typ1) == IntegerType
              or type(typ1) == FloatType
              or type(typ1) == StringType
              or type(typ1) == ArrayType) and isinstance(typ2, VarDecl) and type(typ2) == AutoType:
            return True
        elif isinstance(typ2, FuncDecl) and isinstance(typ1, FuncDecl):
            inheritFunc = inherit[typ1.name]
            while inheritFunc:
                if typ2.name == inheritFunc:
                    return True
                inheritFunc = inherit[inheritFunc]
        elif type(typ2) == ArrayType and type(typ1) == ArrayType:
            return typ1.dimensions == typ2.dimensions and MT22SupFunc.coercion(typ1.typ, typ2.typ, inherit)
        else:
            return False


class Function_op:
    def __init__(self):
        self.variable = {}
        self.statement = {}
        self.parameter = {}


class Variable_op:
    def __init__(self):
        self.type = None
        self.init = None

    def insertVarValue(self, var_type, var_init):
        self.type = var_type
        self.init = var_init


class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast
        self.inheritance = {}
        self.current = None
        self.in_loop = False

    def visitBinExpr(self, ast, o): pass
    def visitUnExpr(self, ast, o): pass

    def visitId(self, ast: Id, o):
        if "local" in o:
            ids = list(filter(lambda x: x.name == ast.name, o["local"]))
            if len(ids) == 0:
                ids = list(filter(lambda x: x.name == ast.name, o["global"]))
                if len(ids) == 0:
                    raise Undeclared(Identifier(), ast.name)
        else:
            ids = list(filter(lambda x: x.name == ast.name, o["global"]))
            if len(ids) == 0:
                raise Undeclared(Identifier(), ast.name)

    def visitArrayCell(self, ast, o): pass

    def visitIntegerLit(self, ast: IntegerType, o):
        return IntegerType()

    def visitFloatLit(self, ast: FloatType, o):
        return FloatType()

    def visitStringLit(self, ast: StringType, o):
        return StringType()

    def visitBooleanLit(self, ast: BooleanType, o):
        return BooleanType()

    def visitArrayLit(self, ast: ArrayLit, o):
        type_of_array_list = [self.visit(explist, o)
                              for explist in ast.explist]
        for type_of_array_element in type_of_array_list:
            if not MT22SupFunc.compare(type_of_array_element, type_of_array_element[0]):
                raise IllegalArrayLiteral(ast)
        return ArrayType([], type(type_of_array_element[0]))

    def visitFuncCall(self, ast, o): pass

    def visitAssignStmt(self, ast, o): pass
    def visitBlockStmt(self, ast, o): pass
    def visitIfStmt(self, ast, o): pass

    def visitForStmt(self, ast: ForStmt, o):
        self.in_loop = True

        self.in_loop = False

    def visitWhileStmt(self, ast, o): pass
    def visitDoWhileStmt(self, ast, o): pass
    def visitBreakStmt(self, ast, o): pass
    def visitContinueStmt(self, ast, o): pass
    def visitReturnStmt(self, ast, o): pass

    def visitCallStmt(self, ast: CallStmt, o):
        call_name = ast.name

    def visitVarDecl(self, ast: VarDecl, o):
        var_type = self.visit(ast.typ, o)
        if ast.init != None:
            var_init = self.visit(ast.init, o)
        else:
            var_init = None
        if "local" not in o:
            if ast.name in o["global"]:
                raise Redeclared(Variable(), ast.name)
            o["global"][ast.name] = Variable_op()
            o["global"][ast.name].insertVarValue(var_type, var_init)
        else:
            if ast.name in o["local"]:
                raise Redeclared(Variable(), ast.name)
            o["local"][ast.name] = Variable_op()
            o["local"][ast.name].insertVarValue(var_type, var_init)

        if ast.init != None:
            if not MT22SupFunc.compare(var_init, var_type) and not MT22SupFunc.coercion(var_init, var_type, self.inheritance):
                raise TypeMismatchInStatement(ast)

    def visitParamDecl(self, ast, o): pass

    def visitFuncDecl(self, ast: FuncDecl, o):
        if ast.name in o["global"]:
            raise Redeclared(Function(), ast.name)
        o["global"][ast.name] = Function_op()
        self.current = ast.name
        if ast.inherit != None:
            if ast.inherit not in o["global"]:
                raise Undeclared(Function(), ast.inherit)
            self.inheritance[ast.name] = ast.inherit
        else:
            self.inheritance[ast.name] = None

        new_o = o.copy()
        new_o["local"] = [{}]
        for body in ast.body.body:
            if isinstance(body, VarDecl):
                self.visit(body, (Variable(), new_o))
            elif isinstance(body, Stmt):
                self.visit(body, (Stmt(), new_o))

        self.current = None

    def visitProgram(self, ast: Program, o):
        o = {}
        o["global"] = {}
        has_main = False
        for i in ast.decls:
            self.visit(i, o)
            if type(i) == FuncDecl and i.name == "main":
                has_main = True
        if has_main == False:
            raise NoEntryPoint()
