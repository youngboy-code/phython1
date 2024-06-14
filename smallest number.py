first = int(input("enter  the first number ; "))
second = int(input("enter  the second number ; "))
third = int(input("enter  the third number ; "))
fourth = int(input("enter  the fourth number ; "))

print("your numbers are", first, second, third, fourth)

if first < second and first < third and first < fourth :
    print(int(first),"is the smallest number")

if second < first and second < third and second < fourth :
    print(int(second),"is the smallest number")

if third < second and third < first and third < fourth :
    print(int(third),"is the smallest number")

if fourth < second and fourth < third and fourth < first :
    print(int(fourth),"is the smallest number")


