# Prime number = divisible by 1 & itself

def prime_checker(num):
    is_prime = True
    if (num == 1):
        print("Not prime")
    else:
        for i in range(2, num):
            if (num % i == 0):
                is_prime = False
                break

        if (is_prime):
            print("prime number")
        else:
            print("not prime")


n = int(input("Check this number: "))
prime_checker(num=n)
