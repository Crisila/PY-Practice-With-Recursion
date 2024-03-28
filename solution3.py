# Write code for algorithm 3 below

# Write a function that returns the nth elements in the Fibonacci Sequence

def fibonacci(n):
     # Base Case
     if n == 0:
          return 0
     if n == 1:
          return n
     # Recursinve Case
     return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(9))   # Output: 34