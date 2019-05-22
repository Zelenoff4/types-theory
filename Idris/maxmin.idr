%default total

myProof : (a : Nat) -> (b : Nat) -> maximum a (minimum a b) = a
myProof Z Z = Refl
myProof Z b = Refl
myProof (S a) Z = Refl
myProof (S a) (S b) = rewrite myProof a b in Refl
--cong (myProof a b)

main : IO()
main = do
  putStrLn "Easy"
