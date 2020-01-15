# no1=int(input("enter d first no"))
# no2=int(input("enter d secnd no"))
# no3=int(input("enter d third no"))
# if no1>no2:
#     if no1>no3:
#         print("largest no is",no1)
#     else:
#         print("largest no is",no3)
# else:
#     if no2>no3:
#
#         print("largest no is ",no2)
#     else:
#         print("largest no is ",no3)no3


# no1=int(input("enter d first no"))
# no2=int(input("enter d secnd no"))
# no3=int(input("enter d third no"))
#
# if (no1>no2)&(no1>no3):
#     print("max no",no1)
# elif (no2>no1)&(no2>no3):
#     print("max no",no2)
# elif (no3>no1)&(no3>no2):
#     print("max no", no3)
# else:
#     print("all r equal")


m1=int(input("enter mark of stdent"))
m2=int(input("enter mark of stdent"))
m3=int(input("enter mark of stdent"))
print("marks f sudent is:",m1,m2,m3)
total=m1+m2+m3
print("total mark out of 150 is",total)
if total>145:
    print("grade is A")
elif (total <145)&(total>=140):

    print("grade is B")
elif (total<140)&(total>=135):

    print("grade is C")
elif( total<135)&(total>=130):
    print("grade is D")
else:
    print("failed")