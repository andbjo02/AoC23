s=[[y for y in x.strip()] for x in open(0)]

H=len(s)
W=len(s[0])

dx=[1,0,-1,0]
dy=[0,1,0,-1]

sm=0

def inside(x,y):
  if x>=0 and x<W and y>=0 and y<H:
    if s[y][x]!='#':
      return True
  return False

for x in range(W):
  if s[0][x]!='#':
    sx=x
  if s[H-1][x]!='#':
    ex=x
lst=[(sx,0),(ex,H-1)]
        
def path(cx,cy,px,py):
  cst=1
  while True:
    for k in range(4):
      nx=cx+dx[k]
      ny=cy+dy[k]
      if inside(nx,ny):        
        if nx!=px or ny!=py:
          cst+=1
          px=cx
          py=cy
          cx=nx
          cy=ny
          break
    if (cx,cy) in lst:
      return cst,lst.index((cx,cy))
            
for y in range(H):
  for x in range(W):
    cnt=0
    if inside(x,y):
      for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if inside(nx,ny):
          cnt+=1
      if cnt>2:    
        lst.append((x,y))
adj=[[] for _ in range(len(lst))]

for i in range(len(lst)):
  x,y=lst[i]
  for k in range(4):
    nx=x+dx[k]
    ny=y+dy[k]
    if inside(nx,ny):
      cnt,dst=path(nx,ny,x,y)
      adj[i].append((cnt,dst))      
best=0
vis=[-1]*len(lst)
def find(cst,who):
  global best
  if who==1:
    if cst>best:
      best=cst
  else:
    for c,nxt in adj[who]:
      if vis[nxt]==-1:
        vis[nxt]=1
        find(cst+c,nxt)
        vis[nxt]=-1
        
find(0,0)            

print(best)      

