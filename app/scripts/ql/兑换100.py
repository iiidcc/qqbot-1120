import os,re,time,asyncio
import sys
sys.path.append(os.path.abspath('../../tmp'))
sys.path.append(os.path.abspath('.'))
try:
    import aiohttp
except Exception as e:
    print(e, "\n�����pip�汾��pip3 install --upgrade pip \nȱ��aiohttp ģ�飬��ִ�����װ: pip3 install aiohttp\n")
    exit(3)  

# ����
# ��ϲ�Ƹ����һ�100���,������
# 59 59 * * * * new
# ��������wy_debug_pin�����˺���&�ָ�,
'''
# ��������
export wy_debug_cycless="50"          # �ظ��������
export wy_debug_sleep="0.05"          # ������Ϊ0.05��
export wy_debug_pin="jd_997eefxx29"                # ��Ҫ������˺�coookie��pin,���˺���&�ָ�
'''

# �������������ڽű��ڲ�����,�������Ĭ�Ͻű��ڲ�����
wy_debug_url=f'https://m.jingxi.com/jxbfd/user/ExchangePrize?strZone=jxbfd&bizCode=jxbfd&source=jxbfd&dwEnv=7&_cfd_t=1636804796373&ptag=138631.135.2&dwType=3&dwLvl=3&ddwPaperMoney=100000&strPoolName=jxcfd2_exchange_hb_202111&strPgtimestamp=1636804796104&strPhoneID=3e06201310b55c90&strPgUUNum=88507d9af4ccfaace1b3e76138e9611c&_stk=_cfd_t%2CbizCode%2CddwPaperMoney%2CdwEnv%2CdwLvl%2CdwType%2Cptag%2Csource%2CstrPgUUNum%2CstrPgtimestamp%2CstrPhoneID%2CstrPoolName%2CstrZone&_ste=1&h5st=20211113195956373%3B3809223826488163%3B10032%3Btk01wad4a1ce130nqJk2GqGIzmI3HNLtvTYgObY0j4mDngkMk0T242O4Wn3o%2FxKaURexjotuIWtpnx6mJlfoq3umCUGX%3Be3d37baab41066bf742886a11c10c21787152597efbc834ff5c6ba89d7ef97b4&_=1636804796374&sceneval=2&g_login_type=1&callback=jsonpCBKPP&g_ty=ls'       # ��ϲ�Ƹ���100���api
wy_debug_headers={
    'Host':'m.jingxi.com',
    'accept':'*/*',
    'x-requested-with':'com.jd.pingou',
    'sec-fetch-mode':'no-cors',
    'sec-fetch-site':'same-site',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer':'https://st.jingxi.com/fortune_island/index2.html?ptag=7155.9.47&sceneval=2'
}        
wy_debug_manner='get'           
wy_debug_postdata=''            
wy_debug_cycless = '50'         
wy_debug_sleep = '0.05'         
wy_debug_pin=''                 

