import unittest
from selenium import webdriver
from PO.PageObjects.home_page import HomePage
from PO.PageObjects.login_page import LoginPage
from PO.TestDatas import Global_datas as GD, login_datas as lds


class TestInvest(unittest.TestCase):

    def setUp(self) -> None:
        # 访问登录页面
        self.driver = webdriver.Chrome()
        self.driver.get(GD.login_url)
        self.driver.maximize_window()
        #使用投资人账号登录
        LoginPage(self.driver).login(*GD.user_inv)

    def tearDown(self) -> None:
        self.driver.quit()

    #正向场景 ，投资成功
    def test_invest_success(self):
        pass



    #逆向场景，投资失败
    # 1 进入输入框格式错误，数据不符合要求
    # 2 你的钱不够
    # 3 标的钱不够
    def test_login_failed(self, case):
        pass




