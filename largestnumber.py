

num=int(input ("Enter First Number: "))
num2=int( input("Enter Second Number: "))
num3=int(input("Enter the third number: "))
num4= int(input("Enter the fourth number: "))

if num>num2 and num>num3 and num>num4:
    print(num, "is greater")
elif num2>num and num2>num3 and num2>num4:
    print(num2,"is greater")
elif num3>num and num3>num2 and num3>num4:
    print(num3, "is greater")
elif num4>num and num4>num2 and num4>num3:
    print(num4, "is greater")
else:
    print("Invalid input")