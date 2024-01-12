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
    guess=g
    break
s[sy][sx]=d[guess] 

vis=longest(sx,sy,-1,-1)   

vert='|-LJ7F'
brd=[['.']*(3*W) for _ in range(3*H)]
rep=[[".x.",".x.",".x."],["...","xxx","..."],[".x.",".xx","..."],[".x.","xx.","..."],["...","xx.",".x."],["...",".xx",".x."]]

for y in range(3*H):
  for x in range(3*W): 
    if y%3==1 and x%3==1:
      brd[y][x]='o'
     
for y in range(H):
  for x in range(W): 
       
    if s[y][x] in vert and vis[y][x]<INF:
      cart=vert.index(s[y][x])
      for ddy in range(3):
        for ddx in range(3):
          brd[y*3+ddy][x*3+ddx]=rep[cart][ddy][ddx]
          
sm=0
h=[]
for x in range(3*W):
  h.append((x,0))
  h.append((x,3*H-1))
for y in range(3*H):
  h.append((0,y))
  h.append((3*W-1,y))
  
vis=[[0]*3*W for _ in range(3*H)]
while len(h):
  x,y=h.pop()
  for k in range(4):
    nx=x+dx[k]
    ny=y+dy[k]
    if nx>=0 and nx<3*W and ny>=0 and ny<3*H:
      if brd[ny][nx]!='x' and not vis[ny][nx]:
        vis[ny][nx]=1
        h.append((nx,ny))

sm=0
for y in range(3*H):
  for x in range(3*W): 
    if vis[y][x]==0 and brd[y][x]=='o':
      sm+=1
print(sm)
