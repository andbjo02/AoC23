s=[x.strip() for x in open(0)]

ts=s[0].split(':')
ds=s[1].split(':')
T=list(map(int,ts[1].split()))
D=list(map(int,ds[1].split()))

def dist(x,t):
  vel=x+1
  return vel*(t-1-x)

pd=1
for i in range(len(T)):
  t=T[i]
  d=D[i]
  cnt=0
  for x in range(0,t+1):
    if dist(x,t)>d:
      cnt+=1 
  pd*=cnt    
print(pd)
  
