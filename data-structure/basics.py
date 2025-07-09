list1 = []
set1 = {5,6,7,8,9}
set2 = {9,10,11,12,13}
tuple1 = (1,2,3,3,4)
list3 = list(tuple1)
list1.extend(list3)
set3 = set2.union(set1)
list2 = list(set3)
list1.extend(list2)
print(list1)
print(tuple1.count(3))
print(tuple1.index(2))