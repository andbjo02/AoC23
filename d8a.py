from collections import deque
s=[x.strip() for x in open(0)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def search(sx,sy):
  h=[(sx,sy)]
  
  while len(h):
    x,y=h.popleft()
    for k in range(4):
      nx=x+dx[k]
      ny=y+dy[k]
      if nx>=0 and nx<W and ny>=0 and ny<H:
        h.append((nx,ny))
        
def part(s):
  t=[]
  l=[]
  for x in s:
    if x!="":
      t.append(x)
    else:
      l.append(t)
      t=[]
  if len(t): l.append(t)
  return l

s=part(s)
tar=s[0][0]

sm=0
lst=[]
D=dict()
for x in s[1]:
  w=x.split('=')
  q=w[1].split(',')
  a=w[0][:-1]
  b=q[0][2:]
  c=q[1][1:-1]
  #lst.append((c,int(r)))
  D[a]=(b,c)

s="AAA"

c=0
while s!="ZZZ":
  t=[]
  x=tar[c]
   
  if x=='L':
    s=D[s][0]
  else:
    s=D[s][1]
  c+=1    
  if c==len(tar): c=0 
  sm+=1   
print(sm)

