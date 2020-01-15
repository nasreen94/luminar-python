clothtype=input("enter the cloth type")
x=int(input("enter the price"))
if clothtype=="cotton":
    if x>20000:
        print("discount is 10%")
    elif x>=15000:
        print("discount is 9%")
    elif x>=14000:
        print("discount is 7%")
    else:
        print("discount is 2%")
elif clothtype=="linen":
    if x>20000:
        print("discount is 15%")
    elif x>=15000:
        print("discount is 10%")
    elif x>=14000:
        print("discount is 9%")
    else:
        print("discount is 5%")
else:
    if x>20000:
        print("discount is 15%")
    elif x>=15000:
        print("discount is 10%")
    elif x>=14000:
        print("discount is 9%")
    else:
        print("discount is 5%")

