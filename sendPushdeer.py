import os
import sys
from pypushdeer import PushDeer  #pip install pypushdeer

push_key=os.environ["PUSH_KEY"] # 获取青龙环境变量PUSH_KEY
def findnewfile(path):
    lists = os.listdir(path)                                    #列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn:os.path.getmtime(path + "/" + fn))#按时间排序
    file_newest = os.path.join(path,lists[-1])                     #获取最新的文件保存到file_new
    return file_newest

# path0 = findnewfile(r"/ql/log/xxxx_change_pro") # 查询目录下最新日志
# path1 = findnewfile(r"路径2")
# path2 = findnewfile(r"路径3")

with open(path0, 'r') as f: # 获取日志内容
    str0=f.read()
# with open(path1, 'r') as f:
#     str1=f.read()
# with open(path2, 'r') as f:
#     str2=f.read()
content = str0 + str1 + str2 # 日志拼接

pushdeer = PushDeer(server="http://xxxxx:8800", pushkey=push_key) # 自建pushdeer推送服务器
# pushdeer = PushDeer(pushkey=push_key)  #默认服务器
pushdeer.send_text(content)
