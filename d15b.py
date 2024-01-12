s=[x.strip() for x in open(0)]

MX=100
box=[[("",0)]*MX for _ in range(256)]

for x in s[0].split(','):
  cv=0
  z=""
  i=0
  while x[i]!='-' and x[i]!='=':
    z+=x[i]
    i+=1
  r=x[i+1:]
  for y in z:
    cv+=ord(y)
    cv*=17
    cv&=255
  if x[i]=='-':
    for q in range(0,MX):
      if box[cv][q][0]==z:
        box[cv][q]=("",0)
    c=0
    for q in range(0,MX):
      if box[cv][q][0]!="":
        box[cv][c]=box[cv][q]
        c+=1
    while c<MX:
      box[cv][c]=("",0)
      c+=1
  if x[i]=="=":
    found=False
    
    for q in range(0,MX):
      if box[cv][q][0]==z:
        box[cv][q]=(z,r)
        found=True              
    if not found:
      c=0
      while c<MX and box[cv][c][0]!="":
        c+=1
      box[cv][c]=(z,r)    
sm=0
for i in range(256):  
  if box[i][0][0]!="":
    for j in range(10):
      if box[i][j][0]!="":
        foc=(i+1)*(j+1)*int(box[i][j][1])
        sm+=foc
  
print(sm)
  
