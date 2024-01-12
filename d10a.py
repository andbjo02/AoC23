import heapq
s=[[y for y in x.strip()] for x in open(0)]
  
H=len(s)
W=len(s[0])

d="|-LJ7FS"
adj=[[3,1],[2,0],[3,0],[3,2],[1,2],[1,0],[0,1,2,3]]
dx=[1,0,-1,0]
dy=[0,1,0,-1]

INF=1<<62

cnt=0
def longest(sx,sy,ox,oy):
  global cnt
  vis=[[INF]*W for _ in range(H)]
  h=[(0,sx,sy,ox,oy)]
  vis[sy][sx]=0
  while len(h):
    cst,x,y,ox,oy = heapq.heappop(h)
    if cst==vis[y][x]:    
      for t in adj[d.index(s[y][x])]:
        nx=x+dx[t]
        ny=y+dy[t]
       
        if nx>=0 and nx<W and ny>=0 and ny<H:
          if s[ny][nx] in d:
            if nx!=ox or ny!=oy:
              ncst=cst+1
              if ncst<vis[ny][nx]:
                vis[ny][nx]=ncst
                if nx!=sx or ny!=sy:
                   heapq.heappush(h,(ncst,nx,ny,x,y))                       
  return vis

sm=0
for y in range(H):
  for x in range(W):
    if s[y][x]=='S':
      sx=x
      sy=y
 
best=INF
for g in range(6):
  con=0
  s[sy][sx]=d[g]
  for k in adj[g]:
    nx=sx+dx[k]
    ny=sy+dy[k]
    if s[ny][nx] in d:
      for k in adj[d.index(s[ny][nx])]:
        nx2=nx+dx[k]
        ny2=ny+dy[k]
        if nx2==sx and ny2==sy:
          con+=1
  if con==2:        
    vis=longest(sx,sy,-1,-1)
    worst=0
    for y in range(H):
      for x in range(W):
        if s[y][x] in d and vis[y][x]!=INF:
          worst=max(worst,vis[y][x])
    break
print(worst)      

