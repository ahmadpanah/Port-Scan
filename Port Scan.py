#!/usr/bin/env python

import socket

def main():
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(1000)
    ip=input('آدرس هاست هدف را وارد کنید：(پیشفرض:127.0.0.1)')
    if ip=='':
        ip='127.0.0.1'

    s=input('پورت شروع：(پیشفرض:20)')
    if s=='':
        startport=20
    else:
        startport=int(s)

    s=input('پورت پایان：(پیشفرض:20)')
    if s=='':
        endport=20
    else:
        endport=int(s)

    for port in range(startport,endport+1):
        print('در حال اسکن پورت：%d' % port)
        try:
            sk.connect((ip,port))
            print('Server %s port %d OK!' % (ip,port))
        except Exception:
            print('Server %s port %d is not connected!' % (ip,port))
    sk.close()

if __name__ == '__main__':
    main()