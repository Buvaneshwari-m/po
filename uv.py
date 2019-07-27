sky,moon = map(int, input().split())
lst = list(map(int, input().split()))
for i in range(moon):
  juv,ko = map(int, input().split())
  print(min(lst[juv-1:ko]))
