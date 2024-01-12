s=[x.strip() for x in open(0)]
sm=0

w=['zero','one','two','three','four','five','six','seven','eight','nine']

for x in s:
  t=0
  first=True
  for i in range(len(x)):
    for j in range(len(w)):
      if x[i:i+len(w[j])]==w[j]:
        if first:
          first=False
          t=t*10+j
        r=j
    if x[i]>='0' and x[i]<='9':
      if first:
        first=False
        t=t*10+ord(x[i])-48  
      r=ord(x[i])-48
  t=t*10+r    
  sm+=t            
print(sm)


