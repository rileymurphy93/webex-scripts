import requests
import json

access_token = 'NzhiOWQ1ZTYtNzNiZS00YTM3LTg3M2EtNWQ5ZjZmMWQ4MDA4ZWNlYTEyMGYtMTJh_P0A1_cb0fa6b7-6c1c-45f5-aae5-b00413680b83'
url = 'https://webexapis.com/v1/people'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {
    'email': 'rileymurphy93@outlook.com'
}
res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))

person_id = 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS84Mjg4NzRkNy1jOGU5LTQ3OWYtODc5Ni0zMWQ2MDllZGExZTc'
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
