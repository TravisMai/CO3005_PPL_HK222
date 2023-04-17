from Visitor import Visitor
from AST import *
from StaticError import *
from functools import *
from abc import ABC

# chưa xử lý xong các thể loại Array
# for funcall callfunction
# chưa xử lý phần check inherit (đã tạo phần check rồi nhưng chưa check)
# chưa xử lý phần inherit của param (hướng đi: truyền xuống tuple)
# chưa check inherit first statement


class MT22SupFunc:
    @staticmethod
    def insert_glo_func(scope):
        scope["readInteger"] = Glo_func(None, IntegerType())
        scope["printInteger"] = Glo_func(IntegerType(), VoidType())
        scope["readFloat"] = Glo_func(None, FloatType())
        scope["writeFloat"] = Glo_func(FloatType(), VoidType())
        scope["readBoolean"] = Glo_func(None, BooleanType())
        scope["printBoolean"] = Glo_func(BooleanType(), VoidType())
        scope["readString"] = Glo_func(None, StringType())
        scope["printString"] = Glo_func(StringType(), VoidType())
        scope["super"] = Glo_func(None, VoidType())
        scope["preventDefault"] = Glo_func(None, VoidType())

    @staticmethod
    def compare(typ1, typ2):
        if type(typ1) == ArrayType and type(typ2) == ArrayType:
            return typ1.dimensions == typ2.dimensions and MT22SupFunc.compare(typ1.typ, typ2.typ)
        elif type(typ1) == FloatType and type(typ2) == IntegerType:
            return True
        elif (type(typ2) in [IntegerType, FloatType, StringType, ArrayType, BooleanType]) and type(typ1) == AutoType:
            return True
        return type(typ1) == type(typ2)

    @staticmethod
    def return_type(type_util):
        if type(type_util) == Variable_op or type(type_util) == Function_op:
            return type_util.type
        else:
            return type_util

    # def coercion(typ1, typ2, inherit):
    #     if type(typ1) == FloatType and type(typ2) == IntegerType:
    #         return True
    #     elif (type(typ1) in [IntegerType, FloatType, StringType, ArrayType, VoidType]) and isinstance(typ2, FuncDecl) and type(typ2) == AutoType:
    #         return True
    #     elif (type(typ1) in [IntegerType, FloatType, StringType, ArrayType]) and isinstance(typ2, VarDecl) and type(typ2) == AutoType:
    #         return True
    #     elif isinstance(typ2, FuncDecl) and isinstance(typ1, FuncDecl):
    #         inheritFunc = inherit[typ1.name]
    #         while inheritFunc:
    #             if typ2.name == inheritFunc:
    #                 return True
    #             inheritFunc = inherit[inheritFunc]
    #     elif type(typ2) == ArrayType and type(typ1) == ArrayType:
    #         return typ1.dimensions == typ2.dimensions and MT22SupFunc.coercion(typ1.typ, typ2.typ, inherit)
    #     else:
    #         return False


class Function_op:
    def __init__(self, ftype: Type, inherit: str or None):
        self.type = ftype
        self.inherit = inherit
        self.parameter = {}


class Variable_op:
    def __init__(self, var_type: Type, var_init: Expr or None):
        self.type = var_type
        self.init = var_init


class Params_op:
    def __init__(self, typ: Type, out: bool = False, inherit: bool = False):
        self.typ = typ
        self.out = out
        self.inherit = inherit


class Glo_func:
    def __init__(self, input_typ: Type or None, return_typ: Type or None):
        self.itype = input_typ
        self.rtype = return_typ


class StaticChecker(Visitor):

    ########################## LOCAL PART OF CLASS ##########################

    def enter_loop(self):
        self.in_loop += 1

    def exit_loop(self):
        self.in_loop -= 1

    def enter_scope(self):
        self.local_index += 1

    def exit_scope(self):
        self.local_index -= 1

    def check(self):
        return self.visitProgram(self.ast, [])

    def __init__(self, ast):
        self.ast = ast
        self.funclist = {}
        self.varilist = {}
        self.glo_envi = {}
        self.func_flag = False
        self.for_flag = False
        self.current = None
        self.in_loop = 0
        self.local_index = 0

