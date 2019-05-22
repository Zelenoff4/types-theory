%{
  open Tree;;
%}
%token <string> VAR
%token ANY
%token POINT
%token OPEN CLOSE
%token EOF

%right POINT

%start main
%type <Tree.tree> main
%%
main:
  expr EOF		        	{ $1 }
expr:
  aplication ANY VAR POINT expr 	{ Application($1, Abstraction($3, $5)) }
  |ANY VAR POINT expr          		{ Abstraction($2, $4) }
  |aplication				{ $1 }
aplication:
  aplication atom			{ Application($1, $2) }
  |atom					{ $1 }
atom:
  OPEN expr CLOSE			{ $2 }
  |VAR					{ Variable($1) }
