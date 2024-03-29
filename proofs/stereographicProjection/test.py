#!/usr/bin/python

from sympy import *

init_printing()

x,y,z,a,b,delta,theta = symbols('x y z a b delta theta')

A_Prime = Matrix([[a+delta],[b],[0]])
B_Prime = Matrix([[a + delta*cos(theta)],[b + delta*sin(theta)], [0]])
P_Prime = Matrix([[a],[b],[0]])

def omega_inverse(vector):
    a = vector[0]
    b = vector[1]
    return (1/(1+a**2+b**2)*Matrix([[2*a],[2*b],[1 - a**2 - b**2]]))

A = omega_inverse(A_Prime)
B = omega_inverse(B_Prime)
P = omega_inverse(P_Prime)

PA = A - P
PB = B - P
normalized_dot_product = PA.dot(PB) / (PA.norm()) * (PB.norm())

pprint('A_Prime = ')
pprint(A_Prime)
pprint('B_Prime = ')
pprint(B_Prime)
pprint('P_Prime = ')
pprint(P_Prime)
pprint('omega_inverse(P_Prime) = ')
pprint(omega_inverse(P_Prime))
pprint('omega_inverse(A_Prime) = ')
pprint(omega_inverse(A_Prime))
pprint('omega_inverse(B_Prime) = ')
pprint(omega_inverse(B_Prime))
pprint('PA = ')
pprint(PA)
pprint('PB = ')
pprint(PB)
pprint('TEST')
pprint(simplify(normalized_dot_product))
