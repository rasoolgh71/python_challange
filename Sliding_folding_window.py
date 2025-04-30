# پنجره جمع متحرک
#
# صورت مسئله:
# تابعی بنویس که یک لیست عددی و یک عدد k بگیره و مجموع همه‌ی زیربخش‌های kتایی پشت‌سرهم رو در لیست محاسبه کنه.

# Input: nums = [1, 2, 3, 4, 5], k = 3
# Output: [6, 9, 12]  # چون 1+2+3، بعد 2+3+4، بعد 3+4+5


def sum_windows(inp, k):
    p = k
    m = k
    while k <= len(inp):
        print(inp[k-p:m])
        sum1 = sum(inp[k-p:m])
        print("sum1", sum1)
        k += 1
        m += 1


if __name__ == "__main__":
    inp = [1, 2, 3, 4, 5, 6, 7]
    k = 5
    sum_windows(inp,k)
