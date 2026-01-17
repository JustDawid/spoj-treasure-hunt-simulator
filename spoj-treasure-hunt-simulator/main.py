import random as rd

def skrot(x, y):
    if x > y:
        x -= y
        return x
    elif x < y:
        y -= x
        return y
    else:
        return 0
    
# 0-N, 1-S, 2-W, 3-E
N = 0
S = 0
E = 0
W = 0

for i in range(4):
    kierunek = rd.randint(0,3)
    kroki = rd.randint(1,6)
    print(kierunek, kroki)
    if kierunek == 0:
        N += kroki
    elif kierunek == 1:
        S += kroki
    elif kierunek == 2:
        E += kroki
    else:
        W += kroki

if skrot(N, S) == 0 and skrot(E, W) == 0:
    print("Studnia")
else:
    print("N" if N > S else "S", skrot(N, S), "E" if E > W else "W", skrot(E, W))
