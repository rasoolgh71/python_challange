# صورت مسئله:
# آرایه‌ای از اعداد صحیح داده شده. خروجی آرایه‌ای باشه که اعداد بر اساس تعداد تکرار نزولی مرتب شده باشن. اگه دو عدد تکرار برابر داشتن، عدد کوچک‌تر جلوتر باشه

def count_repeat_freq(inp):
    sety={}

    for num in inp:
        if num in sety:
            sety[num] += 1
        else:
            sety[num] = 1

    print(sety)

    def sort_key(x):
        k = (-sety[x], x)
        # print(f"x = {x}, key = {k}")
        return k
    # sort1 = sorted(inp, key=lambda x: (-sety[x], x))
    sort1 = sorted(inp, key=sort_key)
    print(sort1)




if __name__ == "__main__":
    inp=[4, 5, 6, 5, 4, 3]
    count_repeat_freq(inp)
