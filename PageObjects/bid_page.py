
from PO.Common.basepage import BasePage
from PO.PageLocators.bid_page_locs import BidPageLocs as locs

class BidPage(BasePage):

    #获取用户余额
    def get_user_money(self):
        return self.get_ele_attribute(locs.money_input,"data-amount","标页面_获取用户投资余额")
    #获取标的余额
    def get_bid_money(self):
        return  self.get_ele_text(locs.bid_money_text,"标页面_获取标的可投余额")

    #输入2000，点击投标
    def invest(self,money):
        self.input_text(locs.money_input,money,"标页面_输入投资金额")
        self.click_element(locs.invest_button,"标页面_点击投资按钮")

    #查看并激活按钮
    def click_active_bitton_in_success_popup(self):
        self.click_element(locs.active_button_on_successPop,"标页面_投标成功的弹出框点击查看并激活按钮")


