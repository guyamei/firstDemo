from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.pages.base_page import BasePage


class EditMemberPage(BasePage):

    def edit_member(self,username, phonenum):
        '''
        edit username
        edit phone
        :return:点击保存，跳转到添加成员页
        '''
        self.find(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../*[@text="必填"]').send_keys(username)
        self.find(MobileBy.XPATH, '//*[contains(@text, "手机")]/..//*[@text="必填"]').send_keys(phonenum)
        bfind = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((MobileBy.XPATH, '//*[@text="保存"]')))
        print(bfind)
        if bfind:
            self.find(MobileBy.XPATH, '//*[@text="保存"]').click()
        else:
            print("保存按钮不可点击")
        from test_appium.pages.add_member_page import AddMemberPage
        #导入写在方法内，可防止循环导入
        return AddMemberPage(self.driver)