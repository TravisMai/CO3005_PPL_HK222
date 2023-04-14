from Visitor import Visitor
from AST import *
from StaticError import *
from functools import *
from abc import ABC

# chưa xử lý phần nonlocal
# chưa xử lý phần auto type
# chưa xử lý ParamDecl
# chưa fix phần FuncDecl khúc truyền xuống variable + stmt
# và ra rả các thứ khác nhưng xử lý xong 3 cái trên r mới xử lý tiếp


class MT22SupFunc:
    @staticmethod
    def compare(typ1, typ2):
        if type(typ1) == ArrayType and type(typ2) == ArrayType:
            return typ1.dimensions == typ2.dimensions and MT22SupFunc.compare(typ1.typ, typ2.typ)
        elif type(typ1) == FloatType and type(typ2) == IntegerType:
            return True
        return type(typ1) == type(typ2)

    def coercion(typ1, typ2, inherit):
        if type(typ1) == FloatType and type(typ2) == IntegerType:
            return True
        elif (type(typ1) in [IntegerType, FloatType, StringType, ArrayType, VoidType]) and isinstance(typ2, FuncDecl) and type(typ2) == AutoType:
            return True
        elif (type(typ1) in [IntegerType, FloatType, StringType, ArrayType]) and isinstance(typ2, VarDecl) and type(typ2) == AutoType:
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
    parameter = {}
    
    def __init__(self, ftype: Type, inherit: str or None):
        self.type = ftype
        self.inherit = inherit

class Variable_op:
    def __init__(self, var_type: Type, var_init: Expr or None):
        self.type = var_type
        self.init = var_init

class Params_op:
    def __init__(self, typ: Type, out: bool = False, inherit: bool = False):
        self.typ = typ
        self.out = out
        self.inherit = inherit


