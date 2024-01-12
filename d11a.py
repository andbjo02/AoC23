s=[[y for y in x.strip()] for x in open(0)]
H=len(s)
W=len(s[0])
vert=[y for y in range(H) if all([s[y][x]=='.' for x in range(W)])]
horz=[x for x in range(W) if all([s[y][x]=='.' for y in range(H)])]
glxs=[(x,y) for y in range(H) for x in range(W) if s[y][x]=='#']
sm=0
for i in range(len(glxs)):
  x1,y1=glxs[i]
  for j in range(i+1,len(glxs)):
    x2,y2=glxs[j]
    mnx=min(x1,x2)
    mxx=max(x1,x2)
    mny=min(y1,y2)
    mxy=max(y1,y2)
    dst=(mxx-mnx)+(mxy-mny)
    for x in range(mnx,mxx+1):
      if x in horz:
        dst+=1
    for y in range(mny,mxy+1):
      if y in vert:
        dst+=1
    sm+=dst
print(sm)        

