from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyperclip
import sys

if len(sys.argv) > 1:
    profile = " ".join(sys.argv[1:])
    print(profile)
else:
    profile = "John Smith"

# Code nabbed from Stack Overflow to disable browser
# notifications for selenium

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.get("http://facebook.com")

email = browser.find_element_by_css_selector("#email")
password = browser.find_element_by_css_selector("#pass")

email.send_keys("username")
password.send_keys("password")

password.submit()

## Send status automatically ##

# status = browser.find_element_by_css_selector("._3en1")
# status.send_keys("This message brought to you automatically thanks to Python's selenium module:\n\nhttp://selenium-python.readthedocs.io/")
# status.submit()

messages = browser.find_element_by_css_selector("a[data-testid='left_nav_item_Messages']")
messages.click()

try:
    newMessage = WebDriverWait(browser, 45).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button._3mv"))
    )
    newMessage.click()
except:
    browser.quit()

try:
    search = WebDriverWait(browser, 45).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input.inputtext.textInput"))
    )
    search.click()
    search.send_keys(profile)
    search.send_keys(Keys.ENTER)
except:
    browser.quit()

messageToSend = browser.find_element_by_tag_name("textarea")
messageToSend.click()

messageToSend.send_keys("Hey, " + profile.split()[0] + ". This message was programmatically generated. Just ignore it. Thanks for playing :-)")
messageToSend.send_keys(Keys.RETURN)
