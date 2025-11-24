nums = [1, 2, 3, 4]
res = list(map(lambda x: x * 2, nums))
print(res)   
res2 = list(filter(lambda x: x % 2 == 0, nums))
print(res2)  



def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(4))  
print(is_prime(7)) 

def digit_sum(k):
    return sum(map(lambda x: int(x), str(k)))

print(digit_sum(24))   
print(digit_sum(502))  



def powers_of_two(N):
    x = 1
    while x * 2 <= N:
        x *= 2
        print(x, end=" ")

powers_of_two(10) 

def powers_of_two(N):
    pows = []
    x = 1
    while x * 2 <= N:
        x *= 2
        pows.append(x)
    print(*pows)

powers_of_two(10)



