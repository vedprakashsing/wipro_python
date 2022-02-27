number=int(input("Enter the number to sum:-"))
newNumber=0;
tempNumber=number;
while tempNumber:
    digit=int(tempNumber%10)
    newNumber=(newNumber*10)+digit
    tempNumber=int(tempNumber/10)

if(newNumber==number):
    print("\n",number,"is palindrom.")
else:
    print("\n",number,"is not a palindrom number.")