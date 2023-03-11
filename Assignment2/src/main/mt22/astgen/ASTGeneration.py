from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *
from functools import *


class ASTGeneration(MT22Visitor):
    # program: declares EOF;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.declares()))

    # declares: declare declares | declare;
    def visitDeclares (self, ctx:MT22Parser.DeclaresContext):
        if ctx.declares():
            return list(self.visit(ctx.declare()))+ self.visit(ctx.declares())
        return list(self.visit(ctx.declare()))

    # declare: funcDeclList | variableDeclList;
    def visitDeclare(self, ctx: MT22Parser.DeclareContext):
        if ctx.funcDeclList():
            return self.visit(ctx.funcDeclList())
        elif ctx.variableDeclList():
            return self.visit(ctx.variableDeclList())

    # funcDeclList: funcDecl funcDeclList | funcDecl;
    def visitFunDeclList(self, ctx:MT22Parser.FuncDeclListContext):
        if ctx.funcDeclList(): return [self.visit(ctx.funcDecl())] + self.visit(ctx.funcDeclList())
        return [self.visit(ctx.funcDecl())]
    
    # funcDecl: ID COLON FUNCTION funcType LB (variaFuncList)? RB ( INHERIT ID )? blockStmt;
    def visitFuncDecl(self, ctx:MT22Parser.FuncDeclContext):
        name = Id(ctx.ID(0).getText())
        return_type = self.visit(ctx.funcType())
        params = self.visit(ctx.variaFuncList()) if ctx.variaFuncList() else []
        body = self.visit(ctx.blockStmt())
        if ctx.INHERIT(): 
            inherit = Id(ctx.ID(1).getText())
        else: inherit = None
        return [FuncDecl(name, return_type, params, inherit, body)]

    # variaFuncList: variaFuncDeclarator COMMA variaFuncList | variaFuncDeclarator;
    def visitVariaFuncList(self, ctx: MT22Parser.VariaFuncListContext):
        if ctx.variaFuncList():
            return [self.visit(ctx.variaFuncDeclarator())]+self.visit(ctx.variaFuncList())
        return [self.visit(ctx.variaFuncDeclarator())]

    # variaFuncDeclarator: INHERIT? OUT? ID COLON typeType;
    def visitVariaFuncDeclarator (self, ctx:MT22Parser.VariaFuncDeclaratorContext):
        inherit = False
        out = False
        name = Id(ctx.ID().getText())
        typ = self.visit(ctx.typeType())
        if ctx.INHERIT(): inherit = True
        if ctx.OUT(): out = True
        return ParamDecl(name, typ, out, inherit)

    # variableDeclList: (varia_yes_body | (varia_no_body COLON (variType | arrayType)) ) SM;
    def visitVariableDeclList(self, ctx:MT22Parser.VariableDeclListContext):
        if ctx.varia_no_body():
            variNo = self.visit(ctx.varia_no_body())
            variNotyp = self.visit(ctx.variType()) if ctx.variType() else self.visit(ctx.arrayType())
            return [VarDecl(x, variNotyp, None) for x in variNo]
        elif ctx.varia_yes_body():
            variYes = self.visit(ctx.varia_yes_body())
            mid_index = len(variYes) // 2
            yesId = variYes[:mid_index]
            yesEss = variYes[mid_index+1:]
            yesTyp = variYes[mid_index]
            combined = [[str(a), str(b)] for a, b in zip(yesId, yesEss)]
            return [VarDecl(x[0], yesTyp, x[1]) for x in combined]

    # varia_no_body: ID COMMA varia_no_body | ID ;
    def visitVaria_no_body(self, ctx:MT22Parser.Varia_no_bodyContext):
        if ctx.varia_no_body(): 
            return [ctx.ID().getText()] + self.visit(ctx.varia_no_body())
        return [ctx.ID().getText()]

    # varia_yes_body: ID COMMA varia_yes_body COMMA espresso | ID COLON (variType | arrayType) ASS espresso;
    def visitVaria_yes_body(self, ctx:MT22Parser.Varia_yes_bodyContext):
        if ctx.varia_yes_body(): 
            return [ctx.ID().getText()] + self.visit(ctx.varia_yes_body()) + [self.visit(ctx.espresso())]
        return [ctx.ID().getText()] + [self.visit(ctx.variType()) if ctx.variType() else self.visit(ctx.arrayType())] + [self.visit(ctx.espresso())]

    # args: LB expList? RB;
    def visitArgs(self, ctx: MT22Parser.ArgsContext):
        return self.visit(ctx.expList()) if ctx.expList() else None

    # expList: espresso COMMA expList | espresso;
    def visitExpList(self, ctx: MT22Parser.ExpListContext):
        if ctx.expList():
            return [self.visit(ctx.espresso())]+self.visit(ctx.expList())
        return [self.visit(ctx.espresso())]

    # typeType: funcType | arrayType | variType;
    def visitTypeType(self, ctx: MT22Parser.TypeTypeContext):
        if ctx.funcType():
            return self.visit(ctx.funcType())
        elif ctx.arrayType():
            return self.visit(ctx.arrayType())
        elif ctx.variType():
            return self.visit(ctx.variType())

    # arrayType: ARRAY LSB arraySize RSB OF variType;
    def visitArrayType( self, ctx: MT22Parser.ArrayTypeContext):
        dimens = self.visit(ctx.arraySize())
        arrType = self.visit(ctx.variType())
        return ArrayType(dimens,arrType)
             
    # arraySize: INTEGERLIT COMMA arraySize | INTEGERLIT ;
    def visitArraySize(self, ctx:MT22Parser.ArraySizeContext):
        if ctx.arraySize():
            return [int(ctx.INTEGERLIT().getText())] + self.visit(ctx.arraySize())
        return [int(ctx.INTEGERLIT().getText())]                    

    # funcType: INTEGER | FLOAT | BOOLEAN | STRING | VOID | AUTO | arrayType;
    def visitFuncType(self, ctx: MT22Parser.FuncTypeContext):
        if ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BooleanType()
        elif ctx.STRING():
            return StringType()
        elif ctx.VOID():
            return VoidType()
        elif ctx.AUTO():
            return AutoType()
        elif ctx.arrayType():
            return self.visit(ctx.arrayType())

    # variType: INTEGER | FLOAT | BOOLEAN | STRING | AUTO;
    def visitVariType(self, ctx: MT22Parser.VariTypeContext):
        if ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BooleanType()
        elif ctx.STRING():
            return StringType()
        elif ctx.AUTO():
            return AutoType()

    # statement
    def visitStatement(self, ctx: MT22Parser.StatementContext):
        return self.visit(ctx.getChild(0))

    # assStmt: lhs ASS espresso;
    def visitAssStmt(self, ctx: MT22Parser.AssStmtContext):
        lhs = self.visit(ctx.lhs())
        rhs = self.visit(ctx.espresso())
        return AssignStmt(lhs, rhs)

    # ifStmt: IF LB espresso RB statement (ELSE statement)?;
    def visitIfStmt(self, ctx: MT22Parser.IfStmtContext):
        cond = self.visit(ctx.espresso())
        tstmt = self.visit(ctx.statement(0))
        fstmt = self.visit(ctx.statement(1)) if ctx.ELSE() else None
        return IfStmt(cond, tstmt, fstmt)

    # forStmt: FOR LB ID ASS espresso COMMA espresso COMMA espresso RB statement;
    def visitForStmt(self, ctx:MT22Parser.ForStmtContext):
        id = Id(ctx.ID().getText())
        initStmt = self.visit(ctx.espresso(0))
        AssSt = AssignStmt(id, initStmt)
        expr1 = self.visit(ctx.espresso(1))
        expr2 = self.visit(ctx.espresso(2))
        state = self.visit(ctx.statement())
        return ForStmt(AssSt,expr1,expr2,state)        
    
    # whileStmt: WHILE LB espresso RB statement;
    def visitWhileStmt(self, ctx:MT22Parser.WhileStmtContext):
        cond = self.visit(ctx.espresso())
        stmt = self.visit(ctx.statement())
        return WhileStmt(cond, stmt)
    
    # doWhileStmt: DO statement WHILE LB espresso RB;
    def visitDoWhileStmt(self, ctx:MT22Parser.DoWhileStmtContext):
        cond = self.visit(ctx.espresso())
        stmt = self.visit(ctx.statement())
        return DoWhileStmt(cond, stmt)
    
    # breakStmt: BREAK;
    def visitBreakStmt(self, ctx: MT22Parser.BreakStmtContext):
        return BreakStmt()

    # continueStmt: CONTINUE;
    def visitContinueStmt(self, ctx: MT22Parser.BreakStmtContext):
        return ContinueStmt()

    # returnStmt: RETURN espresso?;
    def visitReturnStmt(self, ctx: MT22Parser.ReturnStmtContext):
        if ctx.espresso():
            return ReturnStmt(self.visit(ctx.espresso()))
        return ReturnStmt(None)

    # callStmt: ID LB callEsp? RB;
    def visitCallStmt(self, ctx: MT22Parser.CallStmtContext):
        callEspress = self.visit(ctx.callEsp()) if ctx.callEsp() else []
        id = Id(ctx.ID().getText())
        return CallStmt(id, callEspress)
    
    # callEsp: espresso COMMA callEsp | espresso;
    def visitCallEsp(self, ctx:MT22Parser.CallEspContext):
        if ctx.callEsp():
            return [self.visit(ctx.espresso())]+self.visit(ctx.callEsp())
        return [self.visit(ctx.espresso())]        
    
    # blockStmt: LCB blockStmtbody? RCB;
    def visitBlockStmt(self, ctx: MT22Parser.BlockStmtContext):
        return self.visit(ctx.blockStmtbody()) if ctx.blockStmtbody() else []

    # blockStmtbody: (variableDeclList | statement) blockStmtbody | (variableDeclList | statement);
    def visitBlockStmtbody(self, ctx:MT22Parser.BlockStmtbodyContext):
        if ctx.blockStmtbody():
            return [self.visit(ctx.variableDeclList()) if ctx.variableDeclList() else self.visit(ctx.statement())]+self.visit(ctx.blockStmtbody())
        return [self.visit(ctx.variableDeclList()) if ctx.variableDeclList() else self.visit(ctx.statement())]    

    # espresso: espresso (AND | OR) espresso1 | espresso1;
    def visitEspresso(self, ctx: MT22Parser.EspressoContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.espresso1())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.espresso())
        right = self.visit(ctx.espresso1())
        return BinExpr(op, left, right)

    # espresso1: espresso1 (GT | LT | GTE | LTE) espresso2 | espresso2;
    def visitEspresso1(self, ctx: MT22Parser.Espresso1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.espresso2())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.espresso1())
        right = self.visit(ctx.espresso2())
        return BinExpr(op, left, right)

    # espresso2: espresso2 (EQUAL | NEQUAL) espresso3 | espresso3;
    def visitEspresso2(self, ctx: MT22Parser.Espresso2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.espresso3())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.espresso2())
        right = self.visit(ctx.espresso3())
        return BinExpr(op, left, right)

    # espresso3: espresso3 (ADD | SUB) espresso4 | espresso4;
    def visitEspresso3(self, ctx: MT22Parser.Espresso3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.espresso4())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.espresso3())
        right = self.visit(ctx.espresso4())
        return BinExpr(op, left, right)

    # espresso4: espresso4 (MUL | DIV | MOD) espresso5 | espresso5;
    def visitEspresso4(self, ctx: MT22Parser.Espresso4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.espresso5())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.espresso4())
        right = self.visit(ctx.espresso5())
        return BinExpr(op, left, right)

    # espresso5: espresso5 CONCAT espresso6 | espresso6;
    def visitEspresso5(self, ctx: MT22Parser.Espresso5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.espresso6())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.espresso5())
        right = self.visit(ctx.espresso6())
        return BinExpr(op, left, right)

    # espresso6: NOT espresso6 | espresso7;
    def visitEspresso6(self, ctx: MT22Parser.Espresso6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.espresso7())
        op = ctx.NOT().getText()
        val = self.visit(ctx.espresso6())
        return UnExpr(op, val)

    # espresso7: (ADD | SUB) espresso7 | espresso8;
    def visitEspresso7(self, ctx: MT22Parser.Espresso7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.espresso8())
        op = ctx.ADD().getText() if ctx.ADD() else ctx.SUB().getText()
        val = self.visit(ctx.espresso7())
        return UnExpr(op, val)

    # espresso8: espresso10 LSB espresso (COMMA espresso)* RSB | espresso10;
    # def visitEspresso8(self, ctx: MT22Parser.Espresso8Context):

    # espresso10: ID args | espresso11;
    def visitEspresso10(self, ctx: MT22Parser.Espresso10Context):
        if ctx.args():
            name = Id(ctx.ID().getText())
            args = self.visit(ctx.args())
            return FuncCall(name,args)
        return self.visit(ctx.espresso11())

    # espresso11: elem | arrayLit | LB espresso RB | ID;
    def visitEspresso11(self, ctx:MT22Parser.Espresso11Context):
        if ctx.elem(): return self.visit(ctx.elem())
        elif ctx.arrayLit(): return self.visit(ctx.arrayLit())
        elif ctx.espresso(): return self.visit(ctx.espresso())
        elif ctx.ID(): return Id(ctx.ID().getText())
    
    # espresso12: espresso12 COMMA elem | elem;
    def visitEspresso12(self, ctx: MT22Parser.Espresso12Context):
        if ctx.elem():
            return [self.visit(ctx.espresso12())]+self.visit(ctx.elem())
        return [self.visit(ctx.elem())]

    # lhs: ID | lhsop;
    def visitLhs(self, ctx: MT22Parser.LhsContext):
        if ctx.ID():
            return [Id(ctx.ID().getText())]
        elif ctx.lhsop():
            return self.visit(ctx.lhsop())

    # lhsop: ID LSB (espresso12 | lhsop) RSB;
    # arrayLit: LCB elemArrays? RCB;
    def visitArrayLit(self, ctx: MT22Parser.ArrayLitContext):
        return ArrayLit(self.visit(ctx.elemArrays())) if ctx.elemArrays() else None

    # elemArrays: espresso COMMA elemArrays | espresso;
    def visitElemArrays(self, ctx: MT22Parser.ElemArraysContext):
        if ctx.elemArrays():
            return [self.visit(ctx.espresso())]+self.visit(ctx.elemArrays())
        return [self.visit(ctx.espresso())]

    # elem: INTEGERLIT | FLOATLIT | booleanlit | STRINGLIT;
    def visitElem(self, ctx: MT22Parser.ElemContext):
        if ctx.INTEGERLIT():
            return IntegerLit(int(ctx.INTEGERLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLit(float(ctx.FLOATLIT().getText()))
        elif ctx.booleanlit():
            return self.visit(ctx.booleanlit())
        elif ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())

    # booleanlit: TRUE | FALSE;
    def visitBooleanlit(self, ctx: MT22Parser.BooleanlitContext):
        return BooleanLit(True) if ctx.TRUE() else BooleanLit(False)