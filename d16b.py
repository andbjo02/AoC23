import sys
sys.setrecursionlimit(1000000)

s=[[y for y in x.strip()] for x in open(0)]

H=len(s)
W=len(s[0])

sm=0

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def beam(x,y,d):
  global mp,Tab
  if (x,y,d) in Tab:
    return
  Tab.add((x,y,d))  
  nx=x+dx[d]
  ny=y+dy[d]
  if nx>=0 and nx<W and ny>=0 and ny<H:
    mp[ny][nx]='#'
    if s[ny][nx]=='\\':
      d^=1
      beam(nx,ny,d)
    if s[ny][nx]=='/':
      d=3-d
      beam(nx,ny,d)
    if s[ny][nx]=='|':
      if d==0 or d==2:
        beam(nx,ny,1)
        beam(nx,ny,3)
      else:
        beam(nx,ny,d)
    if s[ny][nx]=='-':
      if d==1 or d==3:
        beam(nx,ny,0)
        beam(nx,ny,2)
      else:
        beam(nx,ny,d)
    if s[ny][nx]=='.':
      beam(nx,ny,d) 

def meas():
  sm=0
  for y in range(H):
    for x in range(W):
      if mp[y][x]=='#':
        sm+=1
  return sm

sm=0  
for y in range(H):
  mp=[['.']*W for y in range(H)]
  Tab=set()
  beam(-1,y,0)
  r=meas()
  sm=max(r,sm)
for y in range(H):
  mp=[['.']*W for y in range(H)]
  Tab=set()
  beam(W,y,2)
  r=meas()
  sm=max(r,sm)  
for x in range(W):
  mp=[['.']*W for y in range(H)]
  Tab=set()
  beam(x,-1,1)
  r=meas()
  sm=max(r,sm)  
for x in range(W):
  mp=[['.']*W for y in range(H)]
  Tab=set()
  beam(x,H,3)
  r=meas()
  sm=max(r,sm)      
print(sm)
  
