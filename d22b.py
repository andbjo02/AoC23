s=[x.strip() for x in open(0)]

sm=0

def coords(q):
  w=list(map(int,q.split(',')))
  return w

xys=[]     
for w in s:
  q=w.split('~')
  xys.append((coords(q[0]),coords(q[1])))

xys=[(q[0][2],q) for q in xys]
xys.sort()
xys=[q[1] for q in xys]
          
D=dict()
def empty(z,xy0,xy1):
  S=set()
  for x in range(xy0[0],xy1[0]+1):
    for y in range(xy0[1],xy1[1]+1):
      if (x,y,z) in D:
        S.add(D[(x,y,z)])
  return S
  
def insert(zo,xy0,xy1,who):
  global D
  zo2=xy1[2]-xy0[2]+1
  for x in range(xy0[0],xy1[0]+1):
    for y in range(xy0[1],xy1[1]+1):
      D[(x,y,zo+zo2)]=who
def remove(zo,xy0,xy1,who):
  global D
  zo2=xy1[2]-xy0[2]+1
  for x in range(xy0[0],xy1[0]+1):
    for y in range(xy0[1],xy1[1]+1):
      del D[(x,y,zo+zo2)]  

for i in range(len(xys)):
  b1,b2=xys[i]
  insert(b1[2]-1,b1,b2,i)

again=True
loc=[0]*len(xys)
for i in range(len(xys)):
  b1,b2=xys[i]  
  loc[i]=b1[2]-1
  
while again:
  again=False
  for i in range(len(xys)):
    b1,b2=xys[i]  
    z=loc[i]
    while z>0 and len(empty(z,b1,b2))==0:
      remove(z,b1,b2,i) 
      z-=1
      insert(z,b1,b2,i) 
      again=True
      loc[i]=z
           
adj=[[] for _ in range(len(xys))]
for i in range(len(xys)):
  b1,b2=xys[i]  
  z=loc[i]
  S=empty(z,b1,b2)
  
  for x in S:
    adj[x].append(i)

best=0  
for j in range(len(xys)):
  cnt=0
  lst=[j]
  sup=[0]*len(xys)
  for i in range(len(xys)):
    b1,b2=xys[i]  
    z=loc[i]
    S=empty(z,b1,b2)
    sup[i]=len(S)
    
  while len(lst):
    who=lst.pop()
    for x in adj[who]:
      sup[x]-=1
      if sup[x]==0:
        lst.append(x)
        cnt+=1
  sm+=cnt    

print(sm)

