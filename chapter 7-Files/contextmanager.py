"""
#without the files concept
names = []
for i in range(0,3):
    name = input("enter the name\n")
    names.append(name)

for i in sorted(names):
    print(f"hello {i}")

#can write the same code using (contextmanager - i.e using "with" keyword) to simplify the code in files

with open("hello.txt", "a") as file:
    for i in range(3):
        name = input("enter the name: \n")
        file.write(f"hello  {name}, how are doing? \n")
"""
 
with open("hello.txt") as file:
    lines= file.readlines()

for line in lines:
    print("hey,", line.rstrip())


