#!-*- coding:utf8 -*-

b'''
Author: YanQiaoYu
Github: https://github.com/yanqiaoyu?tab=repositories
Date: 2020-12-15 14:41:48
LastEditors: YanQiaoYu
LastEditTime: 2020-12-15 19:10:46
FilePath: \My-OpenFalcon-Push\glob_func.py
'''

import subprocess
import requests
import time
import json

Agent_Name = 'hecate_agent'
Agent_WatchDog_Name = 'hecate_agent_monitor.sh'
Agent_Log_Path = '/var/log/hecate_agent/'

Agent_EndPointName = '稳定性Agent_26.28'


def get_pid(process_name):
    '''获取agent的pid号'''
    for i in range(3):
        try:
            agent_pid = subprocess.getoutput(f"pidof {process_name} -x")
            if agent_pid != None:
                break
        except Exception as e:
            print(e)
            time.sleep(3)
            continue
    
    return agent_pid

def post_metric(endpoint, metric, value, counterType='GAUGE', tags='自定义监控参数', url='127.0.0.1'):
    '''推送数据至agent'''
    ts = int(time.time())
    payload = [
    {
        "endpoint": endpoint,
        "metric": metric,
        "timestamp": ts,
        "step": 60,
        "value": value,
        "counterType": counterType,
        "tags": tags,
    } ]

    r = requests.post(f"http://{url}:1988/v1/push", data=json.dumps(payload))

    print(r.text)