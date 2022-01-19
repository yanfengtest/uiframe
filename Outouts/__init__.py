import pytest
from selenium import webdriver

def init():
    driver = webdriver.Chrome()
    driver.get("https:www.baidu.com")
    yield
    driver.quit()


