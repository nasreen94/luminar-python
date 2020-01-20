x=[]
limit=int(input("enter the limit"))
for i in range(0,limit):
    value =int(input("enter d the no"))
    x.append(value)
for item in x:
    print (item)
print("even nos are")
sum=0
for i in range(0,limit):
    if x[i]%2==0:
        print(x[i])
        res=x[i]**2
        sum=(x[i]**2)+sum
    
print("sum of sqares of even no",sum)
