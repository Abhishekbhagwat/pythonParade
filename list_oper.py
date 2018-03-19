import random

mainLst = random.sample(range(10),6)
print(mainLst)

print(len(mainLst))
print(max(mainLst))
print(min(mainLst))

mainLst.append(10)
print(mainLst)

print(mainLst.index(10))

mainLst.reverse()
print(mainLst)

mainLst.sort()
