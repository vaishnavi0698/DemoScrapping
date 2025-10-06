"""
#exercise 1: calling function{print_lyrics()} inside another function{repeat_lyrics()}
def print_lyrics():  # as soon as python see's this first line it will undrstand that it's a function and it will be stored in the "memory" but it will not be executed since it's not called yet!
    print("I am a lumberjack, and I'm okay." )
    print("I sleep all night and I work all day.")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()


repeat_lyrics()
# no error since proper functions defining and calling jarigindi 


#exercise 2: to check what error we get as we move the function call before function deftn:
repeat_lyrics()

def print_lyrics():
    print("I am a lumberjack, and I'm okay." )
    print("I sleep all night and I work all day.")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
# errror occured bcz function call first line lo chesam; aa travta functn ni define chesam

#exercise3:to chck error by moving the func call to the end of prgrm and move the defn of printlyrics afetr the def of repeatlyrics defn:
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I am a lumberjack, and I'm okay." )
    print("I sleep all night and I work all day.")

repeat_lyrics() # ikkada fnction call jarigindi bcz deeni function def already paina undi which is not the case in exercse2
# no error in exercise3


#Write a program to create a recursive function that calculates the sum of numbers from 0 to 10.
#A recursive function is a function that calls itself repeatedly.
#Expected Output: 55


def add(a,b):
    result = a+b
    print("result is: ", result)
  
total = add(5, 10) + add(3, 7) # gives the outout as total = none + none since the function returns nothing default values is none; throws error.
print(total)                   # hence this noting is printed since excution stops at total statement itself.

"""
def add(a, b):
    result = a+b
    return result

total = add(5,10) + add(3,7)
print(total)

    