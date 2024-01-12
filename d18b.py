s=[x.strip() for x in open(0)]
# Gauss shoelace formula for polygon area
x=0
y=0
xs=[x]
ys=[y]
dirs="RDLU"
dx=[1,0,-1,0]
dy=[0,1,0,-1]
sm=1
for w in s:
  d,a,c=w.split()
  d=int(c[-2])
  a=int(c[2:-2],16)
  x+=a*dx[d]
  y+=a*dy[d]
  xs.append(x)
  ys.append(y)
  if d<2: sm+=a
ar=0 
for i in range(1,len(xs)-1):
  dx1=xs[i]-xs[0]
  dy1=ys[i]-ys[0] 
  dx2=xs[i+1]-xs[i]
  dy2=ys[i+1]-ys[i]  
  ar+=dx1*dy2-dx2*dy1
ar//=2
sm+=ar
print(sm)
