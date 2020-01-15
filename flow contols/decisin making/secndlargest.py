no1=int(input("enter the first no"))
no2=int(input("enter the scnd no"))
no3=int(input("enter the thrd no"))
if no1>no2:
    if no3>no1:
        print("secnd large no is=",no1)
    else:
        if no3>no2:
            print("secnd large no is=",no3)
        else:
            print("secnd large no is=",no2)
else:
    if no2>no3:
        print("secnd large no is=",no3)
    else:
        if no2>no1:
            print("secnd large no is=",no2)
        else:
            print("secnd large no is=",no1)