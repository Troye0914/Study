import json
import os
from config.setting import user_data
# 专门对数据进行保存以及读取，修改的模块


# 保存数据
def save_data(user_info):
    user_name = user_info['user_name']
    with open(f'{user_data}/{user_name}.json', 'w', encoding='utf-8') as f:
        json.dump(user_info, f)


# 查看数据
def select_data(user_name):
    user_path = f'{user_data}/{user_name}.json'
    if os.path.exists(user_path):
        with open(user_path, 'r', encoding='utf-8')as f:
            user_data1 = json.load(f)
            return user_data1
