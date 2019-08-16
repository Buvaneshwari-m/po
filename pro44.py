buv1,buv2,buv3,buv4=map(int,input().split())
se=list(map(int,input().split()))
gos=[]
for i in range(0,len(se)):
    for j in range(i,len(se)):
        for k in range(j,len(se)):
            gos.append(buv2*se[i]+buv3*se[j]+buv4*se[k])
print(max(gos))
