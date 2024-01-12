s=[x.strip() for x in open(0)]

sm=0
for x in s:
  l=list(map(int,x.split()))
  lsts=[l[:]]
  while True:
    w=[]
    for i in range(len(l)-1):
      w.append(l[i+1]-l[i])
    lsts.append(w)
    if min(w)==0 and max(w)==0:
      break
    l=w 
  p=0  
  for i in range(len(lsts)-1,-1,-1):
    lsts[i]=[lsts[i][0]-p]+lsts[i]
    p=lsts[i][0]   
  sm=sm+p   
print(sm)

