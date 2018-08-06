#/usr/bin/env python
#-*- coding:utf-8 -*-

'''多进程批量子域名爆破'''

import os
from multiprocessing import Pool

__author__ = "@answer"

def run_subdomain(target):
    subdomains_brute_path = '/opt/subDomainsBrute/' #　subDomainsBrute工具路径
    os.chdir(subdomains_brute_path)
    os.system('python subDomainsBrute.py -i %s' % target)

if __name__ == '__main__':
    p = Pool(4)
    target_domains_file = '/root/桌面/answer/answer的军火库/edu_domain.txt' #　目标域名列表
    with open(target_domains_file, 'rt') as f:
        for line in f:
            line = line.strip()
            p.apply_async(run_subdomain,(line,))
    p.close()
    p.join()