a=int(input())
flag=0
for i in range(2,a):
  if(i<=a/2):
    if(a%i==0):
      flag=1
      break
if(flag==0):
   print("{0} is a prime number".format(a))
else:
  print("{0} is not a prime number".format(a))
