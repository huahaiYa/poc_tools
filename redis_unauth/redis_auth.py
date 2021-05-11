import redis
import threading

class myThread(threading.Thread):
    def __init__(self,url,thread):
        threading.Thread.__init__(self)
        self.url = url
        self.thread = thread

    def run(self):
        check_redis(self.url)


def check_redis(url):
    try:

        r = redis.Redis(host=url)
        info = r.info()
        if "redis_version" in info:
            print("存在未授权"+"\n")
            if "Linux" in info['os']:
                with open("success_linux.txt","a",encoding="utf-8")as e:
                    e.writelines(url+"\n")
            else:
                with open("success_windows.txt", "a", encoding="utf-8")as e:
                    e.writelines(url+"\n")

        else:
            print("不存在未授权")
    except BaseException as e:
        pass
if __name__ == '__main__':
    with open("result.txt",'r',encoding="utf-8")as e:
        urls = e.readlines()
        for url in urls:
            print(url)
            check_redis(url.strip())

    # check_redis()