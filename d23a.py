from collections import deque
s=[[y for y in x.strip()] for x in open(0)]
import sys
sys.setrecursionlimit(100000)

H=len(s)
W=len(s[0])

dx=[1,0,-1,0]
dy=[0,1,0,-1]

INF=1<<62

sm=0

sx=1
sy=0

vis=[[-1]*W for _ in range(H)]
h=deque()
h.append((0,sx,sy))

def inside(x,y):
  if x>=0 and x<W and y>=0 and y<H:
    if s[y][x]!='#' and vis[y][x]==-1:
      return True
  return False

best=0
def find(cnt,x,y):
  global best
  if y==H-1:
    if cnt>best:
      best=cnt
  else:    
    if s[y][x]=='>':
      ny=y
      nx=x+1
      if inside(nx,ny):
        vis[ny][nx]=cnt+1
        find(cnt+1,nx,ny)
        vis[ny][nx]=-1
    elif s[y][x]=='<':
      ny=y
      nx=x-1
      if inside(nx,ny):
        vis[ny][nx]=cnt+1
        find(cnt+1,nx,ny)
        vis[ny][nx]=-1
    elif s[y][x]=='^':
      ny=y-1
      nx=x
      if inside(nx,ny):
        vis[ny][nx]=cnt+1
        find(cnt+1,nx,ny)
        vis[ny][nx]=-1
    elif s[y][x]=='v':
      ny=y+1
      nx=x
      if inside(nx,ny):
        vis[ny][nx]=cnt+1
        find(cnt+1,nx,ny)
        vis[ny][nx]=-1
    elif s[y][x]=='.':
      for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if inside(nx,ny):
          vis[ny][nx]=cnt+1
          find(cnt+1,nx,ny)
          vis[ny][nx]=-1

lst=[]          
for y in range(H):
  for x in range(W):
    if s[y][x] in ["<",">","v","^"]:
      lst.append((x,y))
find(0,1,0)
print(best)

