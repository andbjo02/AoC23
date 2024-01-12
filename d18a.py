s=[x.strip() for x in open(0)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

x=0
y=0
D=dict()     
for w in s:
  d,a,c=w.split()
  a=int(a)
  if d=='U':
    d=3
  if d=='D':
    d=1
  if d=='L':
    d=2
  if d=='R':
    d=0
  for i in range(a):
    x=x+dx[d]
    y=y+dy[d]
    D[(x,y)]=c

mnx=100000
mny=100000
mxx=-100000
mxy=-100000
for x,y in D:
  mnx=min(x,mnx)
  mxx=max(x,mxx)
  mny=min(y,mny)
  mxy=max(y,mxy)
B=[['.']*(mxx-mnx+3) for _ in range(mxy-mny+3)]

for y in range(mny,mxy+3):
  for x in range(mnx,mxx+3):    
    if (x,y) in D:
      B[y-mny+1][x-mnx+1]='#'

for y in range(mxy-mny+2,0,-1):
  par=0
  for x in range(mxx-mnx+3):
    if B[y][x]=='#':
      if B[y-1][x]=='.':
        pass
      else:
        par=1-par
    elif par:
      B[y][x]='#'   
sm=0       
for y in range(mxy-mny+3):
  for x in range(mxx-mnx+3):
    if B[y][x]=='#':
      sm+=1
        
print(sm)

