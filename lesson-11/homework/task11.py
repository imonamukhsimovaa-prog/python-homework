def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "no zero"
    return a / b


def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count



def calculate_area(radius):
    return 3.14 * radius * radius

def calculate_circumference(radius):
    return 2 * 3.14 * radius


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)



from math_operations import add, subtract, multiply, divide
from string_utils import reverse_string, count_vowels

from geometry.circle import calculate_area, calculate_circumference
from file_operations.file_reader import read_file
from file_operations.file_writer import write_file

print(add(3, 5))  
print(reverse_string("hello"))
print(count_vowels("hello world"))

print(calculate_area(10))
print(calculate_circumference(10))



