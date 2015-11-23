import sympy
#exercises 8.1
x, y = sympy.symbols("x y")
a, b = sympy.symbols("a b")
exprF = x**2*y**3
print exprF
exprG = (exprF, y)
print exprG
exprH = exprF.subs(x, exprF)
print exprH
print "expressions defined"
print exprF, "base"
print sympy.diff(exprF,x)
print sympy.diff(exprF,y)
print exprH, "base"
print sympy.diff(exprH,x)
print sympy.diff(exprH,y)
print exprG, "base"
print [exprG[0].diff(x),exprG[1].diff(x)]
print [exprG[0].diff(y),exprG[1].diff(y)]
print "substitutions"
print [exprF.diff(x).subs(x,a).subs(y,b),
        exprF.diff(y).subs(x,a).subs(y,b)]
print [(exprG[0].diff(x).subs(x,3).subs(y,5),
        exprG[1].diff(x).subs(x,3).subs(y,5)),
      (exprG[0].diff(y).subs(x,3).subs(y,5),
        exprG[1].diff(y).subs(x,3).subs(y,5))]
print [exprH.diff(x).subs(x,3*a**2).subs(y,5*b**3),
        exprH.diff(y).subs(x,3*a**2).subs(y,5*b**3)]