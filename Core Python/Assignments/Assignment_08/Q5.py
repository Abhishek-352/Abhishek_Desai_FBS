# Sum of all prime numbers between 1 to n

def prime_sum(n):
    total = 0

    for num in range(2, n + 1):
        count = 0

        for i in range(2, num):
            if num % i == 0:
                count = count + 1

        if count == 0:
            total = total + num

    return total

n = int(input("Enter n: "))

result = prime_sum(n)

print("Sum of prime numbers =", result)