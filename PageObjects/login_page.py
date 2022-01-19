from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PO.Common.basepage import BasePage
from PO.PageLocators.login_page_locs import LoginPageLocs as  locs

class LoginPage(BasePage):

    def login(self,username,password):
        self.input_text(locs.user_input,username,"登录页面_输入用户名")
        self.input_text(locs.passwd_input,password,"登录页面_输入密码")
        self.click_element(locs.login_button,"登录页面_点击登录按钮")

    def get_error_msg_from_login_form(self):
        self.wait_ele_visible(locs.msg_from_login_form,"登录页面_获取登录表单的错误提示元素")
        eles = self.get_emements(locs.msg_from_login_form,"登录页面_获取登录表单的错误提示元素们")
        if len(eles) ==1:
            return  eles[0].text
        elif len(eles) >1:
            text_list = []
            for el in eles:
                text_list.append(el)
            return text_list




