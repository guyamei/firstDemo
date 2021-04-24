from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from test_appium.pages.add_member_page import AddMemberPage
from test_appium.pages.base_page import BasePage
from test_appium.pages.personshow_page import PersonshowPage


'''
通讯录页
'''


class ContactListPage(BasePage):

    def goto_addmemberpage(self):
        #通讯录页点击添加成员
        self.swipe_find('添加成员').click()
        return AddMemberPage(self.driver)

    def goto_personshow_page(self, username):
        #判断要删除人员是否存在
        ele = self.checkuserexist('checkexist', username)
        if ele:
           self.find(MobileBy.XPATH, f'//*[@text="{username}"]').click()
           return PersonshowPage(self.driver)
        else:
            print(f"删除{username}不在通讯录中")

    def checkuserexist(self, type, username):
        ele = WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((MobileBy.XPATH, f'//*[@text="企业通讯录"]/..//*[@text="{username}"]')), '元素不存在')
        bret = False
        if (type == 'checkexist' and ele is not None) or (type == 'checknotexist' and ele is None):
            bret = True
        return bret
