# Write code for algorithm 5 below

# Write a function that checks whether a string is a palindrome or not. The program should take in a string and return True if the string is a palindrome and False if not.

def is_palindrome (string):
     # Base Case
     if len(string) == 0 or len(string) == 1:
          return True
     # Recursive Case
     if string[0] == string[-1]:
          return is_palindrome(string[1:-1])
     else:
          return False

# Test cases  
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("evolve"))