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
  default[nm]=z[-1]

for x in s[1]:
  y=x[1:-1].split(',')
  V=dict()
  for z in y:
    q=z.split('=')
    v=int(q[1])
    a=q[0]
    V[a]=v
  start='in'
  
  while start!='A' and start!='R':
    found=False
    for cnd,res in adj[start]:
      w=cnd.split('<')
      if len(w)>1:
        a=w[0]
        v=int(w[1])
        if V[a]<v:
          found=True
          who=res
          break
      else:
        w=cnd.split('>')
        a=w[0]
        v=int(w[1])
        if V[a]>v:
          found=True
          who=res
          break
    if not found:
      start=default[start]   
    else:
      start=who  
  if start=='A':
    ant=0
    for x in V:
      ant+=V[x]
    sm+=ant
print(sm)

