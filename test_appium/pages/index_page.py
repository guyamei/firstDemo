#首页封装
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.pages.base_page import BasePage
from test_appium.pages.contactlist_page import ContactListPage


class IndexPage(BasePage):

    def goto_contactlist(self):
        '''
        //*[contains(@resourec-id, 'login')]
        //*[@text='登录']
        //*[contains(@resource-id, 'login') and contains(@class, 'EditText')]
        '''
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((MobileBy.XPATH, '//*[@text="通讯录"]')), '获取通讯录元素失败').click()
        #self.find(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        return ContactListPage(self.driver)
