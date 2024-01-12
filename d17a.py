import heapq

s=[[int(y) for y in x.strip()] for x in open(0)]

H=len(s)
W=len(s[0])

dx=[1,0,-1,0]
dy=[0,1,0,-1]

INF=1<<62

def dijkstra(sx,sy,d):
  vis=[[[[INF]*4 for j in range(4)] for i in range(W)] for _ in range(H)]
  bk=[[[[-1]*4 for i in range(4) ] for j in range(W)] for _ in range(H)]
  h=[(0,sx,sy,0,0),(0,sx,sy,1,0)]
  vis[sy][sx][0][0]=0
  vis[sy][sx][1][0]=0
  
  while len(h):
    cst,x,y,d,r = heapq.heappop(h)
    if cst==vis[y][x][d][r]:
      for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if k==d:
          cr=r+1
          if r==2:
            continue
        else:
          cr=0  
        if (k-d)&3==2:
          continue  
        if nx>=0 and nx<W and ny>=0 and ny<H:
          v=s[ny][nx]
          ncst=cst+v
          if ncst < vis[ny][nx][k][cr]:
            vis[ny][nx][k][cr] = ncst
            bk[ny][nx][k][cr]=(x,y,d,r)
            heapq.heappush(h,(ncst,nx,ny,k,cr))                         
  return vis,bk

vis,bk=dijkstra(0,0,0)

best=1<<62
for i in range(4):
  for j in range(4):
    if vis[-1][-1][i][j]<best:
      best=vis[-1][-1][i][j]
      sd=i
      sc=j
# Find and print solution
if 0:
  y=H-1
  x=W-1
  mx=[[' ']*W for _ in range(H)]
  mx[y][x]='x'
  while bk[y][x][sd][sc]!=-1:
   x,y,sd,sc=bk[y][x][sd][sc]
   mx[y][x]='x'
   
  for i in range(H):
    print("".join(mx[i]))
print(best)
  
