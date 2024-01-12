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
  
s=tilt(s)
sm=0
for x in range(W):
  for y in range(H):
    if s[y][x]=='O':
      sm+=(H-y)        
  
print(sm)
  
