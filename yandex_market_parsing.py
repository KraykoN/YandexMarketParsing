import time
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

# Set User-Agent
ua = fake_useragent.UserAgent()
user = ua.random
header = {'User-Agent': str(user)}

# Тоr
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
    with open("index2.html", "w", encoding='utf-8') as html1:
        http = 'https://patiimaks.pl/wozki-dzieciece/'
        driver = webdriver.Chrome('path')
        driver.get("your_url")
        time.sleep(2)
        scroll_pause = 3
        last_height = driver.execute_script("return document.body.scrollHeight")
        list = []
        while True:
            # Scroll down to bottom
            driver.execute_script("scroll(0, 10005250);")

            # Wait to load page
            time.sleep(scroll_pause)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            # if new_height == last_height:
            #     break
            # last_height = new_height
            print(new_height)
            list.append(new_height)
            print(list)
            if list[-1] > 300000:
                break




        page = driver.page_source
        soup = BeautifulSoup(page)
        for tag in soup.findAll('a', {'class': 'product__link', 'href': True}):
            html1.write(tag['href'] + ' ' + '\n')
    # button = driver.find_element_by_xpath(".//a[@class='paginator-item transition-element last arrow']")
    # while button.is_displayed():
    #     element = WebDriverWait(driver, 10)
    #     actions = ActionChains(driver)
    #     actions.move_to_element(button).click().perform()
    #     time.sleep(3)

    #  # if url.split()[0] == url.split()[-1]:
    #  #     with open("index2.html", "w", encoding='utf-8') as html:
    # a = str()
    #            spans = soup.find_all("span", {"class": "n-images-set__caption"})
    #            for span in spans:
    #                for link in span.find_all('a'):
    #                    html.write(link.text + '\n')
    #           for tag in soup.findAll("a", {'class': "n-images-set__content"}):
    #               html.write('https://market.yandex.ru' + str(tag['href']) + ' ' + '\n')

    #      # for tag in soup.findAll('a', {'class': 'image', 'href': True}):
    #      #     html.write(str(tag['href']) + ' ' + '\n')

    #            tag = soup.find('a', class_="link link_theme_gray")
    #            print(tag.text)

    # for tag in soup.findAll('span', {'class': 'n-images-set__caption'}):
    # a = tag.find('p')
    #  print(a)
    #        print(line, "\nFile: 'index2.html' created")
    print(line)
