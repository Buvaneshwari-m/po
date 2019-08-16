u1,lo2=map(int,input().split())
uu3=list(map(int,input().split()))
if lo2==1:
    print(min(uu3))
elif lo2==2:
    print(max(uu3[0],uu3[u1-1]))
else:
    print(max(uu3))
