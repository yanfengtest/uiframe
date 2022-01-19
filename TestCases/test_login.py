from selenium import webdriver
from PO.Common.logger import logger
from PO.PageObjects.home_page import HomePage
from PO.PageObjects.login_page import LoginPage
import pytest
from PO.TestDatas import Global_datas as GD, login_datas as lds


@pytest.fixture
def init(init_driver):
    logger.info("login用例的前置")
    lp = LoginPage(init_driver)
    yield init_driver,lp   #init_driver driver对象    lp页面对象
    logger.info("login用例的后置")

@pytest.mark.usefixtures("init")
class TestLogn():

    def test_login_success(self,init):
        #步骤
        # 1 登录操作
        init[1].login(*lds.success)
        # 断言
        assert HomePage(init[0]).get_element_exists()

    @pytest.mark.parametrize("case",lds.cases)
    def test_login_failed(self,case,init):
        init[1].login(case['username'],case['passwd'])
        assert init[1].get_error_msg_from_login_form()==case['check']


