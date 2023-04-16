import requests
import json

access_token = 'NzhiOWQ1ZTYtNzNiZS00YTM3LTg3M2EtNWQ5ZjZmMWQ4MDA4ZWNlYTEyMGYtMTJh_P0A1_cb0fa6b7-6c1c-45f5-aae5-b00413680b83'
url = 'https://webexapis.com/v1/people/me'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
