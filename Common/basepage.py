import logging
import os
import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PO.Common.dir_config import screenshot_dir
from PO.Common.logger import logger

class BasePage:

    def __init__(self,driver:WebDriver):
        self.driver = driver  #初始化drivr

    #等待元素
    def wait_ele_visible(self,loc,img_name,timeout=20,poll_fre=0.5):
        """
        :param loc:
        :param img_name:
        :param timeout:
        :param poll_fre:
        :return:
        """
        logger.info("{}等待{}元素可见。".format(img_name,loc))
        try:
            WebDriverWait(self.driver,timeout,poll_frequency=poll_fre).until(EC.visibility_of_element_located(loc))
        except:
            self.save_page_shot(img_name)
            logger.exception("等待元素可见失败：")
            raise

    #查找元素
    def get_emement(self,loc,img_name):
        logger.info("在{}查找元素{}".format(img_name,loc))
        try:
            ele = self.driver.find_element(*loc)
        except:
            self.save_page_shot(img_name)
            logger.exception("查找元素失败")
            raise
        else:
            return ele

    #查找元素们
    def get_emements(self,loc,img_name):
        logger.info("在{}查找所有的匹配的元素{}".format(img_name,loc))
        try:
            eles = self.driver.find_elements(*loc)
        except:
            self.save_page_shot(img_name)
            logger.exception("查找元素失败")
            raise
        else:
            return eles

    #点击
    def click_element(self,loc,img_name,timeout=20,poll_fre=0.5):
        logger.info("在{}对{}进行点击操作".format(img_name, loc))
        self.wait_ele_visible(loc,img_name,timeout,poll_fre)
        ele = self.get_emement(loc,img_name)
        try:
            ele.click()
        except:
            self.save_page_shot(img_name)
            logger.exception("点击失败")
            raise

    #输入
    def input_text(self,loc,value,img_name,timeout=20,poll_fre=0.5):
        """
        :param loc:
        :param value:
        :param img_name:
        :param timeout:
        :param poll_fre:
        :return:
        """
        logger.info("在{}对元素{}输入{}".format(img_name, loc,value))
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)
        ele = self.get_emement(loc, img_name)
        try:
            ele.send_keys(value)
        except:
            self.save_page_shot(img_name)
            logger.exception("输入失败")
            raise

    #元素存在
    def  wait_page_contain_element(self):
        pass

    #等待元素可点击
    def wait_ele_clickable(self,loc,img_name,timeout=20,poll_fre=0.5):
        logger.info("{}等待{}元素可见。".format(img_name, loc))
        try:
            WebDriverWait(self.driver, timeout, poll_frequency=poll_fre).until(EC.element_to_be_clickable(loc))
        except:
            self.save_page_shot(img_name)
            logger.exception("等待元素不可点击：")
            raise


    #获取属性
    def get_ele_attribute(self,loc,attr_name,img_name,timeout=20,poll_fre=0.5):
        logger.info("在{}获取元素{}的{}属性".format(img_name, loc,attr_name))
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)
        ele = self.get_emement(loc, img_name)
        try:
            vaule = ele.get_attribute(attr_name)
        except:
            self.save_page_shot(img_name)
            logger.exception("属性获取失败")
            raise
        else:
            logger.info("属性为{}".format(vaule))
            return vaule
    #切换到新的窗口

    #js执行
    #上传（windows）
    # iframe切换
    def swith_to_iframe(self,loc,img_name):
        """
        :param loc: 可以是元祖 name  id 都是可以的
        :param img_name:
        :return:
        """
        try:
            WebDriverWait(self.driver,20).until(EC.frame_to_be_available_and_switch_to_it(loc))#等待+切换
        except:
            self.save_page_shot(img_name)
            logger.exception("{}页面切换错误".format(img_name))
            raise

    #获取文本
    def get_ele_text(self,loc,img_name,timeout=20,poll_fre=0.5):
        """
        :param loc:
        :param img_name:
        :param timeout:
        :param poll_fre:
        :return:
        """
        logger.info("在{}获取元素{}文本内容".format(img_name, loc))
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)
        ele = self.get_emement(loc, img_name)
        try:
            text = ele.text
        except:
            self.save_page_shot(img_name)
            logger.exception("文本获取失败")
            raise
        else:
            logger.info("文本值为{}".format(text))
            return ele.text

    def save_page_shot(self,img_name):
        """

        :param img_name: 页面名称_页面行为
        :return:
        """
        #将图片存储到Outputs的screenshots下，图片命名：页面名称_页面行为_时间.png
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        print(now)
        screenshot_path = screenshot_dir+"/{}_{}.png".format(img_name,now)
        print(screenshot_path)
        self.driver.save_screenshot(screenshot_path)
        logger.info("页面图片保存在：{}".format(screenshot_path))
        print("结束")


