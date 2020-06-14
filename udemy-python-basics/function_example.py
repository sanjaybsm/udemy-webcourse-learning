def my_func(param1="hello"):
    print("printing first function")

def addNum(num1,num2):
    if(type(num1)==type(num2)==type(10)):
        return num1+num2
    else:
        return "I need Integers"

result = addNum(1, 2)
print(result)
