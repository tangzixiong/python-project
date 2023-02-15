#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

'test1 模块'

__author__ = '张三'

import sys

def saying():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('参数太多!')

if __name__=='__main__':
    saying()