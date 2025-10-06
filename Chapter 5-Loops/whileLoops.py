"""
# finite loop execution (since we gave a condition at the while statement)
n = int(input("enter the n value\n"))
        
while n > 0:   #conditions that holds either TRUE or FALSE
    print(n)
    n = n-1
print("Blast off")    
"""
# running infinite loop until user enters "Done"
while True:    # condition that is always TRUE and runs the loop forever
    user_input = input("enter your text\n")
    if user_input == 'Done':
        break
print('loop ends here with Done')

