import subprocess

# subprocess.Popen(cmd指令，shell=True，stdout，stderr)
# dir 查询一个文件下的子文件或者文件名
# tasklist 查询当前电脑运行的程序
obj = subprocess.Popen('ifconfig', shell=True,
                       stdout=subprocess.PIPE,# 获取指令正确的结果
                       stderr=subprocess.PIPE)

print(obj.stdout.read().decode('gbk'))
# print(obj.stderr.read().decode('gbk'))
