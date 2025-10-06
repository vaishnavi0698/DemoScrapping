
import string
fhand = open ("example.txt")
counts = {}

#iterating file over each line and each word from that line to convert into a (key,value)pair for the counts{}dictionary
for line in fhand:
    line =line.translate(str.maketrans('','',string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            if letter in counts:
                counts[letter] = counts[letter]+1
            else:
                counts[letter] = 1     

lst = []
for letter,count in counts.items():
    lst.append((count, letter))

lst.sort(reverse=True)

for count, letter in lst:
    print(count, letter)

