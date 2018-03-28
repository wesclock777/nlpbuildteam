import requests, json

url = "https://7etxwojv97.execute-api.us-east-1.amazonaws.com/prod/message"
auth_header = {'content-type': 'application/json'}
data = {
    "to_number": "+15123630687",
    "from_number": "+16284000095",
    "message": "Hello from Python Requests Test to Prod!"
}

r = requests.post(url, data=json.dumps(data), headers=auth_header)
print(r.status_code," ", r.content)
