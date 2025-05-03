# list comprehension → بلافاصله یک لیست کامل در حافظه می‌سازد.
# generator expression → مقدارها را به صورت lazy (تنبل) و یکی‌یکی تولید می‌کند و در حافظه ذخیره نمی‌کند.
numbers = [x * 2 for x in range(10)]

numbers1 = (x * 2 for x in range(10))


import sys

# لیست بزرگ
list_comp = [x for x in range(1000000)]
print("حافظه list comprehension:", sys.getsizeof(list_comp), "بایت")

# جنراتور بزرگ
gen_exp = (x for x in range(1000000))
print("حافظه generator expression:", sys.getsizeof(gen_exp), "بایت")


