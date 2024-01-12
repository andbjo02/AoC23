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

def lowval(start,stop,dep,v):
  if dep==len(lsts):    
    return start
  else:  
    if v==len(lsts[dep]):
      return lowval(start,stop,dep+1,0)
    else:
      d,sr,r=lsts[dep][v]
      if stop>sr and start<sr+r:
        wstart=max(start,sr)
        wstop=min(stop,sr+r)
        q=lowval(d+wstart-sr,d+wstop-sr,dep+1,0)
        if start<sr:
          q=min(q,lowval(start,sr,dep,v+1))
        if stop>sr+r:
          q=min(q,lowval(sr+r,stop,dep,v+1))
        return q  
      else:
        return lowval(start,stop,dep,v+1)  

val=[]        
for f in range(0,len(seeds),2):
  start=seeds[f]
  stop=seeds[f]+seeds[f+1]
  x=lowval(start,stop,0,0)  
  val.append(x)
print(min(val))

