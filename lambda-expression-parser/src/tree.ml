type tree =
  Variable of string
  | Abstraction of string * tree
  | Application of tree * tree
;;

type dTree =
  DVariable of string
  | DClosedVariable of int
  | DApplication of dTree * dTree
  | DAbstraction of dTree
;;

type ttype =
  Tvariable of string
  | TImplication of ttype * ttype
;;
