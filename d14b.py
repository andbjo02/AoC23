s=[[y for y in x.strip()] for x in open(0)]
H=len(s)
W=len(s[0])

def tilt(s):
  for x in range(W):
    for y in range(H):
      if s[y][x]=='O':
        v=y
        while v>0 and s[v-1][x]=='.':
          s[v][x]='.'
          v-=1
          s[v][x]='O'
  return s
  
def rot(s):
  t=[[' ']*len(s) for _ in range(len(s[0]))]
  for y in range(len(s)):
    for x in range(len(s[0])):
      t[x][len(s)-1-y]=s[y][x]
  return t

def cycle(s):
  for i in range(4):
    s=tilt(s)
    s=rot(s)
  return s   

i=0
D=dict()
while True:
  s=cycle(s)
  t=[]
  for y in range(H):
    for x in range(W):
      if s[y][x]=='O':
        t.append(x)
        t.append(y)
  t=tuple(t)
  if t in D:
    break
  D[t]=i
  i+=1

step=i-D[t]
d=(1000000000-i)//step
i+=d*step
while 1000000000-i>1:
  s=cycle(s)                
  i+=1
sm=0
for x in range(W):
  for y in range(H):
    if s[y][x]=='O':
      sm+=(H-y)        
  
print(sm)
  
