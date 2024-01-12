s=[x.strip() for x in open(0)]

A=[12,13,14]
w=["red","green","blue"]
D=dict()
for i in range(3):
  D[w[i]]=A[i]
  
sm=0

for x in s:
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
      if k>D[l]:
        sol=False
  if sol:
    sm+=ids  
print(sm)


