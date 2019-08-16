import sys, string, math

jiva = int(input())
kfc = [ int(x) for x in input().split()]
bhoro = []
dup = []
sintey = []
for i in range(1,jiva+1) :
    if i not in kfc:
        bhoro.append(i)
for i in kfc :
    if kfc.count(i) > 1 and i not in dup :
        dup.append(i)
for i in range(0,jiva) :
    if kfc[i] in dup :
        sintey.append(i)
tom = len(bhoro)
for i in range(0,jiva) :
    if len(bhoro) == 0 :
        break
    if i in sintey :
        if i == sintey[0] :
            if bhoro[0] < kfc[i] :
                kfc[i] = bhoro.pop(0)
                sintey.pop(0)
            elif kfc[i] in dup :
                sintey.pop(0)
                dup.remove(kfc[i])
            else :
                kfc[i] = bhoro.pop(0)
                sintey.pop(0)


print(tom)
print(*kfc)