########################## EXPRESSO ##########################

    def visitBinExpr(self, ast: BinExpr, o):
        lhs = MT22SupFunc.return_type(self.visit(ast.left, o))
        rhs = MT22SupFunc.return_type(self.visit(ast.right, o))
        # print(lhs)
        # print(rhs)
        if ast.op in ["+", "-", "*", "/"]:
            if (type(lhs), type(rhs)) == (IntegerType, IntegerType):
                return FloatType() if ast.op == "/" else IntegerType()
            elif ((type(lhs), type(rhs)) == (FloatType, IntegerType)
                  or (type(lhs), type(rhs)) == (IntegerType, FloatType)
                  or (type(lhs), type(rhs)) == (FloatType, FloatType)):
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
            if ((type(lhs), type(rhs)) == (IntegerType, IntegerType)
                or (type(lhs), type(rhs)) == (FloatType, IntegerType)
                or (type(lhs), type(rhs)) == (IntegerType, FloatType)
                or (type(lhs), type(rhs)) == (FloatType, FloatType)
                or (((type(lhs), type(rhs)) == (IntegerType, IntegerType)
                     or (type(lhs), type(rhs)) == (BooleanType, BooleanType))
                    and (ast.op in ["==", "!="]))):
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ast)
        else:
            raise TypeMismatchInExpression(ast)

    def visitUnExpr(self, ast: UnExpr, o):
        val = MT22SupFunc.return_type(self.visit(ast.val, o))
        if ast.op == "-" and type(val) not in [IntegerType, FloatType]:
            raise TypeMismatchInExpression(ast)
        elif ast.op == "!" and type(val) != BooleanType:
            raise TypeMismatchInExpression(ast)
        else:
            return val

    def visitId(self, ast: Id, o):
        index = self.local_index
        if "local" not in o:
            if ast.name not in o["global"]:
                raise Undeclared(Identifier(), ast.name)

            return o["global"][ast.name]
        else:
            for i in range(index, -1, -1):
                if ast.name in o["local"][i]:
                    return o["local"][i][ast.name]

            if ast.name in o["global"]:
                return o["global"][ast.name]

            raise Undeclared(Identifier(), ast.name)

        # if "local" in o:
        #     index = self.local_index
        #     ids = list()
        #     for i in range(index, -1, -1):
        #         ids += list(filter(lambda x: x.name ==
        #                     ast.name, o["local"][i]))
        #     if len(ids) == 0:
        #         idss = list(filter(lambda x: x.name == ast.name, o["global"]))
        #         if len(idss) == 0:
        #             raise Undeclared(Identifier(), ast.name)
        #         return o["global"][ast.name]
        #     for i in range(index, -1, -1):
        #         if ast.name in o["local"][i]:
        #             return o["local"][i][ast.name]
        # else:
        #     ids = list(filter(lambda x: x.name == ast.name, o["global"]))
        #     if len(ids) == 0:
        #         raise Undeclared(Identifier(), ast.name)
        #     return o["global"][ast.name]

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

