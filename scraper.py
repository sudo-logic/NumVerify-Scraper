import requests
from bs4 import BeautifulSoup
from hashlib import md5

#INSERT PHONE NUMBERS HERE
number_list = [9999999999,8888888888]

session = requests.Session()

#UNCOMMENT TO ADD PROXIES
# session.proxies = {
#   'http': 'http://208.86.120.136:3128',
#   'https': 'socks5://83.97.23.90:18080',
# }

soup = BeautifulSoup(session.get('https://numverify.com/').text, features="html.parser")
scl_secret = soup.findAll('input')[1]['value']

for number in number_list:
    number = '91'+ str(number)
    key = md5((number + scl_secret).encode()).hexdigest()
    loc = (session.get('https://numverify.com/php_helper_scripts/phone_api.php?secret_key={}&number={}'.format(key,number)).json().get('location'))
    print(number, loc)