import random
import time
from functools import wraps


def list_random_number(count):
    list_array = [random.randint(1, 100) for _ in range(count)]
    return list_array


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        # print(f"📍 شروع تابع '{func.__name__}' در {time.strftime('%H:%M:%S', time.localtime(start_time))}")

        result = func(*args, **kwargs)

        end_time = time.time()
        # print(f"✅ پایان تابع '{func.__name__}' در {time.strftime('%H:%M:%S', time.localtime(end_time))}")
        print(f"⏱ زمان اجرا: {end_time - start_time:.4f} ثانیه")
        return result

    return wrapper
