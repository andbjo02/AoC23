import math
s=[x.strip() for x in open(0)]
        
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
  D[a]=(b,c)
 
s=[]
for x in D:
  if x[2]=='A':
    s.append(x)
pd=1
for y in s:
  vis=dict()
  sm=0
  z=y
  c=0
  while (z,c) not in vis:  
    vis[(z,c)]=sm
    x=tar[c]
    c+=1
    if c==len(tar): c=0
 
    if x=='L':
      z=D[z][0]
    else:
      z=D[z][1]
    sm+=1
    if z[2]=='Z':
      dst=sm
  cl=sm-vis[(z,c)]
  if cl!=dst:
    print("Error: shortest distance from start to end and the cycle length differ:",dst,cl)
    print("This solution only works when they are equal (as in my input)")
  pd=(pd*cl)//math.gcd(pd,cl)    

print(pd)

