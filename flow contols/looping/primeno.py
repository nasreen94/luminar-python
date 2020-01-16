x=int(input("enter the value"))
flag=0
for i in range(2,x):
    if (x%i==0):
        flag=flag+1
        break
    else:
        flag=0
if(flag==0):
    print("prime")
else:
    print("not prime")