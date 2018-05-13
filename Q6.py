def lowest_cell(table):
   
    min_cell = float("inf")
    x, y = -1, -1

    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] < min_cell:
                min_cell = table[i][j]
                x, y = i, j

    return x, y


def join_labels(labels, a, b):
  
    if b < a:
        a, b = b, a

   
    labels[a] = "(" + labels[a] + "," + labels[b] + ")"

    del labels[b]



def join_table(table, a, b): # M, 3,0

    if b < a: # 0 < 3 -> True
        a, b = b, a # a = 0, b=3

    row = []
    for i in range(0, a):
        row.append((table[a][i] + table[b][i])/2)
    table[a] = row
    
   
    for i in range(a+1, b):
        table[i][a] = (table[i][a]+table[b][i])/2
        
   
    for i in range(b+1, len(table)):
        table[i][a] = (table[i][a]+table[i][b])/2
        # Remove the (now redundant) second index column entry
        del table[i][b]

    
    del table[b]


def UPGMA(table, labels):
   
    while len(labels) > 1:
        
        x, y = lowest_cell(table) # (3,0)
        join_table(table, x, y)
        join_labels(labels, x, y)

    
    return labels[0]



def alpha_labels(start, end):
    labels = []
    for i in range(ord(start), ord(end)+1):
        labels.append(chr(i))
    return labels


M_labels = alpha_labels("A", "G")   #A through G
M = [
    [],
    [19],
    [27, 31],
    [8, 18, 26],
    [33, 36, 41, 31]
    ]

# UPGMA(M, M_labels) should output: '((((A,D),((B,F),G)),C),E)'
UPGMA(M,M_labels)


