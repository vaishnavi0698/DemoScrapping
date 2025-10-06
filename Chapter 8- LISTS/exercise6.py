# this is from exercise 6 problem on page no:104
"""
nums = []
#for i in nums: #ikkada nums anedi empty list so how will for loop understand how many iterations should it run ani ?? XXXX
n = int(input("enter howmany elements to be taken inside list"))
for i in range(n):
    i = input("enter a number\n")
    if i == 'done':
        break
    else:
        nums.append(i)
print("list given by the user:", nums) 

"""
#same problem with while loop so that we need not ask user to enter how many elements in the list in the beginning and such it can run infinitely
#-------------------------------------------- FOR = FINITE LOOP-------------------------------WHILE = INFINITE LOOP----------------------------
nums = []
while True:
    i = input("enter a number\n")
    if i == "done":
        break
    else:
        nums.append(int(i))
print("list elements are:", nums)        
print("Maximum of list:", max(nums))
print("minimum of list:", min(nums))
