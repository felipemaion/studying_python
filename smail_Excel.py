import  pandas as pd
# input data....
df = pd.read_excel("Flowr.xlsx",'outp')
''' Reading the columns'''
vsl = df['VSL'].tolist()
vsg = df['VSG'].tolist()
Reg = df['Reg'].tolist()  # this is a list of words
#
# print(vsl)
# print(vsg)
# print(Reg)
# [4.7, 4.7, 4.7, 55.0, 4.69, 4.69, 4.69, 4.69, 4.68, 4.68, 4.68]
# [2.06, 2.19, 2.33, 2.48, 2.66, 2.85, 3.06, 3.29, 3.56, 3.87, 4.22]
# ['Mist', ' Wavy', ' Slug', ' INT', ' INT', ' INT', ' INT', ' INT', ' INT', ' INT', ' NOT']
# if we asume that is my data

# vsl = [4.7, 4.7, 4.7, 55, 4.69, 4.69, 4.69, 4.69, 4.68, 4.68, 4.68]
# vsg = [2.06, 2.19, 2.33, 2.48, 2.66, 2.85, 3.06, 3.29, 3.56, 3.87, 4.22]
# Reg = ['Mist', 'Wavy', 'Slug', 'INT', 'INT', 'INT', 'INT', 'INT', 'INT', 'INT', 'NOT']

INTl = []  # corespending to vsl
INTg = []  # corespending to vsg

count = -1
for item in Reg:
    count += 1
    if item == "INT":
        ll = vsl[count]
        gg = vsg[count]
        INTl.append(ll)
        INTg.append(gg)

print(INTl)
print(INTg)