import random

s=[x.strip() for x in open(0)]

sm=0

adj=dict()
edges=[] 
for x in s:
  y=x.split(':')
  rt=y[0].strip()
  nxt=list(y[1].split())
  for w in nxt:
    if rt not in adj:
      adj[rt]=[]
    if w not in adj:
      adj[w]=[]  
    adj[rt].append(w)
    adj[w].append(rt)
    edges.append((rt,w))
n=len(adj)
ids=dict()
c=0
for x in adj:
  ids[x]=c
  c+=1

rnk=list(range(n))

def rank(a):
  while a!=rnk[a]:
    tmp=rnk[a]
    rnk[a]=rnk[rnk[a]]
    a=tmp
  return a

def union(a,b):
  ra=rank(a)
  rb=rank(b)
  if ra!=rb:
    rnk[ra]=rb

ITERS=1000
for i in range(ITERS):
  rnk=list(range(n))
  for j in range(n-2):
    a=random.randint(0,len(edges)-1)
    while rank(ids[edges[a][0]])==rank(ids[edges[a][1]]):
      a=random.randint(0,len(edges)-1)
    union(ids[edges[a][0]],ids[edges[a][1]])  
  sm=0
  for j in range(len(edges)):
    a=edges[j]
    if rank(ids[a[0]])!=rank(ids[a[1]]):  
      sm+=1
  if sm==3:
    C=dict()
    for x in range(n):
      if rnk[x] not in C:
        C[rnk[x]]=1
      else:
        C[rnk[x]]+=1
    x=[C[y] for y in C]
    print(x[0]*x[1])        
    exit(0)  
 
