import math

s=[x.strip() for x in open(0)]

INF=1<<62

pts=[]     
for i in range(len(s)):
  x=s[i]
  y=x.split('@')
  xys=list(map(int,y[0].split(',')))
  ang=list(map(int,y[1].split(',')))
  pts.append((xys,ang))

def findprimesols(PRIME):
  sols=[]
  for t0 in range(PRIME):
    i=0      
    x,y,z=pts[i][0]
    dx,dy,dz=pts[i][1]
    #Guess
    gx=(x+t0*dx) % PRIME
    gy=(y+t0*dy) % PRIME
    gz=(z+t0*dz) % PRIME
    j=1
    x2,y2,z2=pts[j][0]
    dx2,dy2,dz2=pts[j][1]   
    for t1 in range(PRIME):
      if t1!=t0:
        hx=(x2+dx2*(t1)) % PRIME
        hy=(y2+dy2*(t1)) % PRIME
        hz=(z2+dz2*(t1)) % PRIME
        ddx=(hx-gx) % PRIME
        ddy=(hy-gy) % PRIME
        ddz=(hz-gz) % PRIME
        deltat=t1-t0
        deltat=pow(deltat,-1,PRIME)
        ddx=(ddx*deltat) % PRIME
        ddy=(ddy*deltat) % PRIME
        ddz=(ddz*deltat) % PRIME
        
        cx=(gx-t0*ddx) % PRIME
        cy=(gy-t0*ddy) % PRIME
        cz=(gz-t0*ddz) % PRIME
        found=True
        for k in range(len(pts)):
          x3,y3,z3=pts[k][0]
          dx3,dy3,dz3=pts[k][1]
          sol=False
          for t2 in range(PRIME):
            rx=(x3+dx3*t2) % PRIME
            ry=(y3+dy3*t2) % PRIME
            rz=(z3+dz3*t2) % PRIME
                   
            px=(cx+ddx*t2) % PRIME
            py=(cy+ddy*t2) % PRIME
            pz=(cz+ddz*t2) % PRIME
            if px==rx and py==ry and pz==rz:
              sol=True
              break
          if not sol:
            found=False
            break    
        if found:
          sols.append((cx,cy,cz))
  return sols

def crt(c):
  skip=1
  sm=0
  for r,m in c:
    while sm%m!=r:
      sm+=skip
    skip*=m//math.gcd(skip,m)
  return sm
  
MAXN=100
primes=[]
for p in range(2,MAXN):
  q=2
  while q*q<=p and p%q!=0:
    q+=1
  if q*q>p:
    primes.append(p)
      
sieve=[0]*MAXN     
res=[]   
for p in primes:
  if p>10:
    q=findprimesols(p)
    if len(q)==1:
      res.append((p,q[0]))
      if len(res)>10:
        break
ans=[]
for j in range(3):
  c=[]  
  for i in range(len(res)):
    c.append((res[i][1][j],res[i][0]))   
  ans.append(crt(c))
print(sum(ans))    
            
