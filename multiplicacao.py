def multi(x,n):
     valor = 0
     for _ in range(0,n, int(abs(n)/n)):
             valor = valor + int(abs(n)/n) * x
     return valor
