from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.pages.base_page import BasePage


class AddMemberPage(BasePage):

    def addmember_click(self):
        #click 手动输入添加
        sleep(3)
        self.find(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        from test_appium.pages.editmember_page import EditMemberPage
        return EditMemberPage(self.driver)


    '''
    强制等待，捕获toast
    '''
    def verify_ok(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((MobileBy.XPATH, '//*[@text="添加成功"]')))