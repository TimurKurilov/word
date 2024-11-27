import requests

url = "https://libretranslate.com/translate"
json = {
    "q": "hello",
    "source": "en",
    "target": "ru",
    "format": "text",
    "alternatives": 3,
    "api_key": ""
    
}
proxies = {
    "http": "http://MdBB2R:qXZMdk@185.214.75.214:8000",
    "https": "http://MdBB2R:qXZMdk@185.214.75.214:8000"
}

response = requests.post(url, json=json, proxies=proxies)
print(response.text)