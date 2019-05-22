open Buffer;;
open Printf;;

let (>>) x f = f x;;

let string_of_tree tree =
  let buf = Buffer.create 1024 in
  let rec s_t t = match t with
    Tree.Variable v -> Buffer.add_string buf v
    | Tree.Abstraction (var, expr) -> Buffer.add_char buf '('; Buffer.add_char buf '\\'; Buffer.add_string buf var; Buffer.add_char buf '.'; s_t expr; Buffer.add_char buf ')'
    | Tree.Application (l, r) -> Buffer.add_char buf '('; s_t l; Buffer.add_char buf ' '; s_t r; Buffer.add_char buf ')'
  in s_t tree;
  Buffer.contents buf;;

let dbtoString tree =
  let buf = Buffer.create 1024 in
  let rec s_t t = match t with
    Tree.DVariable v -> Buffer.add_string buf v
    | Tree.DAbstraction tree -> Buffer.add_char buf '('; Buffer.add_char buf '\\'; Buffer.add_char buf '.'; s_t tree; Buffer.add_char buf ')'
    | Tree.DApplication (l, r) -> Buffer.add_char buf '('; s_t l; Buffer.add_char buf ' '; s_t r; Buffer.add_char buf ')'
    | Tree.DClosedVariable v -> Buffer.add_string buf (string_of_int v)
  in s_t tree;
  Buffer.contents buf;;

module DBMap = Map.Make(String);;
let dbMap = ref DBMap.empty;;

let toDeBrjiunAA tree =
let rec toDeBrjiun tree level =
  match tree with
    | Tree.Application (left, right) -> Tree.DApplication (toDeBrjiun left level, toDeBrjiun right level)
    | Tree.Abstraction (var, expr) ->
        let f = ref false in
        let old = ref (-1) in
        if (DBMap.mem var !dbMap) then
          begin
            old := DBMap.find var !dbMap;
            f := true;
          end;
        dbMap := DBMap.add var (level + 1) !dbMap;
        let ans = Tree.DAbstraction (toDeBrjiun expr (level + 1)) in
        if (!f) then
          dbMap := DBMap.add var !old !dbMap
        else
          dbMap := DBMap.remove var !dbMap;
        ans
    | Tree.Variable var -> if (DBMap.mem var !dbMap)
    then Tree.DClosedVariable (level - (DBMap.find var !dbMap))
    else Tree.DVariable var
    in toDeBrjiun tree 0;;

let rec reduce expr newex level =
  match expr with
    Tree.DClosedVariable v ->
      if (v == level) then
        let rec update curexpr curlvl lvlup =
          match curexpr with
            Tree.DVariable v -> curexpr
            | Tree.DClosedVariable v -> if (v >= curlvl) then Tree.DClosedVariable (v + lvlup) else curexpr
            | Tree.DApplication (left, right) -> Tree.DApplication (update left curlvl lvlup, update right curlvl lvlup)
            | Tree.DAbstraction e -> Tree.DAbstraction (update e (curlvl + 1) lvlup)
        in update newex 0 level
      else if (v > level) then Tree.DClosedVariable (v - 1) else expr
    | Tree.DVariable v -> expr
    | Tree.DApplication (left, right) -> Tree.DApplication (reduce left newex level, reduce right newex level)
    | Tree.DAbstraction e -> Tree.DAbstraction (reduce e newex (level + 1));;

let rec findRedex expr =
  match expr with
  Tree.DVariable v -> expr
  | Tree.DAbstraction expr1 -> Tree.DAbstraction (findRedex expr1)
  | Tree.DClosedVariable v -> expr
  | Tree.DApplication (left, right) ->
      match left with
        Tree.DVariable var -> Tree.DApplication (left, findRedex right)
        | Tree.DClosedVariable var -> Tree.DApplication (left, findRedex right)
        | Tree.DAbstraction expr1 -> reduce expr1 right 0
        | Tree.DApplication (lleft, rright) -> Tree.DApplication (findRedex left, findRedex right)

let input_data =
let buf = Buffer.create 1024 in
try
  while true do
    let line = read_line() in
    Buffer.add_string buf line;
    Buffer.add_char buf '\n';
  done; assert false
with End_of_file -> Buffer.contents buf;;

let makeZelenoi var =
  "zelenoi" ^ string_of_int var;;

let rec fromDB expr level =
  match expr with
    Tree.DClosedVariable v -> Tree.Variable (makeZelenoi (level - v))
    | Tree.DVariable v -> Tree.Variable(v)
    | Tree.DApplication (left, right) -> Tree.Application (fromDB left level, fromDB right level)
    | Tree.DAbstraction ex -> Tree.Abstraction (makeZelenoi (level + 1), fromDB ex (level + 1));;

