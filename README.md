# 24Game

24 game - play with cards

valid inputs 1 - 10
1 represents face cards, can count as either the value 1 or 10
if four random cards can be operated on in such a way that results in the number 24,
with the operations : addition, subtraction, multiplication, division :
the game is won!

this script checks all permutations of inputed values, to determine if there exists a soln.

TODO:
hash solns to exclude repetitive solns of commutative operations
example:
10 + 10 + 2 + 2
10 + 2 + 10 + 2 <- repetitive
