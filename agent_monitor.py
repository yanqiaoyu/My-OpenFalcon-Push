b'''
Author: YanQiaoYu
Github: https://github.com/yanqiaoyu?tab=repositories
Date: 2020-12-15 10:46:01
LastEditors: YanQiaoYu
LastEditTime: 2020-12-15 11:15:34
FilePath: \My-OpenFalcon-Push\agent_monitor.py
'''
import psutil
import subprocess
import os
from os.path import join, getsize
from glob_func import get_pid, Agent_Name, Agent_Log_Path, Agent_WatchDog_Name
import glob

class agent_proc_monitor:
    '''监控agent进程'''
    def __init__(self):
        '''实例化的时候,获取一次句柄'''
        self.p = psutil.Process(int(get_pid(Agent_Name)))

    def agent_cpu(self):
        '''CPU占用百分比'''
        return self.p.cpu_percent()

    def agent_mem_rss(self):
        '''mem中RSS这个参数 单位MB'''
        return round(self.p.memory_info().rss/1024/1024, 2)

    def agent_mem_vms(self):
        '''mem中VMS这个参数 单位MB'''
        return round(self.p.memory_info().vms/1024/1024 ,2)

    def agent_mem_shared(self):
        '''mem中shared这个参数 单位MB'''
        return round(self.p.memory_info().shared/1024/1024 ,2)

    def agent_openfiles(self):
        '''agent所打开的句柄'''
        List = self.p.open_files()
        sum = 0
        for i in List:
            sum += int(i.fd)
        return sum

class agent_watchdog_monitor:
    '''监控agent的watchdog'''
    def __init__(self):
        '''实例化的时候,获取一次句柄'''
        self.p = psutil.Process(int(get_pid(Agent_WatchDog_Name))) 

    def agent_watchdog_openfiles(self):
        '''agent_watch_dog所打开的句柄'''
        List = self.p.open_files()
        sum = 0
        for i in List:
            sum += int(i.fd)
        return sum

class agent_log_monitor:
    '''监控agent相关日志'''
    def __init__(self):
        '''实例化的时候,获取一次句柄'''
        self.p = psutil.Process(int(get_pid(Agent_Name)))

    def agent_log_size(self):
        '''整个存放日志文件的文件夹大小,单位是KB'''
        size = 0
        for root, dirs, files in os.walk(Agent_Log_Path):
            size += sum([getsize(join(root, name)) for name in files])
        return round(size/1024, 2)

    def agent_log_count(self):
        '''日志文件夹下，日志文件个数'''
        path_file_number=len(glob.glob(Agent_Log_Path + '*.log'))
        return path_file_number

if __name__ == '__main__':
    A = agent_proc_monitor()
    B = agent_log_monitor()
    C = agent_watchdog_monitor()
    # print(B.agent_log_size())
    # print(B.agent_log_count())
    # print(A.agent_cpu())
    # print(A.agent_mem_rss())
    # print(A.agent_mem_shared())
    # print(A.agent_mem_vms())
    # print(A.agent_openfiles())
    print(C.agent_watchdog_openfiles())
