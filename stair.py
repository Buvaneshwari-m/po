bu2=int(input())
c1=list(map(int,input().split()))
ho=0
for m in range(0,bu2):
	for l in range(0,m):
		if c1[l]<c1[m]:
			ho=ho+c1[l]
print(ho)
