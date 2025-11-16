my_set = {1, 2, 3, 4, 5}
my_set.remove(3)   # Error if 3 doesn't exist
my_set.discard(10) # No error if 10 doesn't exist

print(my_set)


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merged = {**dic1, **dic2, **dic3}
print(merged)


n = 5
squares = {x: x*x for x in range(1, n+1)}
print(squares)

square_dict = {x: x*x for x in range(1, 16)}
print(square_dict)
my_set = {1, 2, 3, 4}
print(my_set)

my_set = {10, 20, 30}
for item in my_set:
    print(item)

my_set = {1, 2, 3}
my_set.add(4)
my_set.update([5, 6])

print(my_set)

my_set = {1, 2, 3, 4, 5}
my_set.remove(3)   
my_set.discard(10) 

print(my_set)









