def ehPrimo(n):
    for d in range(2, int(n**.5) + 1):                      
        if n % d == 0:                             
            return False
    return True 


def maiorPrimo(num):
    for n in reversed(range(2,num)):
        if ehPrimo(n): print("Maior Primo:", n); return n


ehPrimo(2**82589933 - 1)