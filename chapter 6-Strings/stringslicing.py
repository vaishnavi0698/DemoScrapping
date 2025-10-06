
str = 'X-DSPAM-Confidence:0.8475'
#str.find(":")
count = 0
for i in str:
    if i != ":" :
        count = count + 1
    else:
        break
index = count  
print("index value of ':' is = ", index) 

extracted_string = float(str[index+1: ])
print("The extracted_string after ':' is ", extracted_string)

