from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.pages.base_page import BasePage


class EditpersonPage(BasePage):

    def delete_member(self):
        self.swipe_find('删除成员').click()
        self.verify_delete()

        from test_appium.pages.contactlist_page import ContactListPage
        return ContactListPage(self.driver)

    '''
        强制等待，捕获toast
        '''

    def verify_delete(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((MobileBy.XPATH, '//*[@text="确定"]'))).click()