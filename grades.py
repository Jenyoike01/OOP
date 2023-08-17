num=int(input("Enter Marks: "))

if num>=80 and num<=100 :
    print("Grade is A")
elif num>=60 and num <=79:
    print("The grade is B")
elif num>=50 and num<=59:
    print("The Grade is C")
elif num>=30 and num<=49:
    print("The grade is D")
elif num<30 and num>0:
    print("The Grade is Fail")

else:
    print("Invalid input")

