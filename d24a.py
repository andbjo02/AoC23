from fractions import Fraction

s=[x.strip() for x in open(0)]

MINX=200000000000000
MAXX=400000000000000
RNG=1000000000000000

def linecross(l1,l2):
  dx1=l1[2]-l1[0]
  dy1=l1[3]-l1[1]
  dx2=l2[2]-l2[0]
  dy2=l2[3]-l2[1]
  xd=l2[0]-l1[0]
  yd=l2[1]-l1[1]
  det=-dx1*dy2+dx2*dy1
  if abs(det)!=0:
    s=(-dy2*xd+dx2*yd)/det
    t=(-dy1*xd+dx1*yd)/det
    if s>=0 and s<=1 and t>=0 and t<=1:
      return (l1[0]+s*dx1,l1[1]+s*dy1)
    else:
      return [] 
  else:
    return []

sm=0

pts=[]     
for i in range(len(s)):
  x=s[i]
  y=x.split('@')
  xys=list(map(int,y[0].split(',')))
  ang=list(map(int,y[1].split(',')))
  pts.append((xys,ang))
  
for i in range(len(s)):
  for j in range(i+1,len(s)):
    l1=[pts[i][0][0],pts[i][0][1],pts[i][0][0]+pts[i][1][0]*RNG,pts[i][0][1]+pts[i][1][1]*RNG]
    l2=[pts[j][0][0],pts[j][0][1],pts[j][0][0]+pts[j][1][0]*RNG,pts[j][0][1]+pts[j][1][1]*RNG]
    
    fl1=[Fraction(x) for x in l1]
    fl2=[Fraction(x) for x in l2]
    xy=linecross(fl1,fl2)
    
    if len(xy):    
      if xy[0]>=MINX and xy[0]<=MAXX:
        if xy[1]>=MINX and xy[1]<=MAXX:
          sm+=1

print(sm)