class StaticChecker(Visitor):
    func_flag = False
    loop_flag = False
    local_index = 0
 
    def check(self):
        return self.visitProgram(self.ast, [])
    
    def __init__(self, ast):
        self.ast = ast
        self.inheritance = {}
        self.current = None

    def visitBinExpr(self, ast: BinExpr, o):
        lhs = self.visit(ast.left, o)
        rhs = self.visit(ast.right, o)
        if ast.op in ["+", "-", "*", "/"]:
            if (type(lhs), type(rhs)) == (IntegerType, IntegerType):
                return FloatType() if ast.op == "/" else IntegerType()
            elif (type(lhs), type(rhs)) == (FloatType, IntegerType) or (type(lhs), type(rhs)) == (IntegerType, FloatType) or (type(lhs), type(rhs)) == (FloatType, FloatType):
                return FloatType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op == "%":
            if (type(lhs), type(rhs)) == (IntegerType, IntegerType):
                return IntegerType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op in ["&&", "||"]:
            if (type(lhs), type(rhs)) == (BooleanType, BooleanType):
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op == "::":
            if (type(lhs), type(rhs)) == (StringType, StringType):
                return StringType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op in ["==", "!=", "<", ">", "<=", ">="]:
            if (type(lhs), type(rhs)) == (IntegerType, IntegerType) or (type(lhs), type(rhs)) == (FloatType, IntegerType) or (type(lhs), type(rhs)) == (IntegerType, FloatType) or (type(lhs), type(rhs)) == (FloatType, FloatType) or (((type(lhs), type(rhs)) == (IntegerType, IntegerType) or (type(lhs), type(rhs)) == (BooleanType, BooleanType)) and (ast.op in ["==", "!="])):
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ast)
        else:
            raise TypeMismatchInExpression(ast)

    def visitUnExpr(self, ast: UnExpr, o):
        val = self.visit(ast.val, o)
        if ast.op == "-" and type(val) not in [IntegerType, FloatType]:
            raise TypeMismatchInExpression(ast)
        elif ast.op == "!" and type(val) != BooleanType:
            raise TypeMismatchInExpression(ast)
        else:
            return val

    def visitId(self, ast: Id, o):
        if "local" in o:
            index = self.local_index
            ids = list()
            for i in range(index, -1, -1):
                ids += list(filter(lambda x: x.name ==
                            ast.name, o["local"][i]))
            if len(ids) == 0:
                idss = list(filter(lambda x: x.name == ast.name, o["global"]))
                if len(idss) == 0:
                    raise Undeclared(Identifier(), ast.name)
                return o["global"][ast.name]
            for i in range(index, -1, -1):
                if ast.name in o["local"][i]:
                    return o["local"][i][ast.name]
        else:
            ids = list(filter(lambda x: x.name == ast.name, o["global"]))
            if len(ids) == 0:
                raise Undeclared(Identifier(), ast.name)
            return o["global"][ast.name]

    def visitArrayCell(self, ast: ArrayCell, o):
        if "local" in o:
            index = self.local_index
            ids = list()
            for i in range(index, -1, -1):
                ids += list(filter(lambda x: x.name ==
                            ast.name, o["local"][i]))
            if len(ids) == 0:
                idss = list(filter(lambda x: x.name == ast.name, o["global"]))
                if len(idss) == 0:
                    raise Undeclared(Identifier(), ast.name)
                arr = o["global"][ast.name]
            else:
                for i in range(index, -1, -1):
                    if ast.name in o["local"][i]:
                        arr = o["local"][i][ast.name]
        else:
            ids = list(filter(lambda x: x.name == ast.name, o["global"]))
            if len(ids) == 0:
                raise Undeclared(Identifier(), ast.name)
            arr = o["global"][ast.name]

        if type(arr.type) != ArrayType:
            raise TypeMismatchInExpression(ast)

        for cell in ast.cell:
            espresso = self.visit(cell, o)
            if type(espresso) != IntegerType:
                raise TypeMismatchInExpression(ast)
        return arr

    def visitIntegerLit(self, ast: IntegerLit, o):
        return IntegerType()

    def visitFloatLit(self, ast: FloatLit, o):
        return FloatType()

    def visitStringLit(self, ast: StringLit, o):
        return StringType()

    def visitBooleanLit(self, ast: BooleanLit, o):
        return BooleanType()

    def visitArrayLit(self, ast: ArrayLit, o):
        type_of_array_list = [self.visit(explist, o)
                              for explist in ast.explist]
        for type_of_array_element in type_of_array_list:
            if not MT22SupFunc.compare(type_of_array_element, type_of_array_element[0]):
                raise IllegalArrayLiteral(ast)
        return ArrayType([], type(type_of_array_element[0]))

    def visitFuncCall(self, ast, o): pass

    def visitAssignStmt(self, ast: AssignStmt, o):
        if type(ast.rhs) == CallStmt or type(ast.rhs) == ArrayCell:
            rhs = self.visit(ast.rhs, o)
            type_rhs = type(rhs)
        else:
            rhs = ast.rhs.accept(self, o)
            type_rhs = rhs.type

        lhs = self.visit(ast.lhs, o)
        type_lhs = rhs.type

        if type_lhs == ArrayType:
            raise TypeMismatchInStatement(ast)
        elif (type_lhs == AutoType) and (type_rhs == AutoType):
            raise TypeMismatchInStatement(ast)
        elif (type_lhs == AutoType) and (type_rhs != AutoType):
            lhs.type = rhs.type
        elif (type_lhs != AutoType) and (type_rhs == AutoType):
            rhs.type = lhs.type
        elif (type_lhs != AutoType) and (type_rhs != AutoType):
            if type_lhs != type_rhs:
                raise TypeMismatchInStatement(ast)

    def visitBlockStmt(self, ast, o): pass
    def visitIfStmt(self, ast, o): pass
    def visitForStmt(self, ast: ForStmt, o): pass
    def visitWhileStmt(self, ast, o): pass
    def visitDoWhileStmt(self, ast, o): pass
    def visitBreakStmt(self, ast, o): pass
    def visitContinueStmt(self, ast, o): pass
    def visitReturnStmt(self, ast, o): pass

    def visitCallStmt(self, ast: CallStmt, o): pass

    def visitVarDecl(self, ast: VarDecl, o):
        # print(ast.init)
        # print(type(self.visit(ast.init, o)))
        var_type = ast.typ
        var_init = self.visit(ast.init, o) if ast.init else None
        index = self.local_index
        if "local" not in o:
            if ast.name in o["global"]:
                raise Redeclared(Variable(), ast.name)
            if var_init is None and type(var_type) == AutoType:
                raise Invalid(Variable(), ast.name)
            else:
                o["global"][ast.name] = Variable_op(var_type, var_init)
        else:
            # for i in range(index, -1, -1):
            #     ids = list(filter(lambda x: x.name == ast.name, o["local"][i]))
            #     if len(ids) > 0: 
            #         raise Redeclared(Variable(), ast.name)
                
            ids = list()
            for i in range(index, -1, -1):
                ids += list(filter(lambda x: x.name ==
                            ast.name, o["local"][i]))
            if len(ids) > 0:
                idss = list(filter(lambda x: x.name == ast.name, o["global"]))
                if len(idss) > 0:
                    raise Redeclared(Variable(), ast.name)
                
            if var_init is None and type(var_type) == AutoType:
                raise Invalid(Variable(), ast.name)
            else:
                o["local"][index][ast.name] = Variable_op(var_type, var_init)

        # if ast.typ is FloatType:
        #     print("lmeoasdasdasd")
        # else: raise TypeMismatchInStatement(ast)
        if ast.init is not None:
            if not MT22SupFunc.compare(var_type, var_init) and not MT22SupFunc.coercion(var_init, var_type, self.inheritance):
                raise TypeMismatchInStatement(ast)

    def visitParamDecl(self, ast: ParamDecl, o):
        if self.func_flag == False:
            if ast.name in o:
                raise Redeclared(Parameter(), ast.name)
            
            o[ast.name] = Params_op(ast.typ,ast.out,ast.inherit)
            # còn khúc check lỗi của params
            
        else:
            o[ast.name] = Params_op(ast.typ,ast.out,ast.inherit)

    def visitFuncDecl(self, ast: FuncDecl, o):
        if self.func_flag == False:
            if ast.name in o["global"]:
                raise Redeclared(Function(), ast.name)
            
            if ast.inherit is not None and ast.inherit not in o["inherit"]:
                raise Undeclared(Function(), ast.inherit)
            
            o["global"][ast.name] = Function_op(ast.return_type, ast.inherit)
            
            for params in ast.params:
                self.visit(params, o["global"][ast.name].parameter)
                
            self.local_index = 0
            new_o = o.copy()
            new_o["local"] = {}
            new_o["local"][0] = {}
            for body in ast.body.body:
                if type(body) is ReturnStmt:  # cần fix khúc này để check return type của function
                    self.visit(body, new_o)
                else:
                    self.visit(body, new_o)

            self.current = None
        else:
            if ast.name in o:
                raise Redeclared(Function(), ast.name)
            
            o[ast.name] = Function_op(ast.return_type, None)
            for params in ast.params:
                self.visit(params, o[ast.name].parameter)

    def visitProgram(self, ast: Program, o):
        o = {}
        o["global"] = {}
        o["inherit"] = {}
        self.loop_flag = False
        self.local_index = 0
        has_main = False
        
        self.func_flag =  True
        for i in ast.decls:
            print(type(i))
            if type(i) == FuncDecl:
                self.visit(i, o["inherit"])
            
        self.func_flag = False        
        for i in ast.decls:
            self.visit(i, o)
            if type(i) is FuncDecl and i.name == "main":
                has_main = True
        if has_main == False:
            raise NoEntryPoint()
