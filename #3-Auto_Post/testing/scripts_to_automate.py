from selenium import webdriver
from assets import save_cookie,load_cookie
from pathlib import Path
path = Path.cwd()
print(path)
driver = webdriver.Chrome()
driver.get('http://website.internets')

foo = input()

save_cookie(driver, '/tmp/cookie')
load_cookie(driver, 'path/to/cookie')
driver = webdriver.Chrome()
