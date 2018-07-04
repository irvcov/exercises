import requests
import json

headers = {'Authorization': 'Basic 7754285443ac89ff7eb66655834d9df20dff64b4880113d5e78a17404bd31524'}
url = "https://www.smartshoot.com/api/prospects/{0}".format(503835)

r = requests.get(url, headers=headers)

obj = json.loads(r.text)

print(obj)
