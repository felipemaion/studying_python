import matplotlib.pyplot as plt

def modulo(x):
    return x if x >= 0 else -x
    
y = []
xs = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
for x in xs:
    y.append(modulo(x-4))
plt.plot(xs,y)
plt.show()