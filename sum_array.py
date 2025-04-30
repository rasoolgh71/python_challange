# آرایه‌ای از اعداد صحیح داده شده. اعدادی که فقط یک بار تکرار شده‌اند رو پیدا کن و مجموعشون رو بده.
from collections import Counter
from utils import list_random_number,measure_time

@measure_time
def sum_array_no_repeat(num_array):
    # sum = 0
    freq = Counter(num_array)
    uniques = [num for num in freq if freq[num] == 1]
    # print(uniques)
    sum1 = sum(uniques)
    return sum1


if __name__ == "__main__":
    num_array = list_random_number(90000)
    sum1 = sum_array_no_repeat(num_array)
    print(sum1)
    # print("p", p)
