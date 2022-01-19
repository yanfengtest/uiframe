#定义测试用例级别的
import  pytest
from selenium import webdriver
from PO.TestDatas import Global_datas as GD
from PO.PageObjects.login_page import LoginPage
@pytest.fixture
def init_driver():  #打开浏览器，访问网址
    """
    前置：打开浏览器，访问网址
    后置：退出浏览器
    :return:
    """
    driver = webdriver.Chrome()
    driver.get(GD.login_url)
    yield driver
    driver.quit()


@pytest.fixture
def init_login(init_driver):
    LoginPage(init_driver).login(*GD.user_inv)
    yield init_driver