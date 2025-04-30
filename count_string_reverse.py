# تعداد رشته هایی که خود و معکوسشان در ارایه هست رو پیدا کن
def count_reverse_paris(words):
    word_set = set(words)
    counted = set()
    count = 0
    for word in words:
        rev = word[::-1]
        if rev in word_set and word not in counted and rev not in counted and word != rev:
            count += 1
            counted.add(word)
            counted.add(rev)
    # print(rev)
    return count


if __name__ == "__main__":
    words = ['ac', 'ca', 'bc', 'cc', 'ca']
    res_words = words[::-1]
    print(res_words)
    count1 = count_reverse_paris(words)
    print(count1)