########################## STATEMENT ##########################

    def visitAssignStmt(self, ast: AssignStmt, o):
        # if type(ast.rhs) == CallStmt or type(ast.rhs) == ArrayCell:
        #     rhs = self.visit(ast.rhs, o)
        #     type_rhs = type(rhs)
        # else:
        #     rhs = ast.rhs.accept(self, o)
        #     type_rhs = rhs
        if self.for_flag is False:
            lhs = MT22SupFunc.return_type(self.visit(ast.lhs, o))
            rhs = MT22SupFunc.return_type(self.visit(ast.rhs, o))
            # type_lhs = lhs.type
            # type_rhs = lhs
            # print(ast.lhs)
            # print(ast.rhs)
            # print("\n")
            # print(lhs)
            # print(rhs)
            # print("\n")
            # print(type(lhs))
            # print(type(rhs))
            if type(lhs) == ArrayType:
                raise TypeMismatchInStatement(ast)
            elif (type(lhs) == AutoType) and (type(rhs) == AutoType):
                raise TypeMismatchInStatement(ast)
            elif (type(lhs) == AutoType) and (type(rhs) != AutoType):
                lhs = rhs
            elif (type(lhs) != AutoType) and (type(rhs) == AutoType):
                rhs = lhs
            elif (type(lhs) != AutoType) and (type(rhs) != AutoType):
                if (type(lhs) != type(rhs)) and (type(lhs) != FloatType) and (type(rhs) != IntegerType):
                    raise TypeMismatchInStatement(ast)
        else:
            rhs = MT22SupFunc.return_type(self.visit(ast.rhs, o))
            return rhs

    def visitBlockStmt(self, ast: BlockStmt, o):
        self.enter_scope()
        # print(index)
        # print(self.local_index)
        new_o_block = o.copy()
        new_o_block["local"][self.local_index] = {}
        for body in ast.body:
            self.visit(body, new_o_block)

        del new_o_block
        self.exit_scope()

    def visitIfStmt(self, ast: IfStmt, o):
        new_o_if = o.copy()
        condition = MT22SupFunc.return_type(self.visit(ast.cond, o))
        if type(condition) != BooleanType:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.tstmt, new_o_if)
        if ast.fstmt:
            self.visit(ast.fstmt, new_o_if)

        del new_o_if

    def visitForStmt(self, ast: ForStmt, o):
        self.enter_loop()
        self.for_flag = True
        new_o_for = o.copy()
        init = self.visit(ast.init, new_o_for)

        # phần cùa condition

        updt = self.visit(ast.upd, new_o_for)
        if type(updt) != IntegerType or type(init) != IntegerType:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.stmt, new_o_for)

        del new_o_for
        self.for_flag = False
        self.exit_loop()

    def visitWhileStmt(self, ast: WhileStmt, o):
        self.enter_loop()
        new_o_while = o.copy()
        condition = MT22SupFunc.return_type(self.visit(ast.cond, new_o_while))
        if type(condition) != BooleanType:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.stmt, new_o_while)
        del new_o_while
        self.exit_loop()

    def visitDoWhileStmt(self, ast, o):
        self.enter_loop()
        new_o_do_while = o.copy()
        condition = MT22SupFunc.return_type(
            self.visit(ast.cond, new_o_do_while))
        if type(condition) != BooleanType:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.stmt, new_o_do_while)
        del new_o_do_while
        self.exit_loop()

    def visitBreakStmt(self, ast: BreakStmt, o):
        if self.in_loop == 0:
            raise MustInLoop(ast)

    def visitContinueStmt(self, ast: ContinueStmt, o):
        if self.in_loop == 0:
            raise MustInLoop(ast)

    def visitReturnStmt(self, ast: ReturnStmt, o):
        new_o_return = o.copy()
        return_type = MT22SupFunc.return_type(self.visit(
            ast.expr, new_o_return)) if ast.expr else None
        if return_type is not None:
            if not MT22SupFunc.compare(o["global"][self.current].type, return_type):
                raise TypeMismatchInStatement(ast)

        del new_o_return

    def visitCallStmt(self, ast: CallStmt, o):
        if ast.name not in o["global"]:
            raise Undeclared(Function(), o)

        if len(o["global"][ast.name].parameter) != len(ast.args):
            raise TypeMismatchInStatement(ast)

        for param, value in zip(o["global"][ast.name].parameter.value(), ast.args):
            if type(param.typ) != type(value):
                raise TypeMismatchInStatement(ast)
        
        if type(o["global"][ast.name].type) is not (VoidType or AutoType):
            raise TypeMismatchInStatement(ast)


