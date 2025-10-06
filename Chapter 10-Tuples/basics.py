"""
t = ('stroller')
print(t)
print(type(t))     #prints t as string

t = tuple('stroller')
print(t)
print(type(t))      #prints t as tuple


t = ('s','t','o','l','l','e','r')
print(t)
print(type(t))      #prints t as tuple

#x = (2 + 3) * 4 

t = ['s','t','o','l','l','e','r']
print(type(t))
"""
x,y = [1,2]
print(x)
print(type(x))

m = ['have', 'fun']
x, y = m
print(type(x))

email_address = "monty@python.org"
uname, domain = email_address.split('@')
print(uname,domain)