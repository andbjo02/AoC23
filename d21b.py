import heapq
s=[[y for y in x.strip()] for x in open(0)]

t=[]
for x in s:
  t.append(x+x)
s=t+t
  
H=len(s)
W=len(s[0])

# Find center
for y in range(H):
  for x in range(W):
    if s[y][x]=='S':
      sx=x
      sy=y

dx=[1,0,-1,0]
dy=[0,1,0,-1]

INF=1<<62
  
def dijkstra(rep,sx,sy):
  vis=[[INF]*rep*W for _ in range(rep*H)]
  sx+=W*(rep//2)
  sy+=H*(rep//2)
  h=[(0,sx,sy)]
  vis[sy][sx]=0
  heapq.heapify(h)
  h=[(0,sx,sy)]
  while len(h):
    cst,x,y=heapq.heappop(h)
    if cst==vis[y][x]:
      for k in range(4):    
        nx=x+dx[k]
        ny=y+dy[k]
        if nx>=0 and nx<rep*W and ny>=0 and ny<rep*H:
          if s[ny % H][nx % W]!='#':
            ncst=cst+1
            if ncst<vis[ny][nx]:
              vis[ny][nx]=ncst
              heapq.heappush(h,(ncst,nx,ny))
  return vis

rep=5 
vis=dijkstra(rep,sx,sy)

RNG=26501365

par=[[0]*rep*W for _ in range(rep*H)]
sm=0
for y in range(rep*H):
  for x in range(rep*W):
    if vis[y][x]<=RNG and (vis[y][x]&1)==RNG&1:
      par[y][x]=1
      sm+=1
      
#       |
#      ABC 
#     -DSE-
#      FGH
#       |

for r in range(1,rep-1):
  # x...
  # x...
  # x...
  for y in range(H):
    for x in range(W):
      if s[y][x]!='#' and par[H*r+y][x]:
        
        dist=vis[H*r+y][x]
        a=(RNG-dist)//W
        if a>0:
          sm+=a
  # ...x
  # ...x
  # ...x
  for y in range(H):
    for x in range(W):
      if s[y][x]!='#' and par[H*r+y][W*(rep-1)+x]:
        dist=vis[H*r+y][W*(rep-1)+x]
        a=(RNG-dist)//W
        if a>0:
          sm+=a
  # xxxx
  # ....
  # ....
  for y in range(H):
    for x in range(W):
      if s[y][x]!='#' and par[y][W*r+x]:
        dist=vis[y][W*r+x]
        a=(RNG-dist)//H
        if a>0:
          sm+=a
  # ....
  # ....
  # xxxx
  for y in range(H):
    for x in range(W):
      if s[y][x]!='#' and par[H*(rep-1)+y][W*r+x]:
        dist=vis[H*(rep-1)+y][W*r+x]
        a=(RNG-dist)//H
        if a>0:
          sm+=a
          
# Corners
for ddy in range(2):
  for ddx in range(2):
    ofx=ddx*W*(rep-1)
    ofy=ddy*H*(rep-1)
    for y in range(H):
      for x in range(W):
        if s[y][x]!='#' and par[ofy+y][ofx+x]: 
          dist=vis[ofy+y][ofx+x]
          a=(RNG-dist)//H
          if a>0:
            sm+=(a+1)*(a+2)//2-1

print(sm)