'''
{"coupon":[{"hongbao":[
    {"ddwAdvanceEndTm":0,"ddwAdvanceStartTm":0,"ddwAdvanceUnLockMoney":0,"ddwGoodsPrice":0,"ddwNeedPay":0,"ddwPaperMoney":1111000,"ddwPrice":111100,"ddwQuota":0,"ddwSecKillEndTm":0,"ddwSecKillPaperMoney":0,"ddwSecKillStartTm":0,"dwHbFirst":0,"dwIsAdvance":0,"dwIsNeedJxApp":0,"dwIsNewUserLead":0,"dwIsNewUserPrize":0,"dwIsPlatCoupon":0,"dwIsSecKill":0,"dwIsSecKillIng":0,"dwIsShowStock":0,"dwLvl":1,"dwPos":30001,"dwState":0,"dwStockNum":1,"dwUnLockLvl":10,"strPrizeName":"1111Ԫ","strPrizePic":"","strSkuId":""},

    {"ddwAdvanceEndTm":0,"ddwAdvanceStartTm":0,"ddwAdvanceUnLockMoney":0,"ddwGoodsPrice":0,"ddwNeedPay":0,"ddwPaperMoney":111000,"ddwPrice":11100,"ddwQuota":0,"ddwSecKillEndTm":0,"ddwSecKillPaperMoney":0,"ddwSecKillStartTm":0,"dwHbFirst":0,"dwIsAdvance":0,"dwIsNeedJxApp":0,"dwIsNewUserLead":0,"dwIsNewUserPrize":0,"dwIsPlatCoupon":0,"dwIsSecKill":0,"dwIsSecKillIng":0,"dwIsShowStock":0,"dwLvl":2,"dwPos":30002,"dwState":1,"dwStockNum":0,"dwUnLockLvl":8,"strPrizeName":"111Ԫ","strPrizePic":"","strSkuId":""},
    
    {"ddwAdvanceEndTm":0,"ddwAdvanceStartTm":0,"ddwAdvanceUnLockMoney":0,"ddwGoodsPrice":0,"ddwNeedPay":0,"ddwPaperMoney":100000,"ddwPrice":10000,"ddwQuota":0,"ddwSecKillEndTm":0,"ddwSecKillPaperMoney":0,"ddwSecKillStartTm":0,"dwHbFirst":0,"dwIsAdvance":0,"dwIsNeedJxApp":0,"dwIsNewUserLead":0,"dwIsNewUserPrize":0,"dwIsPlatCoupon":0,"dwIsSecKill":0,"dwIsSecKillIng":0,"dwIsShowStock":0,"dwLvl":3,"dwPos":30003,"dwState":1,"dwStockNum":0,"dwUnLockLvl":5,"strPrizeName":"100Ԫ","strPrizePic":"","strSkuId":""},
    
    {"ddwAdvanceEndTm":0,"ddwAdvanceStartTm":0,"ddwAdvanceUnLockMoney":0,"ddwGoodsPrice":0,"ddwNeedPay":0,"ddwPaperMoney":100,"ddwPrice":10,"ddwQuota":0,"ddwSecKillEndTm":0,"ddwSecKillPaperMoney":0,"ddwSecKillStartTm":0,"dwHbFirst":0,"dwIsAdvance":0,"dwIsNeedJxApp":0,"dwIsNewUserLead":0,"dwIsNewUserPrize":0,"dwIsPlatCoupon":0,"dwIsSecKill":0,"dwIsSecKillIng":0,"dwIsShowStock":0,"dwLvl":8,"dwPos":30004,"dwState":0,"dwStockNum":4534,"dwUnLockLvl":1,"strPrizeName":"0.1Ԫ","strPrizePic":"","strSkuId":""},
    
    {"ddwAdvanceEndTm":0,"ddwAdvanceStartTm":0,"ddwAdvanceUnLockMoney":0,"ddwGoodsPrice":0,"ddwNeedPay":0,"ddwPaperMoney":200,"ddwPrice":20,"ddwQuota":0,"ddwSecKillEndTm":0,"ddwSecKillPaperMoney":0,"ddwSecKillStartTm":0,"dwHbFirst":0,"dwIsAdvance":0,"dwIsNeedJxApp":0,"dwIsNewUserLead":0,"dwIsNewUserPrize":0,"dwIsPlatCoupon":0,"dwIsSecKill":0,"dwIsSecKillIng":0,"dwIsShowStock":0,"dwLvl":7,"dwPos":30005,"dwState":2,"dwStockNum":2549,"dwUnLockLvl":2,"strPrizeName":"0.2Ԫ","strPrizePic":"","strSkuId":""},
    
    {"ddwAdvanceEndTm":0,"ddwAdvanceStartTm":0,"ddwAdvanceUnLockMoney":0,"ddwGoodsPrice":0,"ddwNeedPay":0,"ddwPaperMoney":500,"ddwPrice":50,"ddwQuota":0,"ddwSecKillEndTm":0,"ddwSecKillPaperMoney":0,"ddwSecKillStartTm":0,"dwHbFirst":0,"dwIsAdvance":0,"dwIsNeedJxApp":0,"dwIsNewUserLead":0,"dwIsNewUserPrize":0,"dwIsPlatCoupon":0,"dwIsSecKill":0,"dwIsSecKillIng":0,"dwIsShowStock":0,"dwLvl":6,"dwPos":30006,"dwState":0,"dwStockNum":4735,"dwUnLockLvl":2,"strPrizeName":"0.5Ԫ","strPrizePic":"","strSkuId":""},
    
    {"ddwAdvanceEndTm":0,"ddwAdvanceStartTm":0,"ddwAdvanceUnLockMoney":0,"ddwGoodsPrice":0,"ddwNeedPay":0,"ddwPaperMoney":1000,"ddwPrice":100,"ddwQuota":0,"ddwSecKillEndTm":0,"ddwSecKillPaperMoney":0,"ddwSecKillStartTm":0,"dwHbFirst":0,"dwIsAdvance":0,"dwIsNeedJxApp":0,"dwIsNewUserLead":0,"dwIsNewUserPrize":0,"dwIsPlatCoupon":0,"dwIsSecKill":0,"dwIsSecKillIng":0,"dwIsShowStock":0,"dwLvl":5,"dwPos":30007,"dwState":0,"dwStockNum":361,"dwUnLockLvl":2,"strPrizeName":"1Ԫ","strPrizePic":"","strSkuId":""},
    
    {"ddwAdvanceEndTm":0,"ddwAdvanceStartTm":0,"ddwAdvanceUnLockMoney":0,"ddwGoodsPrice":0,"ddwNeedPay":0,"ddwPaperMoney":11000,"ddwPrice":1100,"ddwQuota":0,"ddwSecKillEndTm":0,"ddwSecKillPaperMoney":0,"ddwSecKillStartTm":0,"dwHbFirst":0,"dwIsAdvance":0,"dwIsNeedJxApp":0,"dwIsNewUserLead":0,"dwIsNewUserPrize":0,"dwIsPlatCoupon":0,"dwIsSecKill":0,"dwIsSecKillIng":0,"dwIsShowStock":0,"dwLvl":4,"dwPos":30008,"dwState":1,"dwStockNum":0,"dwUnLockLvl":5,"strPrizeName":"11Ԫ","strPrizePic":"","strSkuId":""}
    
    ]}}
'''
# ��ȡpin
cookie_findall=re.compile(r'pt_pin=(.+?);')
def get_pin(cookie):
    try:
        return cookie_findall.findall(cookie)[0]
    except:
        print('ck��ʽ����ȷ������')

