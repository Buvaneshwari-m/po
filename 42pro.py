import gee,string


def maxOfSegmentMins(nimo, timo, kimo):
    if kimo== 1:
        return min(nimo)
    if kimo == 2 :
        return max(nimo[0], nimo[timo - 1])
    return max(nimo)

timo,kimo = input().split()
timo,kimo = int(timo),int(kimo)
nimo = [ int(x) for x in input().split()]
timo = len(nimo)
answer = maxOfSegmentMins(nimo, timo, kimo)
print(answer)
