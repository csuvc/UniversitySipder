#!/usr/bin/env python
#-*- encoding:utf-8 -*-

'''获取域名所对应的ip地址'''

import socket

def run():
    with open('/opt/domain.txt') as f:
        for line in f:
            domain = line.strip()
            try:
                ip = socket.gethostbyname(domain)
                print domain,ip
            except:
                pass

if __name__ == '__main__':
    run()