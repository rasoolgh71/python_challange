from multiprocessing import Process

def worker():
    print("کار در حال اجرا")

if __name__ == "__main__":
    p1 = Process(target=worker)
    p2 = Process(target=worker)
    p1.start()
    p2.start()