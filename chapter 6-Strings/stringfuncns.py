"""
#fruit = 'banana'                     #here fruit ia string and strings are immutable
fruit = ['b','a','n','a','n','a']   #here fruit is a list and lists are mutable(we can change the values inside a list)

index = len(fruit)-1
while len(fruit)-1 > 0:    #this is always calculating len(6)-1 = 5>0 so loop is never reaching to 1st element or pointing to firstindex 
    print(fruit[index])
    index = index - 1
print("done") 
"""


fruit = ['b','a','n','a','n','a']
index = len(fruit) - 1   # index = 5

while index >= 0:        # condition depends on index now so loop ends when the condition fails (-1>=0  ->>>>which is false!)
    print(fruit[index])
    index = index - 1

print("done")

# TIP: anduke while condition lo eppudu iteration variables(index) ni pettali for condition evaluation; constants(len(6)-1 = 5) ni kaadu