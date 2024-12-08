num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is neither prime nor composite.")
else:
    count = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            count += 1
            break  
    if count > 0:
        print(f"{num} is a composite number.")
    else:
        print(f"{num} is a prime number.")