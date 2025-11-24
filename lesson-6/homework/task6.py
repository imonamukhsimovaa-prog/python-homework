n = int(input())
for i in range(n):
    print(i*i)


n = int(input())
for i in range(n):
    print(i*i)


i = 1
while i <= 10:
    print(i)
    i += 1


for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


n = int(input("Enter number: "))
s = 0
for i in range(1, n+1):
    s += i
print("Sum is:", s)


n = int(input())
for i in range(1, 11):
    print(n * i)


numbers = [12, 75, 150, 180, 145, 525, 50]
for x in numbers:
    if x > 100 and x % 5 == 0 and x != 180 and x != 525:
        print(x)


n = int(input())
print(len(str(n)))


for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()


list1 = [10, 20, 30, 40, 50]
for x in reversed(list1):
    print(x)


for i in range(-10, 0):
    print(i)


for i in range(5):
    print(i)
print("Done!")


start, end = 25, 50
for num in range(start, end+1):
    if num > 1:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            print(num)


n = int(input())
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"{n}! = {fact}")
