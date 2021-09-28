import requests
import json

from time import sleep


api_key = ""
url = "https://api.random.org/json-rpc/1/invoke"

try:
    with open("config.json") as file:
        api_key = json.load(file)["apiKey"]
    
except Exception as ex:
    print(ex)
    with open("config.json", "w") as file:
        file.write("""
{"apiKey": ""}

""")
        
if api_key.replace(" ", "") == "":
    print("Please, enter your API key from 'https://api.random.org/dashboard'")
    exit()
    
data = {
    "jsonrpc": "2.0",
    "method": "generateIntegers",
    "params": {
        "apiKey": api_key,
        "n": 1,
        "min": 1,
        "max": 2,
        "replacement": True
        
    },
    "id": 1
}

data = json.dumps(data)

# 1 - орел
# 2 - решка

n = 0
s = 0

while n < 11:
    response = json.loads(requests.post(url=url, data=data).text)
    
    try:
        result = response["result"]
    except:
        print(f"ERROR: RESPONSE: {response}")
    log_text = ""
    
    if result["requestsLeft"] < 1:
        log_text += "Кол-во запросов закончилось\n\n"
        break
    
    number = result["random"]["data"][0]
    
    if s != number:
        s = number
        n = 1
    else:
        n += 1
        
    if number == 1:
        print("Выпал орел ")
        log_text += "Выпал орел. "
    else:
        log_text += "Выпала решка "
        print("Выпала решка ")
        
    log_text += f"Подряд выпало: {n}\n"
    
    print(f"Подряд выпало: {n}\n")
    
    with open("logs.log", "a") as log:
        log.write(log_text)
    
    sleep(0.1)


    
