grammar MT22;

// 2052612 MAI HUU NGHIA
@lexer::header {
from lexererr import *
}

@parser::members {
}

options {
	language = Python3;
}

program: (funcDeclList | variableDeclList)* EOF;

funcDeclList: funcDecl funcDeclList | funcDecl;
funcDecl:
	ID COLON FUNCTION funcType LB (variaFuncList)? RB (
		INHERIT ID
	)? blockStmt;

variaFuncList:
	variaFuncDeclarator COMMA variaFuncList
	| variaFuncDeclarator;
variaFuncDeclarator: INHERIT? OUT? ID COLON typeType;

variableDeclList: (varia_yes_body | varia_no_body) SM;

varia_no_body:
	ID COMMA varia_no_body
	| ID COLON (variType | arrayType);

varia_yes_body:
	ID COMMA varia_yes_body COMMA expression
	| ID COLON (variType | arrayType) ASS expression;

args: LB expList? RB;
expList: expression COMMA expList | expression;

typeType: funcType | arrayType;
arrayType:
	ARRAY LSB INTEGERLIT (COMMA INTEGERLIT)? RSB OF variType;
funcType: INTEGER | FLOAT | BOOLEAN | STRING | VOID;
variType: INTEGER | FLOAT | BOOLEAN | STRING;

statement:
	assStmt SM
	| ifStmt
	| forStmt
	| whileStmt
	| doWhileStmt SM
	| breakStmt SM
	| continueStmt SM
	| returnStmt SM
	| callStmt SM
	| blockStmt;

assStmt: lhs ASS expression;
ifStmt: IF LB expression RB statement (ELSE statement)?;
forStmt:
	FOR LB ID ASS expression COMMA expression COMMA expression RB statement;
whileStmt: WHILE LB expression RB statement;
doWhileStmt: DO statement WHILE LB expression RB;
breakStmt: BREAK;
continueStmt: CONTINUE;
returnStmt: RETURN expression;
callStmt: ID LB (expression (COMMA expression)*)? RB;
blockStmt: LCB blockStmtbody? RCB;
blockStmtbody: (variableDeclList | statement) blockStmtbody
	| (variableDeclList | statement);

expression:
	expression1 (GT | LT | GTE | LTE) expression1
	| expression1;
expression1:
	expression2 (EQUAL | NEQUAL) expression2
	| expression2;
expression2: expression2 (AND | OR) expression3 | expression3;
expression3: expression3 (ADD | SUB) expression4 | expression4;
expression4:
	expression4 (MUL | DIV | MOD) expression5
	| expression5;
expression5: expression5 CONCAT expression6 | expression6;
expression6: NOT expression6 | expression7;
expression7: (ADD | SUB) expression7 | expression8;
expression8: expression9 LSB expression RSB | expression9;
expression9:
	expression9 DOT ID args
	| expression10
	| expression9 DOT ID;
expression10: ID args | expression11;
expression11: elem | arrayLit | LB expression RB | ID;
lhs: ID | expression9 DOT ID | expression9 LSB expression RSB;

// 3.4 Keywords
AUTO: 'auto';
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
TRUE: 'true';
WHILE: 'while';
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';

// 3.5 Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
NEQUAL: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
CONCAT: '::';

// 3.6 Separators
LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
DOT: '.';
COMMA: ',';
SM: ';';
COLON: ':';
LCB: '{';
RCB: '}';
ASS: '=';

// 3.2 Comment
LINE_CMT: '//' ~[\r\n]* -> skip;
BLOCK_CMT: '/*' .*? '*/' -> skip;

// 3.7 Literals 12_12345
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
INTEGERLIT: ('0' | [1-9][0-9]* ('_'[0-9])*)+ {self.text = self.text.replace("_","")};
//INTEGERLIT: ([1-9][0-9_]* | '0')+ {self.text = self.text.replace("_","")};
FLOATLIT: ('0' | [1-9][0-9_]*)+ (Deci | Deci? Expo) {self.text = self.text.replace("_","")};
booleanlit: TRUE | FALSE;

STRINGLIT: ('"' StrCha? '"') {self.text = self.text[1:-1]};
arrayLit: LCB elemArrays RCB;
elemArrays: elemArray COMMA elemArrays | elemArray;
elemArray: INTEGERLIT | FLOATLIT | booleanlit | STRINGLIT;
elem: INTEGERLIT | FLOATLIT | booleanlit | STRINGLIT;
fragment StrCha: (~["\\\r\n] | Esc)+;
fragment Esc: '\\' [btnfr"'\\];
fragment Deci: '.' [0-9]*;
fragment Expo: ('e' | 'E') ('+' | '-')? [0-9]+;

// 3.3 Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;

UNCLOSE_STRING:
	'"' StrCha* EOF? {
	y = str(self.text)
	raise UncloseString(y[0:])
};
ILLEGAL_ESCAPE:
	'"' StrCha* ('\\' ~[bfrnt"\\]) {
	y = str(self.text)
	raise IllegalEscape(y[0:])
};
ERROR_CHAR:
	.{
	raise ErrorToken(self.text)
};