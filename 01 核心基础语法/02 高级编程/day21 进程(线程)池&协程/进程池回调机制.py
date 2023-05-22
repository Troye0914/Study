import time
from concurrent.futures import ProcessPoolExecutor


def func(name):
    time.sleep(2)
    return f'{name}'


# 回调机制打印返回值
def get(f):
    # 参数就是submit返回值
    print(f'获得到返回值为：{f.result()}')


if __name__ == '__main__':
    # 设置进程池对象，传入参数，这个参数代表这个进程池有多少个进程
    # 没有参数会默认开启与当前电脑cpu核数相匹配的进程个数
    p = ProcessPoolExecutor(10)
    for i in range(30):
        # 调用进程池中的进程
        res = p.submit(func, '墨离')
        # 回调机制，获取在一次进程池中所有进程执行完之后的返回值，并一起输出
        res.add_done_callback(get)
