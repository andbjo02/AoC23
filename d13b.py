s=[x.strip() for x in open(0)]
        
def part(s):
  t=[]
  l=[]
  for x in s:
    if x!="":
      t.append(x)
    else:
      l.append(t)
      t=[]
  if len(t): l.append(t)
  return l

s=part(s)

def find(x):
  xx=[]
  yy=[]
  for d in range(H-1):
    sol=True
    for k in range(min(d,H-d)+1):
      if d-k<0 or d+k+1>=H: break
      for l in range(W):
        if x[d-k][l]!=x[d+k+1][l]:
          sol=False
          #print(k)
          break
  
    if sol: yy.append(d+1)
  for d in range(W-1):
    sol=True
    for k in range(min(d,W-d)+1):
      if d-k<0 or d+k+1>=W: break
      for l in range(H):
        if x[l][d-k]!=x[l][d+k+1]:
          sol=False
          break
   
    if sol: xx.append(d+1)
  return (xx,yy)
      
sm=0
for x in s:
  H=len(x)
  W=len(x[0])
  y=[]
  for q in x:
    y.append([d for d in q])
  a=y  
  
  hx,hy=find(a)
  
  taken=False
  for ny in range(H):
    for nx in range(W):
      if a[ny][nx]=='.':
        a[ny][nx]='#'
        (gx,gy)=find(a)
        a[ny][nx]='.'
      else:
        a[ny][nx]='.'
        (gx,gy)=find(a)
        a[ny][nx]='#'
      if not taken:
        found=False
       
        for p in gx:
          if p not in hx:
            found=True
            sm+=p
        if  not found:
          for p in gy:
            if p not in hy:
              found=True
              sm+=100*p
        if found: taken=True

print(sm)
  
