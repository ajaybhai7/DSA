n = int(input("Enter Number: "))
if n <= 1:
    print("Number is Not prime")

else:
    for i in range (2, n):
        if n % i == 0:
            print(f"Number is not prime: {n}")
            break
    else:
        print(f"Number is prime: {n}")
