# Print largest and smallest values out of three
a = int(input("enter any no."))
b = int(input("enter any no."))
c = int(input("enter any no."))

if (a>b and a>c and b>c):
    print(f"{a} is largest value")
    print(f"{c} is the smallest value")

elif (a>b and a>c and c>b):
    print(f"{a} is largest value")
    print(f"{b} is the smallest value")

elif (b>a and b>c and a>c):
    print(f"{b} is largest value")
    print(f"{c} is the smallest value")

elif (b>a and b>c and c>a):
    print(f"{b} is largest value")
    print(f"{a} is the smallest value")

elif (c>a and c>b and a>b):
    print(f"{c} is largest value")
    print(f"{b} is the smallest value")

elif (c>a and c>b and a<b):
    print(f"{c} is largest value")
    print(f"{a} is the smallest value")
