from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver

chrome_options = Options()
chrome_options.experimental_options("detach", True)

driver = webdriver.Chrome(chrome_options)

driver.get("")