from time import sleep

from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.contact_page import ContactPage


class AddMemberPage(BasePage):

    def add_member(self, name, aid, phone):
        sleep(3)
        self.driver.find_element(By.ID, 'username').send_keys(name)
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys(aid)
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, '.qui_btn.ww_btn.js_btn_save').click()

        return ContactPage(self.driver)

    def goto_contact(self):
        pass