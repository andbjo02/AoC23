import heapq
s=[[y for y in x.strip()] for x in open(0)]

H=len(s)
W=len(s[0])

dx=[1,0,-1,0]
dy=[0,1,0,-1]

INF=1<<62

tab=dict()

for x in range(W):
  for y in range(H):
    lst=[]
    for k in range(4):    
      nx=x+dx[k]
      ny=y+dy[k]
      if s[ny%H][nx%W]!='#':
        lst.append((nx,ny))
    tab[(x,y)]=lst

def getnxt(xy):
  nxy=[]
  for x,y in xy:
    mx=x % W
    my=y % H
    dvx=x//W
    dvy=y//H
    for nx,ny in tab[(mx,my)]:
      nxy.append((nx+dvx*W,ny+dvy*H))
  nxy=set(nxy)
  nxy=list(nxy)
  return nxy
 
sm=0
for y in range(H):
  for x in range(W):
    if s[y][x]=='S':
      sx=x
      sy=y
xy=[(sx,sy)]
for i in range(64):
  xy=getnxt(xy)

print(len(xy))

