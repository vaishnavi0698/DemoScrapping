
#problem 1:
#program to print the count of each letter in a word
str = "stroller"
count = {}
for i in str:
    if i in count:
        count[i] = count[i] +1
    else:
        count[i] = 1
print(count)
#------------------------------------------------------------------------------------------------------------------------------------------------
#problem 2:
#program to print the count of words in a given sentence
sentence = "Today is friday, so tomorrow is a saturday"
words = list(sentence.split(' '))
count = {}
for i in words:
    if i in count:
        count[i] = count[i] +1
    else:
        count[i] = 1
print(count) 
#------------------------------------------------------------------------------------------------------------------------------------------------
#problem 3:
#create a dict of students(name--> score) and print the student with the highest score.

n = int(input("enter the no.of students\n"))
scores = {}
for i in range(n):
     i = input("enter the student name\n")
     score = int(input("enter the score\n"))    
     scores[i] = score
print(scores) 
#Maximum_score = max(scores.values())
#print("highest score in the class: ", Maximum_score)

max_student = max(scores, key=scores.get)
max_score = scores[max_student]   
print("student who scored highest is: ", max_student)
#------------------------------------------------------------------------------------------------------------------------------------------------
#problem 4:
# #Write a program to update a dictionary by adding a new key-value pair.

dict1 = {}

dict1.update([ ('name','vaishu'), ('age',27),('height',5) ])
print(dict1)

dict1.update({'name' : 'vaishu', 'age': 27, 'height' : 5 })
print(dict1)

print(dict1.values())
print(dict1.keys())
#------------------------------------------------------------------------------------------------------------------------------------------------
#problem 5:
#Write a program to check if a given key exists in a dictionary.
dict1 = {'name' : 'vaishu', 'age': 27, 'height' : 5 }
key = input("enter the key you want to check inside dictionary\n")

checker = dict1.get(key,0)
print(checker)
#------------------------------------------------------------------------------------------------------------------------------------------------
#problem 6:
#write a program to reverse the keys and values in a dictionary(swap them)
uid = {'a': 1, 'b': 2, 'c': 3}
opd ={}
for key in uid:
    value = uid[key]
    opd.update({value : key})
    
print(opd)   