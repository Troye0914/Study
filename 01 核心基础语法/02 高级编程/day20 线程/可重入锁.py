from threading import Thread, RLock

'''
四个哲学家去西餐厅吃饭（餐刀，餐叉）
这时一个服务员给其中两个哲学家拿了两把餐刀，给另外两个哲学家拿了两把餐叉
'''


# zxj_1：有两把餐刀
def zxj_1():
    z.acquire()
    print('你给我一把餐叉')
    z.acquire()
    print('我给你一把餐刀')
    z.release()
    z.release()


# zxj_2：有两把餐叉
def zxj_2():
    z.acquire()
    print('你给我一把餐刀')
    z.acquire()
    print('我给你一把餐叉')
    z.release()
    z.release()


if __name__ == '__main__':
    z = RLock()
    a = Thread(target=zxj_1)
    b = Thread(target=zxj_2)
    a.start()
    b.start()
