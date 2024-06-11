# data type
number = 78  # int
num = 48.09  #float
greeting = "how are you doing"  #str
is_programming_interesting = True  #bool

devices =["laptop","computer","tablet","phone"] #this is a list

browser =("opera", "firefox", "safari", "Brave") #tuple

countries ={"Kenya", "Uganda", "Tanzania"} #set

employee ={
    "firstname": "Jane",
    "age": 29,
    "nationality": "Kenyan",
    "emailaddress": "jane@gmail.com"
}# this is a dictionary

print(is_programming_interesting)
print(num)
print(countries)

print(employee["firstname"])

 # determining data type

print(type(employee))

# typecasting is the process of converting one data type to another

print(int(num))