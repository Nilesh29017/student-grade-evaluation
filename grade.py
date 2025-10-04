a=int(input("Enter English marks: "))
b=int(input("Enter Maths marks: "))
c=int(input("Enter Physics marks: "))
d=int(input("Enter Chemistry marks: "))
e=int(input("Enter Biology marks: "))
sum=a+b+c+d+e
print("Total Marks:",sum)
avg=(sum)/5
print("Average:",avg)
if avg>=90:
    print("Grade: S")
elif avg>=80:
    print("Grade: A")
elif avg>=70:
    print("Grade: B")
elif avg>=60:
    print("Grade: C")
elif avg>=50:
    print("Grade: D")
else:
    print("Grade: Fail")
