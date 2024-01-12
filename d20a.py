from collections import deque
s=[x.strip() for x in open(0)]

rem=dict() 
cnt=[0]*2
def signal(a,par,v):
  global val,rem,cnt
  h=deque()
  h.append((a,par,v))
  
  while len(h):
    a,par,v=h.popleft()
    
    cnt[v]+=1
    if a not in typ: continue
   
    if typ[a]=='%':
      if v==0:
        val[a]=1-val[a]
        for nxt in adj[a]:
          h.append((nxt,a,val[a]))
    if typ[a]=='&':
      rem[a][par]=v
      found=True
      for w in rem[a]:
        if rem[a][w]==0:
          found=False
          break
      if found:
        v=0
      else:
        v=1  
      for nxt in adj[a]:
        h.append((nxt,a,v))          
    if typ[a]=='.':
      for nxt in adj[a]:
        h.append((nxt,a,v))          
              
adj=dict()
val=dict()  
typ=dict() 
 
for x in s:
  y=x.split('->')
  w=y[0].strip()
  if w=="broadcaster":
    a=w
    t='.'
  else:  
    t=w[0]
    a=w[1:]
  if a not in adj:
    adj[a]=[]
    val[a]=0  
   
  z=y[1].split(',')
  for q in z:
    w=q.strip()
    adj[a].append(w)
    if w not in rem:
      rem[w]=dict()
    if a not in rem[w]:
      rem[w][a]=0
  typ[a]=t
  
for i in range(1000):
  signal("broadcaster","button",0)
print(cnt[0]*cnt[1])

