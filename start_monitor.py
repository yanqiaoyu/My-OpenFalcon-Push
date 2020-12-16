b'''
Author: YanQiaoYu
Github: https://github.com/yanqiaoyu?tab=repositories
Date: 2020-12-15 17:29:01
LastEditors: YanQiaoYu
LastEditTime: 2020-12-15 17:29:01
FilePath: \My-OpenFalcon-Push\start_monitor.py
'''

from agent_monitor import agent_proc_monitor, agent_log_monitor, agent_watchdog_monitor
from system_monitor import system_monitor
from glob_func import post_metric, Agent_EndPointName

A = agent_log_monitor()
B = agent_proc_monitor()
C = system_monitor()
D = agent_watchdog_monitor()
#agent
'''CPU占用百分比'''
post_metric(Agent_EndPointName, 'Agent_CPU', B.agent_cpu())
'''mem中RSS这个参数 单位MB'''
post_metric(Agent_EndPointName, 'Agent_mem_RSS,单位MB', B.agent_mem_rss())
'''mem中VMS这个参数 单位MB'''
post_metric(Agent_EndPointName, 'Agent_mem_VMS,单位MB', B.agent_mem_vms())
'''mem中shared这个参数 单位MB'''
post_metric(Agent_EndPointName, 'Agent_mem_shared,单位MB', B.agent_mem_shared())
'''agent所打开的句柄'''
post_metric(Agent_EndPointName, 'Agent占用的句柄数', B.agent_openfiles())

#agent watchdog
'''agent_watch_dog所打开的句柄'''
post_metric(Agent_EndPointName, 'Agent占用的句柄数', D.agent_watchdog_openfiles())


#agent log
'''整个存放日志文件的文件夹大小,单位是KB'''
post_metric(Agent_EndPointName, 'Agent日志文件大小', A.agent_log_size())
'''日志文件夹下，日志文件个数'''
post_metric(Agent_EndPointName, 'Agent日志文件个数', A.agent_log_count())

#system
'''启动时间'''
post_metric(Agent_EndPointName, '系统启动了多久，单位小时', C.system_uptime())
'''异常进程总数'''
post_metric(Agent_EndPointName, '异常进程数：僵尸，睡眠，停止', C.zombie_proc())