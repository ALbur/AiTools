import os
import smtplib 
from email.mime.text import MIMEText 
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

mail_host = 'smtp.office365.com' # outlook smtp
mail_user = 'xxxx@outlook.com' # 发送者账户 smtp
mail_pass = 'xxxx' # 发送者密码 smtp
sender = 'xxxx@outlook.com' # 发送者账户 smtp
receivers = ['xxxx@outlook.com'] # 接收者账户



message = MIMEText(content,'plain','utf-8') 
message['Subject'] = '每日推送'
message['From'] = sender 
message['To'] = receivers[0] 
  
try: 
 smtp = smtplib.SMTP(mail_host,587)
 smtp.set_debuglevel(False) # 查看实时登录日志信息
 smtp.ehlo()
 smtp.starttls()#   starttls()来建立安全连接
 smtp.ehlo()
 smtp.login(mail_user,mail_pass)
 smtp.sendmail(sender,receivers,message.as_string()) 
 smtp.quit() 
 print('success') 
except smtplib.SMTPException as e: 
 print('error',e)