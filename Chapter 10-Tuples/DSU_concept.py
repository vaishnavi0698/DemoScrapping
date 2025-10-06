"""
#given a list of words; yu ahve to sort them from longest to shortest using DSU pattern
#DSU : Decorate, Sort, Undecorate
#in this example
#  D: decorate a list of tuple as -----> list[tuple(length, word)]
#  S: Sort the list of tuples (sort based on the length)
# U: undecorate the pulling the original data (keep only the words not the length)


txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))

t.sort(reverse = True)


res = list()
for length, word in t:
    res.append(word)

print(res)

"""
 #given a dictionary; you have to sort them from longest to shortest based on values in dictionary:

d = {'a':10,'b':1,'c':22}
l1 = list(d.items())
print(l1)
l1.sort(reverse = True)
print(l1)

l2= []
for key, value in d.items():
    l2.append((value,key))
print("changed list ", l2)

l2.sort(reverse = True)
print("sorted list of tuples for the the gioven dictionary is:", l2)