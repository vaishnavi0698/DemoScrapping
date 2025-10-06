
import string
fhand = open ("example.txt")
counts = {}

#iterating file over each line and each word from that line to convert into a (key,value)pair for the counts{}dictionary
for line in fhand:
    line =line.translate(str.maketrans('','',string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1

#now we should create a list of tuples from the counts{}
lst = []
for word, count in counts.items():
    lst.append((count,word))

#sorting the list of tuples based on the count of words in the list    
lst.sort(reverse=True)

#printing most common top 10 words from the file
for count,word in lst[0:10]:
    print(count, word)

