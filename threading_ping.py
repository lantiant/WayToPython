#!/usr/bin/python3
#coding: utf-8

import threading
import time
import os
import sys
import re

start_time = time.time()

def get_ip_list(ip_range):
    '''

    :param ip_range: get a ip range from sys argv[1]
    :return: a ip address list,eg:192.168.1.1,192.168.1.2,...,192.168.1.254
    '''
    ip_start = int(ip_range.split('-')[0].split('.')[-1])
    ip_end = int(ip_range.split('-')[1])
    ip_list = []
    for ip_tail in range(ip_start, ip_end + 1):
        ip = '.'.join(sys.argv[1].split('-')[0].split('.')[0:3]) + '.' + str(ip_tail)
        ip_list.append(ip)
    return ip_list

def threading_ping(ipaddr):
    ping_result = os.popen('ping -c 3 -i 0.2 ' + ipaddr).read().split('\n')[-2]
    if re.match('.*100.0% packet loss$', ping_result):
        print(ipaddr + " icmp is not ok.")
    else:
        print(ipaddr + " icmp is ok.")
    time.sleep(0.1)

def main():
    '''

    :return: threading ping
    '''
    for ipaddr in get_ip_list(ip_range):
        ping_thread = threading.Thread(target=threading_ping, args=(ipaddr,))
        ping_thread.start()

    main_thread = threading.currentThread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            #print(some_thread)
            some_thread.join()

    print("\nElapsed time: " + str(time.time() - start_time))

if __name__ == '__main__':
    ip_range = sys.argv[1]
    main()