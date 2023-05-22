from concurrent.futures import ThreadPoolExecutor


def eat():
    for i in range(20):
        print(f'喝第{i}杯小柴胡')


if __name__ == '__main__':
    t = ThreadPoolExecutor(10)
    for i in range(30):
        t.submit(eat)
