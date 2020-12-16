b'''
Author: YanQiaoYu
Github: https://github.com/yanqiaoyu?tab=repositories
Date: 2020-12-15 16:15:16
LastEditors: YanQiaoYu
LastEditTime: 2020-12-15 16:15:17
FilePath: \My-OpenFalcon-Push\system_monitor.py
'''

import psutil
import time
import subprocess

class system_monitor:
    '''监控系统一些自定义的参数'''
    def system_uptime(self):
        '''启动时间'''
        return int((time.time() - psutil.boot_time())/60/60)

    def zombie_proc(self):
        '''异常进程总数'''
        zombie_sum = 0
        zombie_sum += int(subprocess.getoutput(f"ps -A -ostat,ppid,pid,cmd | grep -e '^[Zz]' | wc -l"))
        zombie_sum += int(subprocess.getoutput(f"ps -A -ostat,ppid,pid,cmd | grep -e '^[Dd]' | wc -l"))
        zombie_sum += int(subprocess.getoutput(f"ps -A -ostat,ppid,pid,cmd | grep -e '^[Tt]' | wc -l"))
        return zombie_sum

if __name__ == '__main__':
    A = system_monitor()
    print(A.zombie_proc())
    print(A.system_uptime())