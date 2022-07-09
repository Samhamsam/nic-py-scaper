import requests
from bs4 import BeautifulSoup

NIC_DOMAIN = "https://www.nic.py/consultdompy.php"
session = requests.Session()
page = session.get(NIC_DOMAIN)

soup = BeautifulSoup(page.content, "html.parser")

# get html
hidden_input = soup.find_all("input", type="hidden")
select_input = soup.find_all("select")
domain_input = soup.find_all("input", class_="input-xlarge")

# get name and values
domain_name = domain_input[0]["name"]
domain_value = "your-value"

hidden_name = hidden_input[0]["name"]
hidden_value = hidden_input[0]["value"]

select_name = select_input[0]["name"]
select_value = "com" # net, coop, org, mil, gov 


payload = {domain_name: domain_value, hidden_name: hidden_value, select_name: select_value}
r = requests.post(NIC_DOMAIN, data=payload, cookies=session.cookies.get_dict())


answ = BeautifulSoup(r.content, "html.parser")

test  = answ.find_all("h4")

if len(test) != 3:
    print("Is free")
else:
    print("Is taken")
