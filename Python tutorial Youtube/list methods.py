n = [5,2,1,7,4]

n.append(30)
print(n)

n.insert(0,10)
print(n)

n.remove(5)
print(n)

n.clear()
print(n)

n = [5,2,1,7,4]
print(n.pop())
print(n.index(5))
print(n.count(5))

print(n.sort())
print(n)

print(n.reverse())
print(n)

n1 = n.copy()
print(n1)

list1 = [34,42,45,564,2,3546,64,23,23,23,54,65,76,34,42]
list2 = set(list1)
list3 = list(list2)
print(list3)


n1 = [2,2,4,6,3,4,6,1]
uniques = []
for i in n1:
    if i not in uniques:
        uniques.append(i)
print(uniques)
