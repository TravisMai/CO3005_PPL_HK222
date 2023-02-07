# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3;")
        buf.write("\13\4\2\t\2\4\3\t\3\3\2\3\2\3\3\3\3\3\3\2\2\4\2\4\2\3")
        buf.write("\4\2\13\13\23\23\2\b\2\6\3\2\2\2\4\b\3\2\2\2\6\7\7\2\2")
        buf.write("\3\7\3\3\2\2\2\b\t\t\2\2\2\t\5\3\2\2\2\2")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'auto'", "'break'", "'boolean'", "'do'", "'else'", 
                     "'false'", "'float'", "'for'", "'function'", "'if'", 
                     "'interger'", "'return'", "'string'", "'true'", "'while'", 
                     "'void'", "'out'", "'continue'", "'of'", "'inherit'", 
                     "'array'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
                     "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'::'", "'('", "')'", "'['", "']'", "'.'", 
                     "','", "';'", "':'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>", "LINE_CMT", "BLOCK_CMT", "ID", "AUTO", 
                      "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
                      "FOR", "FUNCTION", "IF", "INTERGER", "RETURN", "STRING", 
                      "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", "OF", 
                      "INHERIT", "ARRAY", "ADD", "SUB", "MUL", "DIV", "MOD", 
                      "NOT", "AND", "OR", "EQUAL", "NEQUAL", "LT", "LTE", 
                      "GT", "GTE", "CONCAT", "LB", "RB", "LSB", "RSB", "DOT", 
                      "COMMA", "SM", "COLON", "LP", "RP", "ASS", "WS", "INTERGERLIT", 
                      "FLOATLIT", "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_booleanlit = 1

    ruleNames =  [ "program", "booleanlit" ]

    EOF = Token.EOF
    LINE_CMT=1
    BLOCK_CMT=2
    ID=3
    AUTO=4
    BREAK=5
    BOOLEAN=6
    DO=7
    ELSE=8
    FALSE=9
    FLOAT=10
    FOR=11
    FUNCTION=12
    IF=13
    INTERGER=14
    RETURN=15
    STRING=16
    TRUE=17
    WHILE=18
    VOID=19
    OUT=20
    CONTINUE=21
    OF=22
    INHERIT=23
    ARRAY=24
    ADD=25
    SUB=26
    MUL=27
    DIV=28
    MOD=29
    NOT=30
    AND=31
    OR=32
    EQUAL=33
    NEQUAL=34
    LT=35
    LTE=36
    GT=37
    GTE=38
    CONCAT=39
    LB=40
    RB=41
    LSB=42
    RSB=43
    DOT=44
    COMMA=45
    SM=46
    COLON=47
    LP=48
    RP=49
    ASS=50
    WS=51
    INTERGERLIT=52
    FLOATLIT=53
    STRINGLIT=54
    UNCLOSE_STRING=55
    ILLEGAL_ESCAPE=56
    ERROR_CHAR=57

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanlitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(MT22Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MT22Parser.FALSE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_booleanlit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanlit" ):
                return visitor.visitBooleanlit(self)
            else:
                return visitor.visitChildren(self)




    def booleanlit(self):

        localctx = MT22Parser.BooleanlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_booleanlit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            _la = self._input.LA(1)
            if not(_la==MT22Parser.FALSE or _la==MT22Parser.TRUE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





