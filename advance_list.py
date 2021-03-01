list1 = [1,2,3]
list1.append(4)
print(list1)
print(list1.count(10))
print(list1.count(1))

# append: appends whole object at end:
x = [1, 2, 3]
x.append([4, 5])
print(x)

# extend: extends list by appending elements from the iterable:

x = [1, 2, 3]
x.extend([4, 5])
print(x)

# index() will return the index of whatever element is placed as an argument. Note: If the the element is not in the list an error is raised.
print(list1.index(2))
# print(list1.index(12))

# insert() takes in two arguments: insert(index,object) This method places the object at the index supplied
# Place a letter at the index 2
list1.insert(2,'inserted')
print(list1)

# pop(), which allows us to "pop" off the last element of a list. However, by passing an index position you can remove and return a specific element
ele = list1.pop(1)  # pop the second element
print(list1)
print(ele)

# remove() method removes the first occurrence of a value
list1.remove('inserted')
print(list1)
list2 = [1,2,3,4,3]
list2.remove(3)
print(list2)
# reverse() reverses a list. Note this occurs in place! Meaning it affects your list permanently
list2.reverse()
print(list2)

# sort() method will sort your list in place
list2.sort()
print(list2)
list2.sort(reverse=True)
print(list2)