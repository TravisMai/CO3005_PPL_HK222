from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    # program: (funcDeclList | variableDeclList)+ EOF;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program([])

    # funcDeclList: funcDecl funcDeclList | funcDecl;
    # funcDecl: ID COLON FUNCTION funcType LB (variaFuncList)? RB ( INHERIT ID )? blockStmt;

    # variaFuncList: variaFuncDeclarator COMMA variaFuncList | variaFuncDeclarator;
    # variaFuncDeclarator: INHERIT? OUT? ID COLON typeType;

    # variableDeclList: (varia_yes_body | varia_no_body) SM;

    # varia_no_body: ID COMMA varia_no_body | ID COLON (variType | arrayType);

    # varia_yes_body: ID COMMA varia_yes_body COMMA espresso | ID COLON (variType | arrayType) ASS espresso;

    # args: LB expList? RB;
    # expList: espresso COMMA expList | espresso;

    # typeType: funcType | arrayType | variType;
    def visitTypeType(self, ctx: MT22Parser.TypeTypeContext):
        if ctx.funcType():
            return self.visit(ctx.funcType())
        elif ctx.arrayType():
            return self.visit(ctx.arrayType())
        elif ctx.variType():
            return self.visit(ctx.variType())

    # arrayType: ARRAY LSB INTEGERLIT (COMMA INTEGERLIT)* RSB OF variType;

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
            return self.visit(ctx.ArrayType())

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

    # statement:
    # 	assStmt SM
    # 	| ifStmt
    # 	| forStmt
    # 	| whileStmt
    # 	| doWhileStmt SM
    # 	| breakStmt SM
    # 	| continueStmt SM
    # 	| returnStmt SM
    # 	| callStmt SM
    # 	| blockStmt;

    # assStmt: lhs ASS espresso;
    # ifStmt: IF LB espresso RB statement (ELSE statement)?;
    # forStmt: FOR LB ID ASS espresso COMMA espresso COMMA espresso RB statement;
    # whileStmt: WHILE LB espresso RB statement;
    # doWhileStmt: DO statement WHILE LB espresso RB;
    # breakStmt: BREAK;
    def visitBreakStmt(self, ctx:MT22Parser.BreakStmtContext):
        return BreakStmt()
    
    # continueStmt: CONTINUE;
    def visitContinueStmt(self, ctx:MT22Parser.BreakStmtContext):
        return ContinueStmt()
    
    # returnStmt: RETURN espresso?;
    def visitReturnStmt(self, ctx:MT22Parser.ReturnStmtContext):
        if ctx.espresso():
            return ReturnStmt(self.visit(ctx.espresso()))
        return ReturnStmt()

    # callStmt: ID LB (espresso (COMMA espresso)*)? RB;
    # blockStmt: LCB blockStmtbody? RCB;
    # blockStmtbody: (variableDeclList | statement) blockStmtbody | (variableDeclList | statement);

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
    # espresso10: ID args | espresso11;
    # espresso11: elem | arrayLit | LB espresso RB | ID;
    # espresso12: espresso12 COMMA elem | elem;
    def visitEspresso12(self, ctx:MT22Parser.Espresso12Context):
        if ctx.elem():
            return [self.visit(ctx.expression12())]+self.visit(ctx.elem())
        return [self.visit(ctx.elem())]
    
    # lhs: ID | lhsop;
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        if ctx.ID(): return [Id(ctx.ID().getText())]
        elif ctx.lhsop(): return self.visit(ctx.lhsop())            
    
    # lhsop: ID LSB (espresso12 | lhsop) RSB;
    # arrayLit: LCB elemArrays? RCB;
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