let makeRedex tree =
  let intermediate = ref tree in
    begin
      let f = ref true in
      let oldValue = ref !intermediate in
      while (!f) do
        intermediate := findRedex !intermediate;
        if (!oldValue = !intermediate) then f := false;
        oldValue := !intermediate;
      done
    end;
    fromDB !intermediate 0;;

(*============unification==========*)
module UMap = Map.Make(String);;
let unification = ref UMap.empty;;
let counter = ref 0;;
let umap = ref UMap.empty;;
let equations = ref [];;


let rec makeSystem expr =
  match expr with
    Tree.Variable var ->
      let typeNum = (string_of_int !counter) in
        if not (UMap.mem var !umap) then
          begin
            umap := UMap.add var (Tree.Tvariable("t" ^ typeNum)) !umap;
            counter := !counter + 1
          end;
      UMap.find var !umap
    | Tree.Abstraction (var, right) ->
        umap := UMap.add var (Tree.Tvariable("t" ^ (string_of_int !counter))) !umap;
        counter := !counter + 1;
        let rightPart = makeSystem right in
          let leftPart = UMap.find var !umap in
            umap := UMap.remove var !umap;
            Tree.TImplication (leftPart, rightPart)
    | Tree.Application (left, right) ->
      let leftPart = makeSystem left in
      let rightPart = makeSystem right in
      let cur = "t" ^ (string_of_int !counter) in
      counter := !counter + 1;
      let (x, y) = (leftPart, Tree.TImplication(rightPart, Tree.Tvariable(cur))) in
        equations := (x, y) :: !equations;
        Tree.Tvariable(cur)
;;

let rec systemToString tree =
  let buf = Buffer.create 1024 in
    let rec s_t expr =
      match expr with
        Tree.Tvariable var -> Buffer.add_string buf var
        | Tree.TImplication (left, right) -> s_t left; Buffer.add_string buf " -> "; s_t right
    in s_t tree;
  Buffer.contents buf;;


module USet = Set.Make(String);;

let rec typeToString t =
  match t with
    Tree.Tvariable var -> var
    | Tree.TImplication (left, right) -> "(" ^ (typeToString left) ^ " -> " ^ (typeToString right) ^ ")"
;;

let rec substitution t =
  match t with
    Tree.Tvariable var ->
      if UMap.mem var !unification then substitution (UMap.find var !unification)
      else t
    | Tree.TImplication (left, right) -> Tree.TImplication (substitution left, substitution right)
;;

let rec getFV expr =
  match expr with
    Tree.Variable v -> USet.singleton v
    | Tree.Abstraction (var, expr1) -> USet.remove var (getFV expr1)
    | Tree.Application (left, right) -> USet.union (getFV left) (getFV right)
;;

let makeTree expr =
  let fv = getFV expr in
  let flag = ref false in
  let result = ref "" in
    USet.iter (fun x ->
      if !flag then result := !result ^ ", ";
      flag := true;
      result := !result ^ x ^ " : " ^ (typeToString (substitution (UMap.find x !umap)))
      ) fv;
    !result
;;

let localSub pair = (substitution (fst pair), substitution (snd pair));;
let rec listSub l =
  match l with
    [] -> []
    | head :: tail -> (localSub head) :: (listSub tail)
;;


let typeExistance = ref true;;

let rec printList l =
  match l with
    [] -> print_endline " "
    | head :: tail -> printList tail; print_endline( "(" ^ (typeToString (fst head)) ^ " = " ^ (typeToString (snd head)) ^ ")")
;;

let rec unificationStep l =
  match l with
    [] -> []
    | head :: tail ->
      (*fst head >> systemToString >> print_string;*)
      match fst head with
        | Tree.Tvariable var ->
          begin
            match snd head with
              | Tree.Tvariable other ->
                if var != other then
                  unification := UMap.add var (snd head) !unification;
                  unificationStep (listSub tail)
              | Tree.TImplication (left, right) ->
                let rec equals one another =
                  match another with
                    Tree.Tvariable ev -> if (ev = one) then false else true
                    | Tree.TImplication (lleft, rright) -> (equals one lleft) && (equals one rright)
                in
                if (equals var (snd head)) then
                  begin
                    unification := UMap.add var (snd head) !unification;
                    unificationStep (listSub tail)
                  end
                else
                  begin
                    typeExistance := false;
                    []
                  end
            end
        | Tree.TImplication (left, right) ->
          begin
            match snd head with
              Tree.Tvariable vvv -> (snd head, fst head) :: (unificationStep tail)
              | Tree.TImplication (llleft, rrright) -> (left, llleft) :: (right, rrright) :: (unificationStep tail)
          end
;;

let unify q =
  let rec doUnify eq =
    match unificationStep eq with
      [] -> []
      | head :: tail -> doUnify (listSub (head :: tail))
  in doUnify !equations;
  ()
;;


let rec addTabs amount =
  if amount = 0 then ""
  else "*   " ^ addTabs (amount - 1);;

