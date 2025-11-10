birth_year = int(input("2007"))
birth_month = int(input("09"))
birth_day = int(input("19"))

print("18")


from datetime import date 
name = input("imona")
birth_year = int(input("2007"))
today = date.today()
age = today.year - birth.year 
print(name, "18", age)


txt = 'LMaasleitbtui'
car = txt[0] + txt[2] + txt[4] + txt[6] + txt[8] + txt[10]
print(car) 



txt = 'MsaatmiazD'
car = txt[0] + txt[2] + txt[4] + txt[6] + txt[8]
print(car) 

txt = "I'am John. I am from London"
part = txt.split("from ")[1]
print(part)



text = input("hello world")
print(text[::-1])


numbers = list(map(int, input("1683272930389 ").split()))
print("2", max(numbers)) 


email = input("bob@gmail.com")
domain = email.split("@")[1]
print("Domain", domain)


import random
import string

chars = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(chars) for _ in range(12))
print("Password", password)









