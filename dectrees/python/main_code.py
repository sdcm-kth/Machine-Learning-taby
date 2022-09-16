from re import M
from tkinter import E
import monkdata as m
import dtree as dt
import numpy as np
import random
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
def partition(data, fraction):
  ldata = list(data)
  random.shuffle(ldata)
  breakPoint = int(len(ldata) * fraction)
  return ldata[:breakPoint], ldata[breakPoint:]

def prune_trees(data, test):
  fractions = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
  pruned = []

  for fraction in fractions:
    train, validate = partition(data, fraction)
    tree = dt.buildTree(train, m.attributes)
    forest = dt.allPruned(tree)
    best_perf = dt.check(tree, validate)

    temp_tree = 0
    best_tree = tree

    for t in forest:
      temp_perf = dt.check(t, validate)
      if best_perf < temp_perf:
        best_perf = temp_perf
        best_tree = t

    pruned.append(1 - dt.check(best_tree, test))

  return pruned

fractions = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
monk1_pruned = []
monk3_pruned = []

for i in range(100):
    monk1_pruned.append(prune_trees(m.monk1, m.monk1test))
    monk3_pruned.append(prune_trees(m.monk3, m.monk3test))

monk1_pruned = np.transpose(monk1_pruned)
monk3_pruned = np.transpose(monk3_pruned)

mean1 = np.mean(monk1_pruned, axis=1)
mean3 = np.mean(monk3_pruned, axis=1)
std1 = np.std(monk1_pruned, axis=1)
std3 = np.std(monk3_pruned, axis=1)

MONK1_mean = np.around(mean1, decimals=6)
MONK1_std  = np.around(std1, decimals=6)
MONK3_mean = np.around(mean3, decimals=6)
MONK3_std  = np.around(std3, decimals=6) 
print("Monk1 mean: ")
print(MONK1_mean)
print("Monk1 STD: ")
print(MONK1_std)
print("Monk3 mean: ")
print(MONK3_mean)
print("Monk3 STD: ")
print(MONK3_std)

complete_tree1 = dt.buildTree(m.monk1, m.attributes)
complete_tree3 = dt.buildTree(m.monk3, m.attributes)
Error1 = [1 - dt.check(complete_tree1, m.monk1test), np.amin(mean1)]
Error3 = [1 - dt.check(complete_tree3, m.monk3test), np.amin(mean3)]
print("Error on complete tree vs error on pruned tree")
print(Error1)
print(Error3)

plt.figure()
plt.title('Mean of Errors')
plt.xlabel('Fractions')
plt.ylabel('Mean')
line1, = plt.plot(fractions, mean1, label="MONK1",marker='o')
line3, = plt.plot(fractions, mean3, label="MONK3",marker='o' )
plt.legend()
plt.show()    

plt.title('STD of Errors')
plt.xlabel('Fractions')
plt.ylabel('STD')
line1 = plt.plot(fractions, std1, label="MONK1",marker='o')
line3 = plt.plot(fractions, std3, label="MONK3",marker='o')
plt.legend()

plt.show() 
