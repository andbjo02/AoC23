s=[x.strip() for x in open(0)]

order=['A','K','Q','T','9','8','7','6','5','4','3','2','J']

def pts(h):
  D=dict()
  for x in h:
    if x not in D:
      D[x]=0
    D[x]+=1
  
  y=[D[x] for x in D]
   
  y.sort(reverse=True)
  if y[0]==5:
    sc=7
  elif y[0]==4:
    sc=6
  elif y[0]==3 and y[1]==2:
    sc=5
  elif y[0]==3:
    sc=4
  elif y[0]==2 and y[1]==2:
    sc=3
  elif y[0]==2:
    sc=2
  else:
    sc=1
  return sc    
  
def highestpts(x,y,i):
  if i==5:
    return pts(y)
  else:
    z=y
    pt=0
    if x[i]=='J':
      for q in order:
        z=y+q
        f=highestpts(x,z,i+1)
        pt=max(pt,f)
    f=highestpts(x,y+x[i],i+1)
    pt=max(pt,f)    
    return pt
            
sm=0
lst=[]
for x in s:
  c,r=x.split()
  lst.append((c,int(r)))
nlst=[]
for x,y in lst:
  U=[order.index(q) for q in x]
  nlst.append((-highestpts(x,"",0),U,x,y))
nlst.sort(reverse=True)

for i in range(len(nlst)):
  x,y,w,z =nlst[i]
  sm+=z*(i+1)
print(sm)

  


