
try:
 hours = float(input("enter the hours: \n"))
 rate = float(input("enter the rate: \n"))
 if hours>40:
    pay = hours * 1.5 * rate
 else:
    pay = hours * rate   

except:
 print("Please enter the values in digits!") 
 pay = 0   

print("pay: ", pay)