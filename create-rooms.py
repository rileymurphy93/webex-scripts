import requests

access_token = 'NzhiOWQ1ZTYtNzNiZS00YTM3LTg3M2EtNWQ5ZjZmMWQ4MDA4ZWNlYTEyMGYtMTJh_P0A1_cb0fa6b7-6c1c-45f5-aae5-b00413680b83'
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'title': 'DevNet Associate Training!'}
res = requests.post(url, headers=headers, json=params)
print(res.json())
