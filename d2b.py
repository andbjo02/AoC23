s=[x.strip() for x in open(0)]

w=["red","green","blue"]
  
sm=0

for x in s:
  E=dict()
  sol=True
  z=x.split(':')
  o=z[0].split()
  ids=int(o[1])
  y=z[1].split(';')
  
  for q in y:
    r=q.split(',')
    for u in r:
      k,l=u.split()
      k=int(k)
      if l not in E:
        E[l]=k
      if k>E[l]: E[l]=k
  p=1
  for y in E:
    p*=E[y]  
  sm+=p  
print(sm)


