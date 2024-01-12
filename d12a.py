s=[x.strip() for x in open(0)]
sm=0

def gen(y,z,i):
  global ant
  if i==len(y):
    cnt=0
    lst=[]
    for i in range(len(y)):
      if y[i]=='#':
        cnt+=1
      else:
        if cnt:
          lst.append(cnt)
        cnt=0
    if cnt:
      lst.append(cnt)  
    if lst==z:
      ant+=1
  else:                   
    if y[i]=='?':
      y[i]='#'
      gen(y,z,i+1)
      y[i]='.'
      gen(y,z,i+1)
      y[i]='?'
    else:
      gen(y,z,i+1)  

for x in s:
  y,z=x.split()
  z=list(map(int,z.split(',')))
      
  y=[w for w in y]    
  ant=0
  gen(y,z,0)
  sm+=ant
print(sm)

