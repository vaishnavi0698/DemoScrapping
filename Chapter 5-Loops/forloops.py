"""
count = 0
for i in [23,5,8,90,121]:
    count = count + 1
print("no. of values in the list ", count)
----------------------------------------------------
sum = 0
elements = [23,5,8,90,121]
for i in elements:
    sum = sum + elements[i]
    i = i+1
print("total sum is: ", sum)
# this gives error

-----------------------------------------------------
sum = 0
elements =  [23,5,8,90,121]
for i in range(len(elements)):
    sum = sum + elements[i]
    #i = i+1
print("total sum is: ", sum)   
-----------------------------------------------------
"""
# much simplified and easier code than above:
sum = 0
for i in [23,5,8,90,121]:
    sum = sum +i
print("total sum is: ", sum)    
