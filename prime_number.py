number=int(input("Enter the number to check:-"))
limit=int(number/2);
print(limit)
check=False

for x in range(2,limit+1):
    if(number%x==0):
        check=True
        break

if(check):
    print(number,"is not prime number.")
else:
    print(number,"is prime number.")