number = int(input("Write a number: "))
prime = []
[prime.append(i) for i in range(1, number+1) if (number % i) == 0]
if len(prime) == 2:
    print(number, " is a prime number!")
    
