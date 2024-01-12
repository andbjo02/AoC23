s=[x.strip() for x in open(0)]

sm=0
for x in s[0].split(','):
  cv=0
  for y in x:
    cv+=ord(y)
    cv*=17
    cv&=255
  sm+=cv
print(sm)

