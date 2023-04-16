import requests

access_token = 'NzhiOWQ1ZTYtNzNiZS00YTM3LTg3M2EtNWQ5ZjZmMWQ4MDA4ZWNlYTEyMGYtMTJh_P0A1_cb0fa6b7-6c1c-45f5-aae5-b00413680b83'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vZmMwNWUwZDAtZGNhZC0xMWVkLTlhNTgtNDNlZTIxYzQ3ZmFk'
message = 'Hello **DevNet Associates**!!'
url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())

