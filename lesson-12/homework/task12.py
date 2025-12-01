import threading

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return True

def check_range(start, end, result_list):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    result_list.extend(primes)




import threading
from collections import defaultdict

def process_lines(lines, result_dict):
    local_count = defaultdict(int)
    for line in lines:
        words = line.strip().lower().split()
        for w in words:
            local_count[w] += 1


    for word, cnt in local_count.items():
        result_dict[word] += cnt

if __name__ == "__main__":
    file_path = "large_text.txt"
    num_threads = 4

    with open(file_path, "r", encoding="utf-8") as f:
        all_lines = f.readlines()

    total_lines = len(all_lines)
    chunk = total_lines // num_threads

    threads = []
    global_count = defaultdict(int)

    for i in range(num_threads):
        start = i * chunk
        end = (i + 1) * chunk if i < num_threads - 1 else total_lines
        t = threading.Thread(
            target=process_lines,
            args=(all_lines[start:end], global_count)
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


    
