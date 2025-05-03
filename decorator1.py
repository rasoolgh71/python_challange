# ترتیب اجرا از پایین به بالا است




def decorator1(func):
    def wrapper(*args, **kwargs):
        print("decorator1: قبل از اجرای تابع")
        result = func(*args, **kwargs)
        print("decorator1: بعد از اجرای تابع")
        return result
    return wrapper


def decorator2(func):
    def wrapper(*args, **kwargs):
        print("decorator2: قبل از اجرای تابع")
        result = func(*args, **kwargs)
        print("decorator2: بعد از اجرای تابع")
        return result
    return wrapper

@decorator2
@decorator1
def say_hello():
    print("hello rasool")


if __name__ == "__main__":
    say_hello()
