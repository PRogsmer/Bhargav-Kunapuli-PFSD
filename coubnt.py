n=153
s=0
n1=n
while n>0:
    r = n%10
    s = s+(r*r*r)
    n=n/10
if s == n1:
    print("armstrng")
else:
    print("not armstrng")

