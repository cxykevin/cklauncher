"""路径操作"""

import os

# 导入配置
from core import settings


def get_path_list(): # 获取所有路径
    with open(settings.PATH_LIST_FILE) as file:
        path_list=eval(file.read())["list"]
    return path_list

def add_path(name, path): # 添加路径
    with open(settings.PATH_LIST_FILE) as file:
        path_list=eval(file.read())
    if(name in path_list["list"]):
        return True
    path_list["list"][name]={
                "path": path,
                "can_delete": 1
            }
    return False

