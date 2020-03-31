# Assignment 2: Evaluating Expressions Using Stacks

## 1. Overview  

For this project, you will implement a program to evaluate an infix
expression, the kind of expression used in standard arithmetic.  The
program will do this is two steps, each step implemented as a separate
Python function:

1. Convert the infix expression to a postfix expression.
1. Evaluate the postfix expression

Both these steps make use of a stack in an interesting way.  Many
language translators (e.g. compiler) do something similar to convert
expressions into code that is easy to execute on a computer.

Section 3.9 of the text has a detailed discussion of this material that
you should read carefully before building your implementation.  For this
assignment, you will use an implementation of the Abstract Data Type
Stack. Your programs should work with either implementation from Lab 2 –
the one based on a linked data structure or the one based on Python’s
List data type, but for consistency with grading, use the stack_array.py
implementation.

Notes: 
* Postfix expressions will only consist of numbers (integers, reals, positive or negative) and the five operators separated by spaces.  You may assume a capacity of 30 for the Stack will be sufficient for any expression that your programs will be required to handle.
* The text discusses an easier version of this problem in detail.  You should read it carefully before proceeding.  In addition to the operators + - * / shown in the text, your programs should handle the exponentiation operator.  In this assignment, the exponential operator will be denoted by ^.  For example, 2^3→8 and 3^2→9.  (https://en.wikipedia.org/wiki/Exponentiation)
* For infix expressions, the exponentiation operator has higher precedence than the * or /.  For example, 2*3^2 = 2*9 = 18 not 6^2=36
* Also, for infix expressions, the exponentiation operator associates from right to left.  The other operators (+,-,*,/) associate left to right. Think carefully about what this means.  For example: 2^3^2 = 2^(3^2) = 2^9 = 512 not (2^3)^2= 8^2=64
* Infix expressions may also have parentheses - consider that for the infix_to_postfix() function.
* Every class and function must come with a brief purpose statement in its docstring. In separate comments you should explain the arguments and what is returned by the function or method. 
* You must provide test cases that completely test all functions.  
* Use descriptive names for data structures and helper functions.  You must name your files and functions (methods) as specified below.
* You will not get full credit if you use built-in functions beyond the basic built in operations unless they are explicitly stated as being allowed.  If you are in doubt – ask.

## 2. Modules and Functions

Your code will be contained in these two files:

* exp_eval.py
* exp_eval_testcases.py

As a starting point, you should download the files with those names from
PolyLearn.  As noted above, you will also need a stack – use the
stack_array implementation.  Tip: For strings that are passed in as
arguments, use the split function to convert the input to a list of
tokens.  To turn a list into a string, use the join function.

Functions in exp_eval.py that will be tested when grading your submission:

```
def infix_to_postfix(input_str):
"""Converts an infix expression to an equivalent postfix expression"""

"""Input argument:  a string containing an infix expression where tokens are 
   space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
   Returns a String containing a postfix expression """

def postfix_valid(input_str):
"""Determines if input string contains a valid postfix expression"""

"""Input argument:  a string containing a candidate postfix expression where tokens are 
   space separated.  Tokens are either operators + - * / ^ or numbers
   Returns True if the string is a valid postfix expression, False otherwise"""

def postfix_eval(input_str):
"""Evaluates a postfix expression"""

"""Input argument:  a string containing a valid postfix expression where tokens 
   are space separated.  Tokens are either operators + - * / ^ or numbers
   Returns the result of the expression evaluation"""
```

You may write as many helper functions as you would like.

### 3. Tests
* Write sufficient tests using unittest to ensure full functionality and
  correctness of your program.
* Make sure that your tests test each branch of your program and any
  edge conditions.  You do not need to test for correct input in the
  assignment, other than what is specified above.
* You may assume that when infix_to_postfix(infix_expr) is called that
  infix_expr is a well formatted, correct infix expression containing
  only numbers, the specified operators, parentheses () and that the
  tokens are space separated.  You may use the Python functions split
  and join.
* You can assume that the user will use postfix_valid(input_str) prior
  to calling the postfix evaluation function, so
  postfix_eval(postfix_expr) will always be called with a valid postfix
  expression
* postfix_eval(postfix_expr) should raise a ValueError if a divisor is 0. 

### 4. Submission

Submit two files to PolyLearn: exp_eval.py and exp_eval_testcases.py

