import queue
from multiprocessing import Queue


# 初始化Queue对象
# Queue有个参数，这个参数指定消息存放数量
q = Queue(5)
# 存放消息数据
q.put('初五')
q.put('航宇')
# 判断消息队列是否满了——full
print(q.full())
q.put('我太南了')
q.put('拥有洁的我是无敌的')
# q.put('莫安心')
# 使用put存放消息，当消息数量超过了指定的数量，则进入阻塞状态
# q.put('莫安心1')
try:
    # put_nowait，当消息队列满了会抛出queue.Full异常
    q.put_nowait('莫安心1')
except queue.Full:
    print('消息已满')

# 获得消息队列中有多少个数据——qsize
# print(q.qsize())

# 从消息队列中获取数据
for i in range(5):
    print(q.get())
try:
    # get_nowait() 当消息队列中没有数据，则抛出queue.Empty异常
    print(q.get_nowait())
except queue.Empty:
    print('消息队列中没有数据了')
# 判断消息队列是否为空——empty
print(q.empty())
