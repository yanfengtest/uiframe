from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PO.PageLocators.home_page_locs import HomePagelocs as loc


class HomePage:



    def __init__(self,driver:WebDriver):
        self.driver = driver  #初始化drivr

    #退出元素是否存在，如果存在返回True,如果不存在，返回False
    def get_element_exists(self):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc.exit_link))
        except:
            return False
        else:
            return True








