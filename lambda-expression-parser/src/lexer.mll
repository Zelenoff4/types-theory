{
  open Lexing
  open Parser
  let next_line lexbuf =
    let pos = lexbuf.lex_curr_p in
      lexbuf.lex_curr_p <-
      { 
        pos with pos_bol = lexbuf.lex_curr_pos;
        pos_lnum = pos.pos_lnum + 1
      }
}
let variable = ['a' - 'z'] ['a' - 'z' '0' - '9' '\'']*
let white = [' ' '\t' '\n' '\r']+
rule main = parse
  | variable as v { VAR(v) }
  | "\\"      	  { ANY }
  | "."	    	  { POINT }         
  | "("           { OPEN }
  | ")"           { CLOSE }
  | white         { main lexbuf }
  | eof           { EOF }
