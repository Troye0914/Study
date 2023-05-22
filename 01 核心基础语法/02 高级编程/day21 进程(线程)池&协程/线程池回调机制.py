from concurrent.futures import ThreadPoolExecutor


def eat():
    for i in range(20):
        return f'喝第{i}杯小柴胡'


def get(f):
    print(f'获得到返回值为：{f.result()}')


if __name__ == '__main__':
    p = ThreadPoolExecutor(10)
    for i in range(30):
        res = p.submit(eat)
        res.add_done_callback(get)
