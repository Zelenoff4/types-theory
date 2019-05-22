%default total

data Div : (a, b : Nat) -> Type
  where
    Provide : (k: Nat ** a = k * b) -> Div a b

help : {a : Nat} -> {b : Nat} -> {k : Nat} -> (a + b) = k * a -> b = (minus k 1) * a
{-
first : minus(a + b) a = b
sym first : b = minus (a + b) a
second : minus (a + b) a = minus (k * a) a
trans (sym first) second : b = minus (k * a) a
third : minus(k * a) a = (minus k 1) * a
trans (trans sym first) second) third : b  = (minus k 1) * a
-}
help {a} {b} {k} prf = trans (trans (sym first) second) third
  where
    --this proves that a + b - a = b
    helpFirst : (a, b : Nat) -> minus (a + b) a = b
    helpFirst Z b = minusZeroRight b
    helpFirst (S a) b = rewrite helpFirst a b in Refl

    first : minus (a + b) a = b
    first = helpFirst a b

    --this proves that a + b - a = k * a - a, where (a + b) = (k * a)
    second : minus (a + b) a = minus (k * a) a
    --this basically puts -a to both sides
    second = cong {f = \x => minus x a} prf

    --this proves that k*a - a = (k - 1) * a
    helpThird : (a, k: Nat) -> minus (k * a) a = (minus k 1) * a
    helpThird a k = sym (trans localFirst localSecond)
      where
        --right distributivity : (k - 1) * a = (k * a) - (1 * a)
        localFirst : (minus k 1) * a = minus (k * a) (1 * a)
        localFirst = (multDistributesOverMinusLeft k 1 a)
        --multDistributesOverMinusLeft	 : 	(left : Nat) -> (centre : Nat) -> (right : Nat) -> minus left centre * right = minus (left * right) (centre * right)

        localSecond : minus (k * a) (1 * a) = minus (k * a) a
        localSecond = rewrite multOneLeftNeutral a in Refl

    third : minus (k * a) a = (minus k 1) * a
    third = helpThird a k

task : {a : Nat} -> {b : Nat} -> (Div (a + b) a) -> (Div b a)
task (Provide (k ** prf)) = Provide ((minus k 1) ** help prf)

main : IO()
main = do
  putStrLn "It works!"
