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

sm=0

adj=dict()
default=dict()     
for x in s[0]:
  y=x.split('{')
  nm=y[0].strip()
  adj[nm]=[]
  
  z=y[1].strip('}').split(',')
  for q in z[:-1]:
    w=q.split(':')
    cnd=w[0]
    res=w[1]
    adj[nm].append((cnd,res))
    #print(cnd,res)
  default[nm]=z[-1]

V=dict()
V['x']=[1]*4001
V['m']=[1]*4001
V['a']=[1]*4001
V['s']=[1]*4001
sm=0

def push(start,V):
  global sm
  if start=='R':
    return
  if start=='A':
    pr=1
    w=[]
    for y in V:
      ant=0
      for i in range(1,4001):
        if V[y][i]==1:
          ant+=1
      w.append(y+':'+str(ant))    
      pr*=ant
    sm+=pr
  else:           
    for cnd,res in adj[start]:
      w=cnd.split('<')
      if len(w)>1:
        a=w[0]
        v=int(w[1])
        Q=dict()
        for y in V:
          Q[y]=V[y][:]
        for i in range(v,4001):
          Q[a][i]=0
        push(res,Q)
        for i in range(1,v):
          V[a][i]=0  
      else:
        w=cnd.split('>')
        a=w[0]
        v=int(w[1])
        Q=dict()
        for y in V:
          Q[y]=V[y][:]
       
        for i in range(1,v+1):
          Q[a][i]=0
        push(res,Q)
        for i in range(v+1,4001):
          V[a][i]=0  
    Q=dict()
    for y in V:
      Q[y]=V[y][:] 
    push(default[start],Q)
    
push('in',V)
print(sm)

