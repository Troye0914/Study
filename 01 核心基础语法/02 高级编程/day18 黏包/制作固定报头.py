import struct

# 制作报头
# 发送整型数据, 制作类型为i，获得到的是一个4个字节的整数
res = struct.pack('i', 2023)

print(res)
print(len(res))

# 将获得到的数据报头进行解码
# 获得到的是一个元组类型，第一个数据就是解码之后的真实数据
obj = struct.unpack('i', res)
print(obj)
print(obj[0])
