import random, sys
from cogent import LoadSeqs, DNA, LoadTree
from cogent.phylo import distance, nj
from cogent.evolve.models import F81, JC69
import numpy as np
import matplotlib.pyplot as plt
debug = False

# true tree is:  ((A,B),(C,D))
# alignment that is consistent:  AAGG
# alignment that is not:         AGAG
# uninformative alignment:       AAAA
tr = LoadTree(treestring='((A,B),(C,D));')

def makeAlignment(pro,con,neutral):
    seqs = list()
    for otu in 'ABCD':
        temp = ['A'*neutral]
        if otu in 'AB':  temp.append('A'*pro)
        else:            temp.append('G'*pro)
        if otu in 'AC':  temp.append('T'*con)
        else:            temp.append('C'*con)
        seqs.append(''.join(temp))
    return seqs
    
def sample(seqs):
    N = len(seqs[0])
    iL = [random.choice(range(N)) for j in range(N)]
    rL = list()
    for seq in seqs:
        temp = [seq[i] for i in iL]
        rL.append(''.join(temp))
    return rL
    
def evaluate_tree(aln):
    d = distance.EstimateDistances(aln, submodel=JC69())
    d.run(show_progress=False)
    njtree = nj.nj(d.getPairwiseDistances())
    if debug:
        print (d)
        print (njtree.asciiArt())
        print (njtree.sameTopology(tr))
        for otu in 'BCD':
            print (njtree.getConnectingEdges('A',otu))
    L = njtree.getConnectingEdges('A','B')
    return len(L) == 3

R = [35,40,42,44] + range(44,57) + [58,60,65]
C = []
for con in R:
    pro = 100 - con
    seqs = makeAlignment(pro,con,0)
    if debug:
        print ('\n'.join(seqs))
    count = 0
    reps = 100

    for i in range(reps):
        #print i
        s = sample(seqs)
        #print '\n'.join(s)
        dna = dict(zip('ABCD',s))
        aln = LoadSeqs(data=dna, moltype=DNA)
        if evaluate_tree(aln):  count += 1
    C.append(count*1.0/reps)
    print (con, count, reps)

plt.scatter(R,np.array(C),s=250)
ax = plt.axes()
ax.set_xlim(30,70)
ax.set_ylim(-0.05,1.05)
plt.savefig('example.png')
