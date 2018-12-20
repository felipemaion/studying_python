alphabet=['A', 'C', 'G', 'T']
score=[[0, 4, 2, 4, 8], \
       [4, 0, 4, 2, 8], \
       [2, 4, 0, 4, 8], \
       [4, 2, 4, 0, 8], \
       [8, 8, 8, 8, 8]]

def globalAlignment(x, y):
  d=[]

  for i in range(len(x)+1):
    d.append([0]* (len(y)+1))
  for i in range(1, len(x)+1):
    d[i][0]=d[i-1][0] + score[alphabet.index(x[i-1])][-1]
  for i in range(1, len(y)+1):
    d[0][i]=d[0][i-1] + score[-1][alphabet.index(y[i-1])]  
  
  for i in range(1, len(x) +1):
    for j in range(1, len(y)+1):
      distHor = d[i][j-1] + score[-1][alphabet.index(y[j-1])]
      distVer = d[i-1][j] + score[alphabet.index(x[i-1])][-1]
      if x[i-1] == y[j-1]:
        distdiag = d[i-1][j-1]
      else:
        distdiag = d[i-1][j-1] + score[alphabet.index(x[i-1])][alphabet.index(y[j-1])]
 
      d[i][j] = min(distHor, distVer , distdiag)
  
  return d[-1][-1]

x='TACCAGATTCGA'
y='TACCAGATTCGA'

print(globalAlignment(x,y))


