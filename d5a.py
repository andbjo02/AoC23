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

lsts=[]
seeds=s[0][0].split()
seeds=list(map(int,seeds[1:]))

for i in range(1,len(s)):
  lst=[]
  for j in range(1,len(s[i])):
    d,sr,r=map(int,s[i][j].split())
    lst.append((d,sr,r))
  lsts.append(lst)

val=[]
for sd in seeds:
  x=sd
  for i in range(len(lsts)):
    found=True
    for d,sr,r in lsts[i]:
      if x>=sr and x<sr+r:
        x=d+(x-sr)
        found=True
        break
  val.append(x)
print(min(val))
                
  


