import requests
from data_input import data_in

URL = 'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data = {"input": data_in}

# sending get request and saving the response as response object
r = requests.get(URL, headers=headers, json=data)

# extracting data in json format
r.json()