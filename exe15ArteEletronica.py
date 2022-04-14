# _______________
# |           __|___
# |          |      |
# |          R      R1
# +          |      |
# V          ---|----   
# -             |
# |             |  
# |_____________|

V = 15 # 15V
R = 1000 # 1k
# Achar P em R.
def potencia(R1=1000, V=15,R=1000):
    Req = (1/R + 1/R1)**-1
    print("Req:", Req)
    I = V / Req
    print("I:", I)
    print("Preq:", V*I)
    # I = Ir + I1
    # I = Vr/ R + V1/R1
    # I = V / R + V/R1
    # I = V*(1/R + 1/R1)
    # V/Req = V*(1/R + 1/R1)
    # V**2/Req = V**2(1/R + 1/R1)
    # P = Pr + Pr1
    Pr = V**2/R
    Pr1 = V**2/R1
    P = Pr + Pr1
    print("P:", P, "Pr:", Pr, "Pr1:", Pr1)
    return P


potencia(1000)