def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    
    for num in range(2, n-1):
        if (n % num) == 0:
            return False
    else:
        return True
        
print(is_prime(int(input("Enter number: "))))