from multiprocessing import Pool, cpu_count
import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def count_primes_in_range(start, end):
    count = 0
    for num in range(start, end):
        if is_prime(num):
            count += 1
    return count


if __name__ == "__main__":
    N = 100_000  # تا عدد ۱۰۰ هزار
    num_workers = cpu_count()
    pool = Pool(processes=num_workers)

    # تقسیم بازه بین processها
    ranges = []
    chunk_size = N // num_workers
    for i in range(num_workers):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_workers - 1 else N
        ranges.append((start, end))

    # اجرای موازی
    results = pool.starmap(count_primes_in_range, ranges)

    # جمع نتایج
    total_primes = sum(results)
    print(f"تعداد اعداد اول تا {N}: {total_primes}")
