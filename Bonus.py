# Write a function that when given two numbers, finds their greatest common divisor.

def gcd(a, b):
     # Base Case
     if b == 0:
          return a
     # Recursive Case
     return gcd(b, a % b)

print(gcd(36, 24))  # Output: 12