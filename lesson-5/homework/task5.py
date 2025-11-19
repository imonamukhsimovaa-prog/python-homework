def is_leap(year):
    """Determines whether a given year is a leap year"""
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


n = int(input())

if n % 2 == 1:
    print("weird")
elif 2 <= n <= 5:
    print("not weird")
elif 6 <= n <= 20:
    print("weird")
else:
    print("not weird")


def even_numbers_if(a, b):
    start = a if a % 2 == 0 else a + 1
    end = b if b % 2 == 0 else b - 1

    if start > end:
        return []

    return list(range(start, end + 1, 2))

def even_numbers_no_if(a, b):
    return list(range(a + a % 2, b + 1 - (b % 2), 2))

