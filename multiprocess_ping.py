#!/usr/bin/python3
#coding:utf-8

import multiprocessing
import time
import os
import re
import sys


def ips(ip_range):
    ip_start = int(ip_range.split('-')[0].split('.')[-1])
    ip_end = int(ip_range.split('-')[1])
    ip_list = []
    for ip_tail in range(ip_start, ip_end + 1):
        ip = '.'.join(ip_range.split('-')[0].split('.')[0:3]) + '.' + str(ip_tail)
        ip_list.append(ip)
    return ip_list



def multi_ping(ipaddr):
    ping_result = os.popen('ping -c 3 -i 0.2 ' + ipaddr).read().split('\n')[-2]
    if re.match('.*100.0% packet loss$', ping_result):
        print(ipaddr + " icmp is not ok.")
    else:
        print(ipaddr + " icmp is ok.")
    time.sleep(0.1)

if __name__ == '__main__':
    start_time = time.time()
    #ip_range = '192.168.9.1-25'
    ip_range = sys.argv[1]
    iplist = ips(ip_range)
    pool = multiprocessing.Pool(processes=100)
    for ipaddr in iplist:
        pool.apply_async(multi_ping, (ipaddr, ))
    pool.close()
    pool.join()
    print('\nHave Done! Elapsed time was {0} seconds: '.format(str(time.time() - start_time)))
