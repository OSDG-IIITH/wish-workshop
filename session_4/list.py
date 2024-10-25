l = [1,2,3,4]

# pop function
a = l.pop()
print("poped element:", a)

# append function
b = 5
l.append(b)
print("New list is:", l)

print(l[0], l[2])

# appending a list
l2 = [1,2]
l.append(l2[0])
l.append(l2[1])
print(l)

# clear
l.clear()
print("cleared list:", l)

# count
l = [1,2,3,4,1,1,2]
a = l.count(1)
b = l.count(2)
print("a: ", a, "b:", b)

# index at
print("4's index in list:", l.index(4))

# insert
l = [0,1,2,3]
l.insert(2, 5)
print("updated list:", l)

l = [0,1,2,3]
l.insert(6, 5)
print("updated list2:", l)

# complex index
l = [1,2,3,4,5]
print("index at -2 of l is:", l[-2])

# out of range indexing
#print("Index at 6 for l", l[6])

# slicing
l = [1,2,3,4,5]
print("Sliced from 1 to 3", l[0:3])
print("Slicing upto 3", l[:3])
print("Slicing from 3", l[3:])

# negetive slicing
print("Slicing upto -1", l[:-1], l[:4])
print("Slicing upto -3", l[:-3])

print("Slicing upto -3", l[:-3], l[:2])
print("Slicing from 1 upto -3", l[1:-3])

# exterior function
print("lenth of l is:", len(l))

# sort
l = [5,3,4,2,1]
#print("sort:", sorted(l))
print("sort2:", l.sort())
print("sort3:", l)

