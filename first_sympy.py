import numpy, sympy

from sympy import symbols, expand, factor

print(sympy.sqrt(16))

print(numpy.sqrt(3)) # => 1.73205080757
print(sympy.sqrt(3))

print(numpy.sqrt(8))
print(sympy.sqrt(8)) # => simplifies symbolically: 2*sqrt(2)



x, y = symbols('x y')
expr = x + 2*y
print(expr)

print(expr + 1)
print(expr - x)

new_expr = expr * x
expanded_expr = (expand(new_expr))
print("%s : the expression is expanded." %expanded_expr)

factored_expr = (factor(expanded_expr))
print("%s : the expansion reverts back to factored form." %factored_expr)

 
