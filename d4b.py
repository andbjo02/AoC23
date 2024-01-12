s=[x.strip() for x in open(0)]

sm=0

mul=[1]*len(s)
for i in range(len(s)):
  x=s[i]
  y=x.split('|')
  z=y[0].split(':')
  w=list(map(int,z[1].split()))
  q=list(map(int,y[1].split()))
  cnt=0
  for t in w:
    if t in q:
      cnt+=1
  if cnt:    
    for j in range(cnt):
      if i+j+1<len(s):
        mul[i+j+1]+=mul[i]
  sm+=mul[i]
          
print(sm)


