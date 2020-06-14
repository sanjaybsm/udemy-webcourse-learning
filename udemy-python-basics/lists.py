mylist = [1, 2, 3]
print(mylist)
myNewList = ['a', 'b', ['c', 'd', 'e']]
print(myNewList[2])

# list comprention
list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
col = [row[0] for row in list]
print(col)
