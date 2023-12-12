import requests
import re
import string
import random
import time
def get_access_token(urlpre, payload):
    url = urlpre + "/api/auth/login"

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        match = re.search(r'"access_token":"([^"]+)"', response.text)

        if match:
            access_token = match.group(1)
            print({"access_token": access_token})
            return access_token
        else:
            print("无法找到access_token")
            return None
    else:
        print(f"请求失败，状态码: {response.status_code}")
        print(response.text)
        return None

def register_fake_open(urlpre, access_token):
    url = urlpre + "/api/token/register"
    random_string = ''.join(random.choices(string.ascii_letters, k=8))
    payload = f"unique_name={random_string}&access_token={access_token}&site_limit=&expires_in=0&show_conversations=true&show_userinfo=true"
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    response = requests.post(url, headers=headers, data=payload)
    
    print(response.text)
    
    match = re.search(r'"token_key":"([^"]+)"', response.text)
    
    if match:
        return match.group(1)
    else:
        return None
def register_pooltoken(urlpre, login_payloads, pool_token):
    # 用于存储所有的 access_token
    fake_tokens = []

    # 遍历每个登录请求
    for payload in login_payloads:
        fake_token = register_fake_open(urlpre,get_access_token(urlpre,payload))
        delay_time = random.uniform(10, 30)
        time.sleep(delay_time)
        if fake_token:
            fake_tokens.append(fake_token)

    # 打印所有获取到的 access_token
    print("所有的 access_token:", fake_tokens)

    fake_token_all = '\n'.join(fake_tokens)

    # 更新池信息
    update_url =urlpre + "/api/pool/update"
    update_payload = f"share_tokens={fake_token_all}\n&&pool_token={pool_token}"
    update_headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    update_response = requests.post(update_url, headers=update_headers, data=update_payload)

    print(update_response.text)
    return None
def main():
    urlpre="" #url+前缀
    pool_token="" #pooltoken
    # 示例 login_payload，这里假设是一个字符串数组
    login_payloads = [
        '', # 'username=帐号&password=密码'
        '' # 'username=帐号&password=密码'
        # 添加其他payloads...
    ]
    register_pooltoken(urlpre, login_payloads, pool_token)
    
if __name__ == "__main__":
    main()