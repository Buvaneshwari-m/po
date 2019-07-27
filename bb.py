oody,lub = map(int, input().split())
dee = list(map(int, input().split()))
for o in range(lub):
  hun,gim = map(int, input().split())
  print(min(dee[hun-1:gim]))
