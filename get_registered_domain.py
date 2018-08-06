#/usr/bin/env python
#-*- coding:utf-8 -*-

'''提取注册域名'''

__author__ = "@answer"

import tldextract

def run():
    with open('/opt/school_url.txt','rt') as f,open('/opt/domain.txt','at') as f2:
        for line in f:
            line = line.strip()
            ext = tldextract.extract(line)
            registered_domain =  ext.registered_domain
            print registered_domain
            f2.write(registered_domain + '\n')
if __name__ == '__main__':
    run()
