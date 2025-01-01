# Uncommon Python Error: Mixing Expected and Unexpected Exceptions

This repository demonstrates a common yet subtle error in Python exception handling, where expected errors (like ZeroDivisionError) are handled alongside unexpected errors (like TypeError).  This can lead to less clear error messages and difficulties in debugging.  The `bug.py` file shows the problematic code; `bugSolution.py` offers improved handling.

## Bug
The `bug.py` file contains a function that attempts to perform division, catching both ZeroDivisionError and TypeError in the same try-except block. While catching ZeroDivisionError is appropriate, lumping in TypeError reduces code clarity and may mask other issues.

## Solution
The `bugSolution.py` file presents a revised approach. The ZeroDivisionError is treated as an expected error, potentially providing a user-friendly alternative. TypeErrors should be treated differently – either checked for before division or handled more effectively (e.g., logging, raising a more specific exception) to ensure robust error handling and maintain code clarity.