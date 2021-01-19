import requests

def send_msg(text):
    token = "Your token"        
    chat_id = "Your chat ID"                                           
    url_req = "https://api.telegram.org/bot" + token +"/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())
