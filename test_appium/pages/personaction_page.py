from appium.webdriver.common.mobileby import MobileBy

from test_appium.pages.base_page import BasePage
from test_appium.pages.editperson_page import EditpersonPage

'''
个人信息操作页
'''
class PersonactionPage(BasePage):

    def goto_editperson_page(self):
        self.find(MobileBy.XPATH, '//*[@text="编辑成员"]').click()
        return EditpersonPage(self.driver)