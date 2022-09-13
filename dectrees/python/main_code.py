
import monkdata as m
import dtree as dt
# Assigment 0

# Assigment 1

# Assigment 2

# Assigment 3
def avGain(data):
    aveGain = [] 
    for i in range(6):
        aveGain.append(round(dt.averageGain(data,m.attributes[i]),5))
    return aveGain
print(avGain(m.monk1))
print(avGain(m.monk2))
print(avGain(m.monk3))


# Assigment 4

# Assigment 5

# Assigment 6

# Assigment 7
