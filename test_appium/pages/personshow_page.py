from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from test_appium.pages.base_page import BasePage
from test_appium.pages.personaction_page import PersonactionPage

'''
个人信息展示页
'''
class PersonshowPage(BasePage):

    def goto_personaction_page(self):
        sleep(2)
        self.find(MobileBy.ID, 'h8g').click()
        return PersonactionPage(self.driver)