########################## DECL ##########################


    def visitVarDecl(self, ast: VarDecl, o):
        var_type = ast.typ
        var_init = self.visit(ast.init, o) if ast.init else None
        if self.func_flag == False:
            index = self.local_index
            # print(self.local_index)
            if "local" not in o:
                if ast.name in o["global"]:
                    raise Redeclared(Variable(), ast.name)
                if var_init is None and type(var_type) == AutoType:
                    raise Invalid(Variable(), ast.name)
                else:
                    # if type(var_type) == AutoType:
                    #     var_type = var_init
                    o["global"][ast.name] = Variable_op(var_type, var_init)
            else:
                if ast.name in o["local"][index]:
                    raise Redeclared(Variable(), ast.name)

                # for i in range(index, -1, -1):
                #     if ast.name in o["local"][i]:
                #         raise Redeclared(Variable(), ast.name)

                # if ast.name in o["global"]:
                #     raise Redeclared(Variable(), ast.name)

                if var_init is None and type(var_type) == AutoType:
                    raise Invalid(Variable(), ast.name)
                else:
                    # if type(var_type) == AutoType:
                    #     var_type = var_init
                    o["local"][index][ast.name] = Variable_op(
                        var_type, var_init)

            # if ast.typ is FloatType:
            #     # print("lmeoasdasdasd")
            # else: raise TypeMismatchInStatement(ast)
            # # print(var_type)
            # # print(var_init)
            # # print(o)
            if ast.init is not None:
                if not MT22SupFunc.compare(var_type, var_init):
                    # and not MT22SupFunc.coercion(var_type, var_init, self.funclist):
                    raise TypeMismatchInVarDecl(ast)
        else:
            if ast.name in o:
                raise Redeclared(Variable(), ast.name)

            o[ast.name] = Variable_op(var_type, var_init)

        # print(o)

    def visitParamDecl(self, ast: ParamDecl, o):
        # # print(o)
        if self.func_flag == False:
            if ast.name in o:
                # # print("dsadasd")
                raise Redeclared(Parameter(), ast.name)

            # # print(o)
            o[ast.name] = Params_op(ast.typ, ast.out, ast.inherit)
            # còn khúc check lỗi của params

        else:
            o[ast.name] = Params_op(ast.typ, ast.out, ast.inherit)
            # # print(o)

    def visitFuncDecl(self, ast: FuncDecl, o):
        if self.func_flag == False:
            if ast.name in o["global"]:
                raise Redeclared(Function(), ast.name)

            if ast.inherit is not None and ast.inherit not in self.funclist:
                raise Undeclared(Function(), ast.inherit)

            o["global"][ast.name] = Function_op(ast.return_type, ast.inherit)

            self.current = ast.name
            if ast.params != []:
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
            del new_o
            # # print("\ndictionary sau khi nhập xong function: ")
            # # print(new_o)

        else:
            if ast.name in o:
                raise Redeclared(Function(), ast.name)

            o[ast.name] = Function_op(ast.return_type, None)
            if ast.params != []:
                for params in ast.params:
                    self.visit(params, o[ast.name].parameter)

            # # print(o[ast.name].parameter)


########################## WHERE ITS START ##########################


    def visitProgram(self, ast: Program, o):
        o = {}
        o["global"] = {}
        MT22SupFunc.insert_glo_func(self.glo_envi)
        # print(self.glo_envi)
        has_main = False

        self.func_flag = True
        for i in ast.decls:
            # # print((o))
            if type(i) == FuncDecl:
                self.visit(i, self.funclist)
            elif type(i) == VarDecl:
                self.visit(i, self.varilist)

        self.func_flag = False
        for i in ast.decls:
            self.visit(i, o)
            if type(i) is FuncDecl and i.name == "main" and type(i.return_type) == VoidType and i.params == []:
                has_main = True

        # print("\ndictionary cua program sau khi nhập xong hết: ")
        print(o)
        if has_main == False:
            raise NoEntryPoint()
