#  WAP to check if a given number is Armstrong number or not. For 
# each task create separate functions. 


def count_digits(n):
    count = 0

    while n > 0:
        count = count + 1
        n = n // 10

    return count


def armstrong_sum(n, digits):
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit ** digits
        n = n // 10

    return total


def check_armstrong(n):
    digits = count_digits(n)
    total = armstrong_sum(n, digits)

    if total == n:
        return True
    else:
        return False


n = int(input("Enter a number: "))

if check_armstrong(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")