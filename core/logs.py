import time

def gett(): # 获取时间
    return time.strftime('%H:%M:%S', time.localtime())

def log(level,text,module="core"): # 输出日志
    ttime=gett()
    print(f"[{level}][CKL {module}][{ttime}] {text}")
