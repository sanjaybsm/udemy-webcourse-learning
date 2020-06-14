# Lamda examles
# Without using lamda a funciton
mylist = [1, 2, 3, 4, 5, 6, 7, 8]
def even_bool(num):
    return num % 2 == 0
result = filter(even_bool, mylist)
print(list(result))

# Using Lamda
result1 = filter(lambda num: num % 2 == 0, mylist)
print(list(result1))
