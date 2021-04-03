# list is a collection of data types
myList = [3, 10, -1, True, "Python"]
print(myList)

item = myList[0]

# Loop through array
for i in myList:
    print(i)

# check content in my list
if "Python" in myList:
    print("yes")
else:
    print("No")

# print length
print(len(myList))

# add element at the end of array
myList.append("Lemmon")
print(myList)

# insert at specific index
myList.insert(1, "Apple")
print(myList)

# remove the last item
myList.pop()
print(myList)

# remove specific item from list
item = myList.remove(True)
print(myList)

# reverse list
myList.reverse()
# sort
# myList.sort()


# immutable copy
myListCopy = myList.copy()
myListCopy = list(myList)
myListCopy = myList[:]


# slice
a = myList[1:5]

print(a)


# remove all elements
myList.clear()


myList = [1, 2, 3, 4, 5, 6]
b = [i * i for i in myList]
print(b)
