import numpy as np

p = input("Fill five letter word P in: ")
pp = list(p)
Pi = np.array(pp)
print(Pi)
P = np.char.lower(Pi)

q = input("Fill five letter word Q in: ")
qq = list(q)
Qi = np.array(qq)
print(Qi)
Q = np.char.lower(Qi)

i = 0;

while i <= 5:
    if P[i] == Q[i]:
        print(1)
    else:
        print(0)
    i += 1
