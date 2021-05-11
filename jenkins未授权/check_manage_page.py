
import requests

def check_manage_exist(url):
    urls = []
    error_url = []
    path = "/manage"
    url = url+path
    try:
        resp = requests.get(url, verify=False,timeout=10)
        if "[Jenkins]" in resp.text:
            print("该url"+url+"存在未授权漏洞")
            Writefile(url)
        elif("login?from" in resp.text):
            print("该url不存在漏洞")
        else:
            print("未知错误，请手工查看")
            print(url)
    except BaseException as e:
        pass



def Writefile(url):
    with open("jenkins.txt", 'a+',encoding="utf-8")as e:
        e.write(url+"\n")




if __name__ == '__main__':

    filename = "jenkins_url.txt"
    with open(filename,'r',encoding="utf-8")as files:
        file = files.readlines()
        for fi in file:
            check_manage_exist(fi.strip())


