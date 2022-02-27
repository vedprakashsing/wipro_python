def primeNumber(number):
 limit=int(number/2);
 #print(limit)
 check=False

 for x in range(2,limit+1):
    if(number%x==0):
        check=True
        break

 if(check):
   #print(number,"is not prime number.")
   return False
 else:
    #print(number,"is prime number.")
    return True


start=10
end=99
check=False

for x in range(start,end):
    if x%2==0:
        continue
    else:
        check=primeNumber(x)
        if(check):
            print(x)
