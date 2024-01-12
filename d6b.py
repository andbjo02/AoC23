s=[x.strip() for x in open(0)]

ts=s[0].split(':')
ds=s[1].split(':')
T=list(map(int,ts[1].split()))
D=list(map(int,ds[1].split()))

T=int("".join([str(x) for x in T]))
D=int("".join([str(x) for x in D]))

sm=1

def dist(x):
  vel=x+1
  return vel*(T-1-x)

lst=[]
sqT=1000
for x in range(0,T,sqT):
  if dist(x)>D:
    lst.append(x)

for x in range(lst[0]-sqT,lst[0]+1):
  if dist(x)>D:
    f=x
    break
for x in range(lst[-1]+sqT-1,lst[-1]-1,-1):
  if dist(x)>D:
    b=x
    break
    
print(b-f+1)

  


