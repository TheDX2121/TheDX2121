import requests
from fake_useragent import UserAgent
from faker import Faker

banner = """
CODED BY @im_satyam_chauhan
"""

print("\033[31m",banner,"\033[0m")

target_user = input("Enter the target username [@abc]: ")

fake = Faker()

text = """Hello sir/ma'am,

I would like to report a Telegram user who is engaging in suspicious and harmful activities. Their username is """+target_user+""" . I believe they may be involved in scams and phishing attempts, which is causing harm to the community. I would appreciate it if you could look into this matter and take appropriate action.

Thank you for your attention to this matter.
"""



def report():
    username = fake.user_name()
    domain = fake.free_email_domain()
    email = f"{username}@{domain}"

    #print(email)

    country_code = fake.country_calling_code()
    mobile_number = fake.random_number(digits=10)
    generated_number = f"{country_code}{mobile_number}"

    #print(generated_number)
    
    user_agent = UserAgent().random

    cookies = {
        'stel_ln': 'en',
        'stel_ssid': 'f578802e99c4b87012_3506401586024839227',
    }

    headers = {
        'User-Agent': user_agent,
        'Accept-Language': 'en,en-US;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://telegram.org',
        'Connection': 'keep-alive',
        'Referer': 'https://telegram.org/support',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    data = {
        'message': text,
        'email': email,
        'phone': generated_number,
        'setln': '',
    }

    try:
        response = requests.post('https://telegram.org/support', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()

        if "We will try to reply as soon as possible." in response.text:
            print(response ,f" \033[32m{email} : Report done !!\033[0m")
        else:
            print(response,"\033[31mReport Failed.\033[0m")
    except requests.exceptions.RequestException as e:
        return "Error: " + str(e)

while True:
    report()