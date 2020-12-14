import requests

def send_msg(text):
    token = "1464942755:AAHYdVxyuFEXLriq3rW7R_DlN0bs_DsDe6E"
    chat_id = "-403532973"
    url_req = "https://api.telegram.org/bot" + token +"/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())
