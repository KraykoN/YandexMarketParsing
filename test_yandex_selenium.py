import time
import re
import fake_useragent
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
line = "---------------------------------------------------------------"

# User-Agent
ua = fake_useragent.UserAgent()
user = ua.random
header = {'User-Agent': str(user)}

# Тор
ipSite = 'http://icanhazip.com'
address = requests.get(ipSite, headers=header)

# Check my ip address
print(line + "\n[*] IP your network:\n" + address.text + line)
print("[!] Connecting to the Tor network /", end="")

options = Options()
ua = UserAgent()
a = ua.random
user_agent = ua.random
print(line)
print('' + user_agent + '')
print(line)
options.add_argument(f'user-agent={user_agent}')
# Proxie tor's
proxie = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

# Connecting to the tor
try:
    address = requests.get(ipSite, proxies=proxie, headers=header)

# Not connected
except:
    connection = False
    print("/\n[x] Stopping connect to the Tor network\n" + line)

# Connected
else:
    connection = True
    print("/\n[+] Connected to the Tor network\n" + line)
    print("[*] IP Tor network:\n" + address.text + line)


finally:
    url = input("[!] Uniform Resource Locator:\nhttp://")
    full_url = 'https://' + url

    page = requests.get(full_url, proxies=proxie)
    soup = BeautifulSoup(page.text, "html.parser")
    print(page.text)
    result = re.findall(r'<a href=[\'\"]\/marka\/(.*?)\.html[\'\"]', page.text, re.IGNORECASE)
    print(result)
    with open("index2.html", "w", encoding='utf-8') as html1:
        for word in result:
            html1.write(word + '\n')
