import sympy
#exercises 8.2
x, y = sympy.symbols("x y")
a, b = sympy.symbols("a b")
f = sympy.Function("f")
g = sympy.Function("g")
h = sympy.Function("h")
f = x**2*y**3
print f
g = (f, y)
print g
h = f.subs(x,g[0]).subs(y,g[1])
print h