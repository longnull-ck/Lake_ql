import requests,os,random
from requests.adapters import HTTPAdapter
url = 'https://mfg.wcczsoft.com/api/api/gatesdistributor/PutCheckIn'

def postImg(staffId,random_code):
    data = {
        'CustomerType': '修理厂',
        'KeHuUserID': staffId,
        'UploadedFileName':f'{random_code}.jpg',
        'UploadedFilePath':'https://wccz-mfg.oss-cn-shanghai.aliyuncs.com/gates/distributorcheckin/0f2fce2bbc5f31d23dc848f96778486_49D5E383A3A64870BF197DD6C72B3A28.jpg'
    }
    headers ={
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '298',
    'Host':'mfg.wcczsoft.com',
    'Origin': 'https://mfg.wcczsoft.com',
    'Referer': f'https://mfg.wcczsoft.com/html/gates/distributor_checkingarage.html?campaignId=PYQDKH5&staffId={staffId}&formId=requestFormId:fail%20deprecated&sharedByStaffId={staffId}&timestamp=2024-05-20T05:49:27.574098094Z&sign=AC3F89BFC545CF9BC068644F5E2E4110792A028D7F8ED600A5E6B82C5722FAE4',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': '''Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36'''
    }
    sess = requests.Session()
    sess.mount('http://', HTTPAdapter(max_retries=3)) 
    sess.mount('https://', HTTPAdapter(max_retries=3))     
    sess.keep_alive = False # 关闭多余连接
    requests.packages.urllib3.disable_warnings()
    res = requests.post(url,headers=headers,data=data,verify=False, )
    res = res.json()

    print(res['Message'],'本周打卡次数%d' % res['Data']['WeeklyCount'],'本月打卡次数%d' % res['Data']['MonthlyCount'])

def version():
    txt = requests.get("https://gitee.com/twoln/lake/raw/master/publick.txt").text
    print(txt)

 
def generate_random_code(length=6):
    code = ''
    for _ in range(length):
        # 随机选择大写字母还是数字
        if random.randint(0, 1):
            # 生成一个大写字母
            code += chr(random.randint(65, 90))
        else:
            # 生成一个数字
            code += str(random.randint(0, 9))
    return code
 
# 生成一个长度为5的随机编码





staffId = '' 
version()
if not staffId:
 staffId = os.getenv("cz_begcid")
if not staffId:
    print("❌你还没有设置ck,请设置环境变量:cz_begcid")
    exit()
staffId = staffId.split("@")
print(f"一共获取到{len(staffId)}个账号")
i = 1
for staffId in staffId:
    print(f"\n--------开始第{i}个账号--------")
    random_code = generate_random_code(30)
    postImg(staffId,random_code)
    print(f"--------第{i}个账号执行完毕--------")
    i+= 1
    
