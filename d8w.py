import math
l=[
14893,
19951,
22199,
16579,
17141,
12083
]
p=1
for x in l:
  p=(p*x)//math.gcd(p,x)
print(p)
  
