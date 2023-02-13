"""任务功能"""

import time
import threading

from core import logs

all_task=[]

def add_task(name,function,status="loading",progress=-1): # 添加任务
    all_task.append({"name":name,"status":status,"function":function,"progress":progress})

class ProgressTools: # 函数内实用工具
    def set_progress(progress):
        all_task[0]["progress"] = progress
    def set_status(status):
        all_task[0]["status"] = status
    def log(*args,**kwargs):
        logs.log(*args,**kwargs)

def loop(): # 主循环
    while(1):
        if(len(all_task)==0):
            logs.log("INFO", f"waiting...", "TASKS")
        while(len(all_task)==0): time.sleep(1)
        logs.log("INFO", f"task [{all_task[0]['name']}] is start", "TASKS")
        try:
            all_task[0]["function"](ProgressTools)
        except:
            logs.log("ERROR", f"task [{all_task[0]['name']}] error", "TASKS") # 服务异常停止
        logs.log("INFO", f"task [{all_task[0]['name']}] is stop", "TASKS")
        del all_task[0]

class LoopThread (threading.Thread): #继承父类threading.Thread
    def __init__(self):
        threading.Thread.__init__(self)
        self.threadID = 1
        self.name = "CKL_TaskLoopService"
        self.counter = 1
    def run(self):
        logs.log("INFO", f"task service start", "TASKS") # 服务启动提醒
        loop()
        logs.log("ERROR", f"task service stop", "TASKS") # 服务异常停止

def start():
    LoopThread().start()
