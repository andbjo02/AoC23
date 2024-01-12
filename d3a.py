s=[x.strip() for x in open(0)]
  
dx=[1,0,-1,0]
dy=[0,1,0,-1]
sm=0

t=0
cm=1
vis=[[0]*len(s[0]) for _ in range(len(s))]
for y in range(len(s)):
  for x in range(len(s[0])):
    if s[y][x]>='0' and s[y][x]<='9':
      if not vis[y][x]:
        vis[y][x]=cm
        h=[(x,y)]
        while len(h):
          cx,cy=h.pop()
          for k in range(4):
            nx=cx+dx[k]
            ny=cy+dy[k]
            if nx>=0 and nx<len(s[0]) and ny>=0 and ny<len(s):
              if s[ny][nx]>='0' and s[ny][nx]<='9':
                if vis[ny][nx]==0:
                  vis[ny][nx]=cm
                  h.append((nx,ny))
        cm+=1              

for c in range(1,cm+1):
  t=0
  spec=False
  for y in range(len(s)):
    for x in range(len(s[0])):
      if vis[y][x]==c:
        t=t*10+ord(s[y][x])-48
        for rx in range(-1,2):
          for ry in range(-1,2):
            nx=rx+x
            ny=ry+y 
            if nx>=0 and nx<len(s[0]) and ny>=0 and ny<len(s):  
              if s[ny][nx]!='.' and (s[ny][nx]<'0' or s[ny][nx]>'9'):
                spec=True
  if spec:
    sm+=t                   
print(sm)