# ua
def ua():
    try:
        from jdEnv import USER_AGENTS as a
    except:
        a='jdpingou;android;5.8.0;9;3e06201310b55c90;network/wifi;model/MI 6;appBuild/19037;partner/xiaomi;;session/4;aid/3e06201310b55c90;oaid/a697f773bf9c0cb0;pap/JA2019_3111789;brand/;eu/3356036323031333;fv/1303265353369303;Mozilla/5.0 (Linux; Android 9; MI 6 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36'
    return a


# ��ȡ��������
def get_env(env):
    try:
        if env in os.environ:
            a=os.environ[env]
        elif '/ql' in os.path.abspath(os.path.dirname(__file__)):
            try:
                a=v4_env(env,'/ql/config/config.sh')
            except:
                a=eval(env)
        elif '/jd' in os.path.abspath(os.path.dirname(__file__)):
            try:
                a=v4_env(env,'/jd/config/config.sh')
            except:
                a=eval(env)
        else:
            a=eval(env)
    except:
        a=''
    return a

# v4
def v4_env(env,paths):
    b=re.compile(r'(?:export )?'+env+r' ?= ?[\"\'](.*?)[\"\']', re.I)
    with open(paths, 'r') as f:
        for line in f.readlines():
            try:
                c=b.match(line).group(1)
                break
            except:
                pass
    return c 


## ��ȡcooie
class Judge_env(object):
    def main_run(self):
        if '/jd' in os.path.abspath(os.path.dirname(__file__)):
            cookie_list=self.v4_cookie()
        else:
            cookie_list=os.environ["JD_COOKIE"].split('&')       # ��ȡcookie_list�ĺϼ�
        if len(cookie_list)<1:
            msg('����д��������JD_COOKIE\n')    
        return cookie_list

    def v4_cookie(self):
        a=[]
        b=re.compile(r'Cookie'+'.*?=\"(.*?)\"', re.I)
        with open('/jd/config/config.sh', 'r') as f:
            for line in f.readlines():
                try:
                    regular=b.match(line).group(1)
                    a.append(regular)
                except:
                    pass
        return a
cookie_list=Judge_env().main_run()


async def get_url(cookie,n):
    await asyncio.sleep(sleep*n)
    headers = {
        'user-agent': ua,
        'cookie': cookie,
    }
    headers={**headers,**headers_env}
    try:      
        async with session.get(url, headers=headers) as res:
            res =await res.text(encoding="utf-8")
        print('�������')
        print(f'{res}\n')
    except:
        print('����ʧ��\n')
        return
    sys.stdout.flush()


async def post_url(cookie,n):
    await asyncio.sleep(sleep*n)
    headers = {
        'user-agent': ua,
        'cookie': cookie,
    }
    headers={**headers,**headers_env}
    if not data:
        try:      
            async with session.post(url, headers=headers) as res:
                res =await res.text(encoding="utf-8")
            print('�������')
            print(f'{res.text}\n')
        except:
            print('����ʧ��\n')
            return
    else:
        try: 
            async with session.post(url, headers=headers, data=data) as res:
                res =await res.text(encoding="utf-8")
            print('�������')
            print(f'{res.text}\n')
        except:
            print('����ʧ��\n')
            return    
    sys.stdout.flush()


async def asyncclass():
    tasks=list()

    global session
    async with aiohttp.ClientSession() as session:
        cycless=int(get_env('wy_debug_cycless'))
        if (manner:=get_env('wy_debug_manner'))=='get':
            for n in range(cycless):
                for cookie in cookie_list:
                    tasks.append(get_url(cookie,n))

        elif manner=='post':
            for n in range(cycless):
                for cookie in cookie_list:
                    tasks.append(post_url(cookie,n))

        else:
            print(f"��֧�ֵ�����ʽ {manner}")

        await asyncio.wait(tasks)


if __name__ == '__main__':
    ua=ua()
    debug_pin=get_env('wy_debug_pin')
    cookie_list=[cookie for cookie in cookie_list if get_pin(cookie) in debug_pin]
    url=get_env('wy_debug_url') 
    # try:
    #     headers_env = {header.split("=")[0]:''.join(header.split("=")[1:]) for header in get_env('wy_debug_headers').split('&')}
    # except:
    #     headers_env=dict()
    headers_env=wy_debug_headers
    data=get_env('wy_debug_postdata')
    sleep=float(get_env('wy_debug_sleep'))

    asyncio.run(asyncclass())
    
