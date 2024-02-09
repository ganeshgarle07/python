mylist = ["banana", "cherry", "apple", "banana"]
# print(mylist.count('banana'))
# str1 = 'abbcdecfg'
# listOfStr = list(str1)
# newList = {}
# count = 0
# for i in listOfStr:
#     if(i in newList):
#         newList[i]= newList[i] + 1
#     else:
#         newList[i] = 1
# print(newList)

list_of_jobs = [
    {"Job": "Sailor", "People": ["Martin", "Joseph"]},
    {"Job": "Teacher", "People": ["Alex", "Maria"]},
]
for i in list_of_jobs:
    if i["Job"] == "Teacher" and "Alex" in i["People"]:
        i["People"].pop(0)

# print(list_of_jobs)

l1 = [1, 4, 7, 9, 12]
res = 11


def find_pair_two_pointers(arr, target):
    left = 0
    right = len(arr) - 1
    print("----left", left)
    print("----right", right)
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [arr[left], arr[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None


print(find_pair_two_pointers(l1, res))

# print(i, '--------',l1[len(l1)-i:len(l1)])


# list_of_jobs[0]['People'].append('Andrew')
# print(list_of_jobs)
#

# mylist2 = [True, 2, 'Apple', 'Apple'] # added duplicate item
# print(mylist2)
# print(mylist2[0]) # indexing
# print(mylist2[-1]) # indexing

# for i in mylist:
#     print(i)

# # check item exit or not
# if 'banana' in mylist:
#     print('Banana is exit')
# else:
#     print('Banana is not exit')

# # append
# mylist.append('Text')
# print(mylist)

# #insert
# mylist.insert(1, 'Blueberry')
# print(mylist)

# #remove last item
# mylist.pop()
# print(mylist)

# #remove specific element
# mylist.remove('cherry')
# print(mylist)

# #reverse list
# mylist.reverse()
# print(mylist)
# #clear list
# mylist.clear()
# print(mylist)

# numberList = [1,2,3,33,44,2,5]
# # sorted = numberList.sort()
# print(sorted(numberList))

# # concate list
# l1 = [1,2,3]
# l2 = [5,4,3]
# print(l1 + l2)

# Slicing
# l1 = [1,2,3,4,5,6,7,8,9]
# print(l1[1:5]) # between
# print(l1[:6]) # start with 0 and end with 6
# print(l1[5:]) # start with 0 till the last
# print(l1[::2]) # skip second number

# copy
list_org = ["banana", "cherry", "apple"]
# newlist = list_org.copy() # option 1
# newlist = list(list_org) # option 2
newlist = list_org[:]  # option 3
newlist.append("lemon")
print(list_org)
print(newlist)

# # short hand to create new list
# l1 = [1,2,3,4,5]
# l2 = [i*i  for i in l1]
# print(l1)
# print(l2)
