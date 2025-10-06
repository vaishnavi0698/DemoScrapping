
try:
    total = 0
    count = 0
    avg = 0
    while True:
        user_input = int(input("enter a number\n"))
        if user_input == "done":
            break
        total = total + user_input
    print("total is:", total)

except:
    print("invalid input")


