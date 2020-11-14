import requests

url ='http://127.0.0.1:8000/veh/'
response = requests.get(url)

response.status_code


response.json()
