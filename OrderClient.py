import requests

endpoint="http://127.0.0.1:8000/auth"
username="henselwilson"
password="Newuser123"

auth_token=requests.post(endpoint,json={'username':username,'password':password})
print(auth_token.json())

if auth_token.status_code==200:
    token=auth_token.json()['token']
    endpoint = "http://127.0.0.1:8000/order"
    header = {
        'Authorization': f"Token {token}"
    }
    print(header['Authorization'])
    data = {
        'phone':'Redmi 10',
        'quantity': 1
    }
    result = requests.post(endpoint, json=data, headers=header)
    print(result.json())