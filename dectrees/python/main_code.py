
import monkdata as m
import dtree as dt
# Assignment 0

# Assignment 1
e1 = dt.entropy(m.monk1);e2 = dt.entropy(m.monk2);e3 = dt.entropy(m.monk3)
print(e1)
print(e2)
print(e3)
# Assignment 2

# Assignment 3
def avGain(data):
    aveGain = [] 
    for i in range(6):
        aveGain.append(round(dt.averageGain(data,m.attributes[i]),5))
    return aveGain
AG_1 = avGain(m.monk1); AG_2 = avGain(m.monk2); AG_3 = avGain(m.monk3)
print("AG")
print(AG_1[4])
print(AG_2[4])
print(AG_3[1])

# Assignment 4
E_Sk1 = e1- AG_1[4]; E_Sk2 = e2 - AG_2[4] ; E_Sk3 = e3 - AG_3[1]
print("E[Sk]")
print(E_Sk1)
print(E_Sk2)
print(E_Sk3)

# Assignment 5
#dt.select(m.monk1,)
# t=dt.buildTree(m.monk1, m.attributes);
# print(dt.check(t, m.monk1test))
# Assignment 6

# Assignment 7
