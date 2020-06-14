seq = [1, 2, 3, 4, 5, 6]

for item in seq:
    print(item)

dict = {"key1":"value","key2":"value2"}

for k in dict:
    print(k)

# tuples
mypairs = [(1, 2), (3, 4), (4, 5)]
for tup1, tup2 in mypairs:
    print(tup1)
    print(tup2)

# range
for item in range(10):
    print(item)

# list comprension
myList = [1, 2, 3, 4]

out = []

for num in myList:
    out.append(num**2)

# print("list without comprention")
# print(out)

# List with comprention
out = [num**2 for num in myList]
print("list comprention")
print(out)
