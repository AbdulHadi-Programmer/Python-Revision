## List Methods:
# append() = add num at the end of list
# sort() = sort the list in ascending order
# sort(reverse=True) = Now it sort the list into reverse mean descending order
# reverse() = reverse the list, list start from end and end to first
# index(given_num) = give the index of given index in the first occurence and we have to print it
# count() = count the how many time the given element is present
# copy() = make a copy of original list 
# insert() = insert the new item at an specific index (1st argument is index, 2nd argument is num)
# extend() = add other list with the existing list
"""
l = [14, 1, 4, 0, 2, 3, 4, 1, 2, 1, 1, 1, 1]
print(l)
# l.append(7)
# l.sort(reverse=True)
# l.reverse()
# print(l.index(14)) # Output: 0
#print(l.count(1))
## Now in this situation, m is a reference of l list
# m = l
# m[0] = 0
# if we want to make a new list that is copy of l list then
# m = l.copy()
# m[0] = 0
# print(l)
# print(m) # now only m list change not l
# l.insert(1, 899)
m = [900, 1000, 1100]
# l.extend(m) # add m in l name list in the end
print(l)
# We can also make a new list, so that this can't change l 
k = l + m
print(l) # same list without any changes
print(m) # now this is same list as above
print(k) # Now this is the combined list 
"""
for i in range(3):
    for j in range(2):
        print(i, j)
