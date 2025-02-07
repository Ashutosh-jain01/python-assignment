# Accept two strings. Check whether one string is there in another string
str1 = input("enter any string:")
str2 = input("enter another string:")

if (str2 in str1):
    print("yes string found")
    print(str1.replace(str2,"haha"))

else :
    print("not found")