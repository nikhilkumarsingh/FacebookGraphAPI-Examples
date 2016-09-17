from selenium import webdriver
from bs4 import BeautifulSoup


def get_groups():
        browser = webdriver.Firefox()
        browser.get('https://m.facebook.com/login')

        username = raw_input("Enter username:")
        password = raw_input("Enter password:")

        emailElem = browser.find_element_by_name('email')
        emailElem.send_keys(username)
        passwordElem = browser.find_element_by_name('pass')
        passwordElem.send_keys(password)
        passwordElem.submit()

        browser.get('https://m.facebook.com/groups/?seemore')
        html_source = browser.page_source
        soup = BeautifulSoup(html_source)

        groups=[]

        for link in soup.findAll('a'):
                if 'groups' in link['href'] and 'create' not in link['href']:
                        group={}
                        group['id'] = (link['href'].split('/')[2]).split('?')[0]
                        group['name'] = link.get_text()
                        groups.append(group)

        browser.quit()
        return groups
