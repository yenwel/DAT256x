import numpy as np
eqs = np.array([[2,1,13],[10,-2,44]])
print(eqs)
print(eqs[0]*5)
eqs[0] = eqs[0]*5
print(eqs[0]- eqs[1])
eqsy = eqs[0]- eqs[1]
print(eqsy[2]/eqsy[1])
y = eqsy[2]/eqsy[1]
eqsx = eqs[0]
print(eqsx)
print((eqsx[2]-(eqsx[1]*y))/eqsx[0])

eqs = np.array([[2,3,23],[1,4,24]])
print(eqs)
print(eqs[1]*2)
eqs[1] = eqs[1]*2
print(eqs[0]- eqs[1])
eqsy = eqs[0]- eqs[1]
print(eqsy[2]/eqsy[1])
y = eqsy[2]/eqsy[1]
eqsx = eqs[0]
print(eqsx)
print((eqsx[2]-(eqsx[1]*y))/eqsx[0])