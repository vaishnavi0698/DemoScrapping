"""
# to count no.of times a letter is repeated in a given word
count = 0                     # intialised the count variable outside the function so count will never be updated in an iteration.
def counter(word,letter):
    for i in word:
        if i == letter:
            count = count + 1
        else:
            pass
    return count

word = input("enter the word\n")
letter = input("enter the letter\n") 
counter(word, letter) 
print("count is = ", count)

------------------------------------------------------------------
def counter(word, letter):
    count = 0                   # <-- initialized the count variable inside the function 
    for i in word:
        if i == letter:
            count = count + 1
    return count

word = input("enter the word\n")
letter = input("enter the letter\n") 
result = counter(word, letter)  # <-- capture return value
print("count is =", result)
------------------------------------------------------------------


word = "banana"
result = word.count('a')
print(result)
------------------------------------------------------------------
"""

word = input("enter the word\n")
letter = input("enter the letter\n")
result=word.count(letter)
print("count is =", result)