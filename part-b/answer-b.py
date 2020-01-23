from propositional_logic import *

A = BoolVar('A')
B = BoolVar('B')
C = BoolVar('C')

# write code using A, B, and C, along with
# the classes from propositional_logic.py
# and the .format() mathod to output the
# following expression:

# (((A => B) & (B => C)) => (A => C))
ab = Implies(A, B)
bc = Implies(B, C)
ac = Implies(A, C)

f1 = And(ab, bc)
f2 = Implies(f1, ac)

print(f2.format())
