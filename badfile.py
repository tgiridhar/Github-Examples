#!/usr/bin/env python3

import sys, os  # Multiple imports on one line

def BADFunctionName():
  # No module-level docstring, no function docstring, poor function name
  import math; A=42  # Multiple statements on one line, single-letter variable
  dict = 10          # Shadowing the built-in 'dict'
  if (A == 42):
        print("The answer to life, universe, and everything!") # Inconsistent indentation
  for i in range(5): print(i)  # Inline statement
  UnUsedVar = "This variable is never used"  
  result= A+dict  
  return result
  
class myclass:  # Class name not in PascalCase
    def __init__(self):
       pass

def main(): print(BADFunctionName())  # Inline statement in a function

if __name__ == "__main__":
  main()
