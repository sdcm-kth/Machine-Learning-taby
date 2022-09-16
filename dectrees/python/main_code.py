
import monkdata as m
import dtree as dt
import drawtree_qt5 as dwt5
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import drawtree_qt5 as qt

monks = [m.monk1, m.monk2, m.monk3]
monks_test = [m.monk1test, m.monk2test, m.monk3test]

# Assignment 0

# Assignment 1
entropy = [dt.entropy(monks[0]), dt.entropy(monks[1]), dt.entropy(monks[2])]
for x in range(len(entropy)):
    print("Entropy of dataset MONK-{}: {}".format(x+1,entropy[x]))
print()
# Assignment 2

# Assignment 3
def avGain(data):
    aveGain = [] 
    for i in range(6):
        aveGain.append(round(dt.averageGain(data,m.attributes[i]),5))
    return aveGain
AG_1 = avGain(monks[0]); AG_2 = avGain(monks[1]); AG_3 = avGain(monks[2])
AG = [AG_1[4], AG_2[4], AG_3[1]]
for x in range(len(AG)) :
    print("Average gain {} of maximized attribute for dataset MONK-{} ".format(AG[x],x+1))
print()

# Assignment 4
E_Sk = [ entropy[0]- AG_1[4],entropy[1] - AG_2[4],entropy[2] - AG_3[1]]
for x in range(len(E_Sk)):
    print("E[Sk] of dataset MONK-{}: {}".format(x+1,E_Sk[x]))
print()

# Assignment 5

for i in range(3):
    t = dt.buildTree(monks[i],m.attributes)
    error_train = (1 - dt.check(t, monks[i]))
    error_test = (1 - dt.check(t, monks_test[i]))
    print("Train set error for MONK-{} dataset: {}".format(i+1,error_train))
    print("Test set error for MONK-{} dataset: {}\n".format(i+1,error_test))

print ()

# Assignment 6
# no need
# Assignment 7

