"""
s = 'spam'
t = list(s)
print(t)
------------------------------------------------------------------------
s = 'Ready for the painting'
#t = list(s)
#print(t)

t = s.split()
print(t)
------------------------------------------------------------------------

#exercise 1:(pg 99)
def chop(t):
    del t[0]
    j = len(t)-1
    del t[j]

t = []
t = input("enter the elements for list t\n").split()
chop(t)
print(t)    

------------------------------------------------------------------------
"""
def middle(t):
    new_list = t[1:-1]
    return new_list

t = []
t = input("enter the list elements\n").split()
new_list = middle(t)
print(new_list)
