# Write code for algorithm 2 below

# Write a function that prints the natural numbers from 1 to n

def count_up(n):
     # Base Case
     if n == 0:
          return
     # Recursinve Case
     count_up(n - 1)
     print(n)

# test case
print(count_up(5))