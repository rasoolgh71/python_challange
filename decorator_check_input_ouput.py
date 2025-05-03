import functools


def log_inputs_outputs(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # چاپ پارامترهای ورودی
        print(f": args={args}, kwargs={kwargs}")

        # فراخوانی تابع اصلی و گرفتن خروجی
        result = func(*args, **kwargs)

        # چاپ خروجی
        print(f"خروجی: {result}")

        return result

    return wrapper


# مثال استفاده از دکوراتور
@log_inputs_outputs
def add(a, b):
    return a + b


if __name__ == "__main__":
    add(2, 3)
