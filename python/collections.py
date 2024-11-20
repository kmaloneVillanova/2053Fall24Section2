lst = [10,20,30,40,50]
lst.append(5)
lst.append(6)
lst.append(7)
print(lst)

lst.remove(50)
print(lst)
lst.pop(1)
print(lst)
lst.pop()
print(lst)
lst.reverse()
print(lst)
lst.sort()
print(lst)

double_digits=lst[2:]
print(double_digits)
print(lst)

lst.append(40)
num40=lst.count(40)
print(num40)

copy_lst = lst
print(copy_lst)
copy_lst.append("new element")
print(copy_lst)
print(lst)

lst.remove("new element")
print(lst)

#copy_lst = lst[:]
copy_lst = lst.copy()
copy_lst.append("new element")
print(copy_lst)
print(lst)

empty = []
for val in lst:
    if val >= 10:
        empty.append(val)
print(empty)

empty = []
#empty[0] = 1
print(empty)
zeros = [0] * 10
print(zeros)

nums = []
for i in range(1,10):
    nums.append(i)
print(nums)

nums2 = []
for val in lst:
    nums2.append(val)

print(nums, nums2)

nums = [i for i in range(1,10)]
print(nums)
nums2 = [val for val in lst]
print(nums2)

# comprehensions allow us to filter and modify the value before
# adding it to the new list

nums = [val for val in lst if val < 10]
print(nums)
nums = [2*i for i in range(1,10)]
print(nums)

# Sets
aset = {1,2,3,3,3,3,3,2,1}
print(aset)

# Dictionary
fav_foods = {'Kathleen': 'pizza', 'Steve':'ribs', 'John':'burgers',
             'Patrick': 'pizza', 'Michelle':'pasta'}
print(fav_foods)

kff = fav_foods['Kathleen']
print(kff)

for key in fav_foods:
    print(fav_foods[key])

for key,value in fav_foods.items():
    print(key, value)
if 'Bob' in fav_foods:
    print("Bob's fav food is "+ fav_foods['Bob'])
else:
    fav_foods['Bob'] = "tacos"
print(fav_foods)

new_dict = {}
new_dict['key'] = 'value'

nums = [i*i for i in range(1,10) if i*i % 2 == 0]
print(nums)
