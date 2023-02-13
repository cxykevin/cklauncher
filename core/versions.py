"""版本操作"""

import os

# 导入配置
from core import settings
from core import paths
from core import download
from core import checkhash

def get_version_list(): # 获取所有版本
    path_list=paths.get_path_list()
    all_version=[]
    for this_name, this_path in path_list.items(): # 遍历所有路径
        tpath_vlist=os.listdir(this_path["path"] + "version/") # 读取所有版本
        for this_version in tpath_vlist: # 遍历当前路径下的版本
            all_version.append(
                {
                    "name": this_version, 
                    "path": this_path + this_version
                }
            )
    return all_version

def download_version(path,name,version,other): # 安装一个版本
    os.mkdir(path+"version"+"/"+name+"/") # 创建目录
    try: # 下载集群
        download.download_json(path, version)
        if("assist" in os.listdir(path)):
            if(checkhash.checkass(download.get_ass_hask())):
                download.download_ass(path)
        else:
            download.download_ass(path)
        if("library" in os.listdir(path)):
            if(checkhash.checklib(download.get_lib_hask())):
                download.download_lib(path)
        else:
            download.download_lib(path)
        download.download_version(path+"version"+"/"+name+"/",version)
    except:
        return True
    return False

