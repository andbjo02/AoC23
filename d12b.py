s=[x.strip() for x in open(0)]
sm=0
      
for x in s:
  y,z=x.split()
  z=list(map(int,z.split(',')))
  y=y+'?'+y+'?'+y+'?'+y+'?'+y
  z=z+z+z+z+z  
  dp=[[0]*(len(z)+1) for _ in range(len(y)+1)]
  dp[0][0]=1
  for k in range(len(y)):        
    if y[k]=='#':
      break
    dp[k+1][0]=1
  for i in range(1,len(y)+1):
    for j in range(len(z)):
      q=z[j]
      if i-q>=0:
        sol=True  
        for k in range(q):
          if y[i-1-k]=='.':
            sol=False
            break
        if sol:
          if i-1-q>=0 and y[i-1-q]=='#':
            sol=False
        if sol:
          rep=dp[i-q][j]
          if i-q>0:
            rep=dp[i-q-1][j]          
          dp[i][j+1]+=rep 
          for k in range(i,len(y)):        
            if y[k]=='#':
              break
            dp[k+1][j+1]+=rep 
  sm+=dp[len(y)][len(z)]  
print(sm)

