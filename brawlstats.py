from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
brawltag = str(input("What is your tag?"))
brawlurl = str('https://brawlstats.com/profile/')+str(brawltag)
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
driver.get(brawlurl)