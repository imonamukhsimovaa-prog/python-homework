import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(5)
print(c.area())
print(c.perimeter())


from datetime import date

class Person:
    def __init__(self, name, country, birth_date):
        self.name = name
        self.country = country
        self.birth_date = birth_date 

    def age(self):
        today = date.today()
        y, m, d = self.birth_date
        return today.year - y - ((today.month, today.day) < (m, d))

p = Person("ali", "uzbekistan", (2005, 6, 15))
print(p.age())



class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

c = Calculator()
print(c.mul(5, 6))



class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop() if self.data else None

s = Stack()
s.push(10)
s.push(20)
print(s.pop())



class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        cur = self.head
        while cur:
            print(cur.val, end=" ")
            cur = cur.next
        print()

    def insert(self, value):
        new = Node(value)
        new.next = self.head
        self.head = new

    def delete(self, value):
        cur = self.head
        if cur and cur.val == value:
            self.head = cur.next
            return

        while cur.next and cur.next.val != value:
            cur = cur.next

        if cur.next:
            cur.next = cur.next.next



class shoppingcart:
    def __init__(self):
        self.items = {}  # item: price

    def add(self, item, price):
        self.items[item] = price

    def remove(self, item):
        if item in self.items:
            del self.items[item]

    def total(self):
        return sum(self.items.values())

cart = shoppingcart()
cart.add("bread", 5000)
cart.add("milk", 8000)
print(cart.total())


class stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.pop()

    def display(self):
        print(self.data)

s = stack()
s.push(5)
s.push(10)
s.display()


class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0) if self.data else None

q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())


class Bank:
    def __init__(self):
        self.accounts = {}

    def deposit(self, name, amount):
        self.accounts[name] += amount

    def withdraw(self, name, amount):
        if self.accounts[name] >= amount:
            self.accounts[name] -= amount

    def get_balance(self, name):
        return self.accounts[name]

b = Bank()
b.create_account("Ali", 100)
b.deposit("Ali", 50)
print(b.get_balance("Ali"))
