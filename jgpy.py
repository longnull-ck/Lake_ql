import requests,os

def sing(Authorization):
    headers = {
        'Host': 'smp-api.iyouke.com',
        'Connection': 'keep-alive',
        'appId': 'wx3b294e7a0ba29bc3',
        'envVersion': 'release',
        'content-type': 'application/json',
        'Authorization': Authorization,
        'xy-extra-data': 'appid=wx3b294e7a0ba29bc3;version=2.3.8;envVersion=release;senceId=1005',
        'version': '2.3.8',
        # 'Accept-Encoding': 'gzip,compress,br,deflate',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003112) NetType/WIFI Language/zh_CN',
        'Referer': 'https://servicewechat.com/wx3b294e7a0ba29bc3/39/page-frame.html',
    }

    res = requests.get('https://smp-api.iyouke.com/dtapi/points/user/centerInfo', headers=headers)
    res = res.json()
    if res['success'] == True :
        print('当前账号积分为：%d' % res['data']['pointsBalance'])
    else:
        print(res)


staffIdArr = 'bearera16c0bcbaaa944bb88620403808c4bdc1718164391089@bearera16c0bcbaaa944bb88620403808c4bdc1718164391089'
if not staffIdArr:
    staffIdArr = os.getenv("lake_jgpy")
if not staffIdArr:
    print("❌你还没有设置ck,请设置环境变量:lake_jgpy")
    exit()
staffIdArr = staffIdArr.split("@")
print(f"一共获取到{len(staffIdArr)}个账号")
i = 1
for staffId in staffIdArr:
    print(f"\n--------开始第{i}个账号--------")
    sing(staffId)
    print(f"--------第{i}个账号执行完毕--------")
    i += 1


