try:
    print(x)

except:
   print("an error occurred here")

finally:
    print("success")

num1 = 99
num2 = 0

try:
    print(num1 / num2)

except:
     print("zero division occurred")

finally:
     print("success")