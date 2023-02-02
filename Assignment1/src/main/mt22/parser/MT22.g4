grammar MT22;

// 2052612
// MAI HUU NGHIA
@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program:  EOF ;





// 3.1 Characters set



// 3.2 Comment
LINE_CMT:		'//' ~[\r\n]* ('\r'? '\n') -> skip;
BLOCK_CMT: 		'/*' .*? '*/' -> skip;

// 3.3 Identifiers
ID: 			[a-zA-Z_][a-zA-Z0-9_]*;

// 3.4 Keywords
AUTO:			'auto';
BREAK:			'break';
BOOLEAN:		'boolean';
DO:				'do';
ELSE:			'else';
FALSE:			'false';
FLOAT:			'float';
FOR:			'for';
FUNCTION:		'function';
IF:				'if';
INTERGER:		'interger';
RETURN:			'return';
STRING:			'string';
TRUE:			'true';
WHILE:			'while';
VOID:			'void';
OUT:			'out';
CONTINUE:		'continue';
OF:				'of';
INHERIT:		'inherit';
ARRAY:			'array';

// 3.5 Operators
ADD: 			'+';
SUB: 			'-';
MUL: 			'*';
DIV: 			'/';
MOD:			'%';
NOT:            '!';
AND:            '&&';
OR: 			'||';
EQUAL: 			'==';
NEQUAL: 		'!=';
LT:            	'<';
LTE:            '<=';
GT:            	'>';
GTE:            '>=';
CONCAT:			'::';

// 3.6 Separators
LB:     		'(';
RB:     		')';
LSB:			'[';
RSB:			']';
DOT:    		'.';
COMMA:  		',';
SM:     		';';
COLON:  		':';
LP:	    		'{';
RP:	    		'}';
ASS:			'=';

// 3.7 Literals
WS : 			[ \t\r\n_]+ -> skip ; // skip spaces, tabs, newlines
INTERGERLIT: 	([1-9][0-9_]*| '0');
FLOATLIT: 		([1-9][0-9_]* | '0') (Deci | Deci? Expo);
booleanlit: 	TRUE | FALSE;
STRINGLIT:      '"' StrCha? '"';
fragment StrCha:(~["\\\r\n] | Esc)+;
fragment Esc:	'\\' [btnfr"'\\];
fragment Deci:	'.'[0-9]*;
fragment Expo: 	('e'|'E') ('+'|'-')?[0-9]+;

// 7 Statements
/* statement:		AssStmt SM
				|ifStmt
				|forStmt
				|whileStmt
				|doWhileStmt SM
				|breakStmt SM
				|continueStmt SM
				|returnStmt SM
				|callStmt SM
				|blockStmt;

AssStmt:		lhs ASS expression;
ifStmt:			IF expression THEN statement (ELSE statement)?;
forStmt:		FOR LB ID ASS expression COMMA expression COMMA expression RB statement;
whileStmt:		WHILE LB expression RB statement;
doWhileStmt:	DO statement WHILE LB expression RB;
breakStmt:		BREAK;
continueStmt:	CONTINUE;
returnStmt:		RETURN expression;
callStmt:		ID LB (expression (COMMA expression)*)? RB;
blockStmt:		LP statement RP;*/


UNCLOSE_STRING: '"' StrCha*  EOF? {
	y = str(self.text)
	raise UncloseString(y[0:])
};
ILLEGAL_ESCAPE: '"' StrCha* ('\\' ~[bfrnt"\\]) {
	y = str(self.text)
	raise IllegalEscape(y[0:])
};
ERROR_CHAR: .{
	raise ErrorToken(self.text)
};