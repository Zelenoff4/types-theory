import Prelude.Nat
%default total

subIsZero: LTE n m -> minus n m = Z
subIsZero LTEZero = Refl
subIsZero (LTESucc x) = rewrite subIsZero x in Refl

equalityToLte : {a, b : Nat} -> a = b -> LTE a b
equalityToLte {a = Z} b = LTEZero
equalityToLte {a = S a'} {b = Z} x = void (uninhabited x)
--succInjective returns a`
--equalityToLte returns some kind of LTE a' b'
--thus LTESucc returns LTE (S a') (S b), making it go recursive to Z
equalityToLte {a = S a'} {b = S b'} x = LTESucc (equalityToLte (succInjective a' b' x))

minusToLte: {n, m : Nat} -> LTE (minus n m) n
minusToLte {n = Z} = LTEZero
minusToLte {n = S n'} {m = Z} = lteRefl
minusToLte {n = S n'} {m = S m'} = lteSuccRight (minusToLte {n = n'} {m = m'})

--gets the desired type
--minusToLte returns LTE (n - m) n
--lteAddRight n retirn LTE n (n + m)
--lteTransitive returns LTE (n - m) (n + m)
leftMinusRightAddLTE: {n, m: Nat} -> LTE (minus n m) (n + m)
leftMinusRightAddLTE {n} = lteTransitive minusToLte (lteAddRight n)

start: {a, b : Nat} -> (a + b) * (a + b) = (a + b) * a + (a + b) * b
start {a} {b} = multDistributesOverPlusRight (a + b) a b

--first mult returns (a + b) * a = a * a + b * a
--second mult returns (a + b) * b = a * b + b * b
--intermediate type is : a = b -> c = d -> a + c = b + d
--it is rewritten as ((a + b) * a + (a + b) * b) = (a * a + b * a) + (a * b + b * b)
step: {a, b : Nat} -> ((a + b) * a + (a + b) * b) = (a * a + b * a) + (a * b + b * b)
step {a} {b} = rewrite (multDistributesOverPlusLeft a b a) in rewrite (multDistributesOverPlusLeft a b b) in Refl

desire: {a, b : Nat} -> (a * a + b * a) + (a * b + b * b) =  a * a + (b * a + (a * b + b * b))
desire {a} {b} = sym (plusAssociative (a * a) (b * a) (a * b + b * b))

--start returns (a + b) * (a + b) = (a + b) * a + (a * b) * b
--step returns (a + b) * a + (a * b) * b = (a * a + b * a) + (a * b + b * b)
--thus first trans returns (a + b) * (a + b) = (a * a + b * a) + (a * b + b * b)
--desire returns (a * a + b * a) + (a * b + b * b) = a * a + (b * a + (a * b + b * b))
--thus last trans returns (a + b) * (a + b) = a * a + (b * a + (a * b + b * b))
finalSquareRepl : {a, b : Nat} -> (a + b) * (a + b) =  a * a + (b * a + (a * b + b * b))
finalSquareRepl {a} {b} = trans (trans start step) desire

zeroSubtract : n = n - 0
zeroSubtract {n = Z} = Refl
zeroSubtract {n = S n'} = Refl

finalResolvedRepr : LTE n m -> m = n + (m - n)
finalResolvedRepr {m} LTEZero = zeroSubtract {n = m}
finalResolvedRepr {n = S n'} {m = S m'} (LTESucc x) = rewrite finalResolvedRepr x in Refl

resolvedRepr : LTE n m -> m * m = (n + (m - n)) * (n + (m - n))
resolvedRepr x = rewrite finalResolvedRepr x in Refl

--righthand side is m*m believe_me
squareMRepr : LTE n m -> m * m = n * n + ((m - n) * n + (n * (m - n) + (m - n) * (m - n)))
squareMRepr {n} {m} x = trans (resolvedRepr x) (finalSquareRepl {a = n} {b = m - n})

subSquares : LTE n m -> LTE (n * n) (m * m)
subSquares {n} {m} x =
  --lteAddRight returns LTE n^2 (n^2 + m^2 - n^2)
  --equalityToLte returns LTE (n^2 + m^2 - n^2) (m^2)
  --thus lteTransitive returns LTE n^2 m^2
  (lteAddRight {m = (m - n) * n + (n * (m - n) + (m - n) * (m - n))} (n * n)) `lteTransitive`
  (equalityToLte {a = n * n + ((m - n) * n + (n * (m - n) + (m - n) * (m - n)))} {b = m * m} (sym (squareMRepr x)))

--leftMinusRightAddLTE returns LTE (a - b) (a + b)
--subSquares returns LTE (a - b) ^ 2 (a + b) ^ 2
--subIsZero proves the result returned
task : {a, b : Nat} -> (minus a b) * (minus a b) `minus` (a + b) * (a + b) = 0
task {a} {b} = subIsZero (subSquares (leftMinusRightAddLTE {n = a} {m = b}))

main : IO()
main = do
  putStrLn "Holy heaven and Jesus pls work"

{-
a : (minus 5 2) * (minus 5 2) `minus` (5 + 2) * (5 + 2) = 0
a = task {a = 5} {b = 2}
-}
