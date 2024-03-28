# Write code for algorithm 1 below

# Write a program that takes a positive number as an argument and prints the numbers from n to zero.


def count_down(n):
     # Base Case
     if n == 0:
          return
     # Recursinve Case
     print(n)
     count_down(n - 1)

# test case
print(count_down(5)) 