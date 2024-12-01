import time
import requests
import json
import warnings
import urllib3

# 忽略 SSL 警告
warnings.simplefilter('ignore', urllib3.exceptions.InsecureRequestWarning)

def GameLogin():
    url = "https://wsgo.minigame.qq.com/GameLogin/OnlineBatch"

    headerss = {
        "Host": "wsgo.minigame.qq.com",
        "User-Agent": "QQGameHall",
        "Accept": "*/*",
        "Cookie": "pt4_token=JPkeLD7KnxMeac0rLNb-hwUJQdLWsUIN8X0YbZIuTGw_; p_skey=tLhsQ9I7JOKGi5ZpK9ZK*kI315lJd0J9iiFMt-foHHE_; p_uin=o2941556477; ptcz=472ffbe0898f2f592b7642b5d6502281c08857bded79d16777812ad3bac810f8; skey=@QIGCcVP9z; uin=o2941556477; RK=uGU5OMUHsT",
        "Content-Type": "text/plain",
        "Referer": "http://www.qq.com"
    }

    data = {
        "Page": "hall",
        "BatchInfo": [
            {
                "Uin": 2941556477,
                "AppID": "10302",
                "Duration": 300
            }
        ]
    }

    # Convert data to JSON string
    json_data = json.dumps(data)

    # Send POST request
    response = requests.post(url, headers=headerss, data=json_data, verify=False)

    # Print the response content
    if response.status_code == 200:
        print("Request successful")
        print(response.text)  # You can print the response here or handle it further
    else:
        print(f"Request failed with status code {response.status_code}")


def tab():
    url = "https://data.ab.qq.com/tab/get_experiments"

    headers = {
        "Host": "data.ab.qq.com",
        "Accept": "*/*",
        "Accept-Encoding": "gzip",
        "Content-Type": "application/proto",
        "Content-Length": "135"
    }

    # 这是你提供的二进制数据（已转为十六进制格式）
    # 注意：需要将二进制数据正确编码到 Python 中。此处以十六进制表示。
    data = b'\x04\x56\x00\x12\x26\x7B\x44\x45\x42\x41\x33\x36\x2D\x42\x32\x39\x41\x2D\x33\x33\x38\x38\x2D\x42\x41\x37\x31\x2D\x46\x32\x45\x42\x46\x46\x35\x36\x39\x44\x42\x7D\x1A\x15\x0A\x0A\x70\x63\x5F\x6F\x73\x5F\x76\x65\x72\x73\x69\x6F\x6E\x12\x04\x02\x13\x1A\x0E\x0A\x0F\x0C\x31\x31\x2E\x39\x38\x2E\x37\x33\x32\x37\x2E\x30\x1A\x13\x0A\x05\x70\x63\x5F\x6F\x73\x5F\x74\x79\x70\x65\x12\x05\x03\x77\x69\x6E\x52\x12\x07\x56\x00\x01'

    # Send POST request
    response = requests.post(url, headers=headers, data=data, verify=False)

    # Print the response content
    if response.status_code == 200:
        print("Request successful")
        print(response.text)  # You can print the response here or handle it further
    else:
        print(f"Request failed with status code {response.status_code}")
# Call the function


# 每隔 5 分钟 (300秒) 调用一次 GameLogin 和 tab
while True:
    GameLogin()  # 调用 GameLogin
    tab()        # 调用 tab
    time.sleep(300)  # 等待 5 分钟
