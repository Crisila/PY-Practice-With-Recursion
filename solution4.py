# Write code for algorithm 4 below

#  Write a function that calculates the value of 'a' to the power of 'b'.

def exponents (a, b): 
     # Base Case
     if b == 0: # 0^0 = 1
          return 1 
     # Recursinve Case
     return a * exponents(a, b - 1)

print(exponents(3, 3))