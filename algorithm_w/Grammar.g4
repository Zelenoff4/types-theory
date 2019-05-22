grammar Grammar;

expression: let var myEquals expression myIn expression | abstraction;

let: LET;
myIn: IN;
var: VAR;
myEquals: EQ;
lpar: LPAR;
rpar: RPAR;
myLabmda: LAMBDA;
dot: DOT;

abstraction: application | application* myLabmda var dot abstraction;
application: application atom | atom;
atom: lpar expression rpar | var;


LET: 'let';
IN: 'in';
fragment LITERAL: [a-zA-Z];
fragment DIGIT: [0-9];
VAR: LITERAL (LITERAL | DIGIT)*;
EQ: '=';
LPAR: '(';
RPAR: ')';
DOT: '.';
LAMBDA: '\\';
WHITESPACE: [ \t\r\n] -> skip;