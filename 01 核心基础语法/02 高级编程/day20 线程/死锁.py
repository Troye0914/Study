from threading import Thread, Lock

'''
四个哲学家去西餐厅吃饭（餐刀，餐叉）
这时一个服务员给其中两个哲学家拿了两把餐刀，给另外两个哲学家拿了两把餐叉
'''


# zxj_1：有两把餐刀
def zxj_1():
    z_a.acquire()
    print('你给我一把餐叉')
    z_b.acquire()
    print('我给你一把餐刀')
    z_b.release()
    z_a.release()


# zxj_2：有两把餐叉
def zxj_2():
    z_b.acquire()
    print('你给我一把餐刀')
    z_a.acquire()
    print('我给你一把餐叉')
    z_a.release()
    z_b.release()


if __name__ == '__main__':
    # zxj_1给自己的数据加了锁
    z_a = Lock()
    # zxj_2给自己的数据加了锁
    z_b = Lock()
    a = Thread(target=zxj_1)
    b = Thread(target=zxj_2)
    a.start()
    b.start()