let rec makeAns expr freeValues indent =
  match expr with
    Tree.Variable var ->
      let curType = (string_of_int !counter) in
        if not (UMap.mem var !umap) then
          begin
            umap := UMap.add var (substitution (Tree.Tvariable("t" ^ curType))) !umap;
            counter := !counter + 1
          end;
      let res = UMap.find var !umap in
        let buf = Buffer.create 10000 in
          Buffer.add_string buf (addTabs indent);
          Buffer.add_string buf freeValues;
          Buffer.add_string buf (if freeValues = "" then "|- " else " |- ");
          Buffer.add_string buf var;
          Buffer.add_string buf " : ";
          Buffer.add_string buf (typeToString (substitution res));
          Buffer.add_string buf " [rule #1]\n";
          (substitution res, Buffer.contents buf)
    | Tree.Application (left, right) ->
      let leftPart = makeAns left freeValues (indent + 1) in
        let rightPart = makeAns right freeValues (indent + 1) in
          let curType = "t" ^ (string_of_int !counter) in
            counter := !counter + 1;
      let res = substitution (Tree.Tvariable curType) in
        let buf = Buffer.create 10000 in
          Buffer.add_string buf (addTabs indent);
          Buffer.add_string buf freeValues;
          Buffer.add_string buf (if freeValues = "" then "|- " else " |- ");
          Buffer.add_string buf (string_of_tree expr);
          Buffer.add_string buf " : ";
          Buffer.add_string buf (typeToString (substitution res));
          Buffer.add_string buf " [rule #2]\n";
          Buffer.add_string buf (snd leftPart);
          Buffer.add_string buf (snd rightPart);
          (substitution res, Buffer.contents buf)
          (*blyaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa kill me pls*)
    | Tree.Abstraction (var, expr1) ->
      umap := UMap.add var (substitution (Tree.Tvariable ("t" ^ (string_of_int !counter)))) !umap;
      counter := !counter + 1;
      let tempBuf = Buffer.create 10000 in
        Buffer.add_string tempBuf var;
        Buffer.add_string tempBuf " : ";
        Buffer.add_string tempBuf (typeToString (substitution (UMap.find var !umap)));
        let tempBufResults = Buffer.contents tempBuf in
          let part = makeAns expr1 (if freeValues = "" then tempBufResults else freeValues ^ ", " ^ tempBufResults) (indent + 1) in
            let varType = UMap.find var !umap in
              umap := UMap.remove var !umap;
        let res = substitution (Tree.TImplication (varType, fst part)) in
          let buf = Buffer.create 10000 in
          Buffer.add_string buf (addTabs indent);
          Buffer.add_string buf freeValues;
          Buffer.add_string buf (if freeValues = "" then "|- " else " |- ");
          Buffer.add_string buf (string_of_tree expr);
          Buffer.add_string buf " : ";
          Buffer.add_string buf (typeToString (substitution res));
          Buffer.add_string buf " [rule #3]\n";
          Buffer.add_string buf (snd part);
          (substitution res, Buffer.contents buf)
          (*Im so done pls work*)
;;


  (*input_data >> Lexing.from_string >> Parser.main Lexer.main >> toDeBrjiunAA >> dbtoString >> print_string;;
  print_endline "\n";;*)
  (*input_data >> Lexing.from_string >> Parser.main Lexer.main >> toDeBrjiunAA >> makeRedex >> string_of_tree >> print_string;*)
  let inputTree = input_data >> Lexing.from_string >> Parser.main Lexer.main;;
  let system = inputTree >> makeSystem;; (*>> systemToString >> print_endline;*)
  system >> systemToString >> print_endline;;
  let frees = inputTree >> makeTree;;
  (*(system >> systemToString) ^ " before\n" >> print_string;;*)
  (*let fakeBuild = makeAns inputTree frees 0 in*)
  (*frees >> print_endline;
  not !typeExistance >> string_of_bool >> print_endline;
  snd fakeBuild >> print_endline;*)
  !counter >> string_of_int >> print_endline;;
  unify 0;;
  !equations >> printList;
  print_endline "LIST IS ABOVE";
  !counter >> string_of_int >> print_endline;;
  (*((UMap.cardinal !umap) >> string_of_int) ^ " umap " >> print_endline;
  ((UMap.cardinal !unification) >> string_of_int) ^ " unification " >> print_endline;*)
  counter := 0;;
  if not !typeExistance then print_string "Expression has no type" else
      let frees = makeTree inputTree in
      umap := UMap.empty;
      (*(system >> systemToString) ^ " after\n" >> print_string;*)
      (*snd (makeAns inputTree frees 0) >> print_string*)
      (*let realBuild = makeAns inputTree frees 0 in
      snd realBuild >> print_string;*)
      begin
      frees >> print_endline;
      snd (makeAns inputTree frees 0) >> print_string
      end;
