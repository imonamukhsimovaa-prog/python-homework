fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']


print(fruits[2])


number_s = [2, 3, 4, 6, 8, 9]
number_s2 = [4, 5, 6, 2, 3,] 
combined_list = number_s + number_s2
print(combined_list)  


numbers1 = [10, 20, 30, 40, 50, 60, 100]
first = numbers1[0]
middle = numbers1[len(numbers1)//2]
last = numbers1[-1]
new_list = [first, middle, last]
print(new_list)



movies = ['rush hour', 'interestellar', 'venom,' 'avengers', 'batman']
movies_tuple = tuple(movies)
print(movies_tuple)


countries = ['paris', 'london', 'tashkent', 'yiwu']

if 'paris' in countries:
  print('im live in paris now')
else:
     print('no') 

nums = [1, 2, 3]
dup = nums * 2
print(dup)

nums = [5, 10, 15, 20]
nums[0], nums[-1] = nums[-1], nums[0]
print(nums)

t = (1,2,3,4,5,6,7,8,9,10)
print(t[3:8])

olors = ["blue", "red", "blue", "green", "blue"]
print(colors.count("blue"))

animals = ("cat", "dog", "lion", "tiger")
print(animals.index("lion"))


a = (1, 2, 3)
b = (4, 5, 6)
merged = a + b
print(merged)

t = (2, 4, 6, 8, 10)
new_list = list(t)
print(new_list)
nums = (3, 9, 1, 7, 5)
print(max(nums), min(nums))

words = ("hello", "world", "python")
print(words[::-1])

















