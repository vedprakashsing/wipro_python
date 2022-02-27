
number=int(input("Enter the number to sum:-"))
result=0
while number:
    digit=int(number%10)
    result=result+digit
    number=int(number/10)

print("\n","Sum is",result)