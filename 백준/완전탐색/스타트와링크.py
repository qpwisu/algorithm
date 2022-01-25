from itertools import combinations
n= int(input())
arr = [list(map(int, input().split())) for _ in range(n)]



    
li= [i for i in range(n)]
cl=list(combinations(li,int(n/2)))
m=1000000

for k in range(int(len(cl)/2)):
  start=0
  link=0
  for i in cl[k]:
    for j in cl[k]:
      start+=arr[i][j]
  for i in cl[len(cl)-k-1]:
    for j in cl[len(cl)-k-1]:
      link+=arr[i][j]
  m= min(m,abs(start-link))
print (m)
