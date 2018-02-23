a=int(input())
b=int(input())
c=int(input())
if((a>b)and(a>c)):
    print('{0} is a largest number'.format(a))
elif((b>a)and(b>c)):
    print('{0} is a largest number'.format(b))
elif((c>b)and(c>a)):
    print('{0} is a largest number'.format(c))
else:
    print("Equal")
    
