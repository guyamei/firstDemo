from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_selenium.page.base_page import BasePage


class ContactPage(BasePage):

    def add_member(self):
        pass

    def get_list(self):

        ele_list = self.driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')

        name = [i.text for i in ele_list]

        return name

    def add_department(self, name):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.member_colLeft_top_addBtnWrap')))
        self.driver.find_element(By.CSS_SELECTOR, '.member_colLeft_top_addBtnWrap').click()

        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.js_create_party')))
        self.driver.find_element(By.CSS_SELECTOR, '.js_create_party').click()

        if self.driver.find_element(By.CSS_SELECTOR, '.member_tag_dialog').is_displayed() is True:
            self.driver.find_element(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[1]/input').send_keys(name)
            self.driver.find_element(By.CSS_SELECTOR, '.qui_btn.ww_btn.ww_btn_Dropdown.js_toggle_party_list').click()
            if self.driver.find_element(By.CSS_SELECTOR, '.qui_dialog_body .qui_dropdownMenu').is_displayed() is True:
                self.driver.find_elements(By.CSS_SELECTOR, '.qui_dialog_body .jstree-anchor')[1].click()
                self.driver.find_element(By.CSS_SELECTOR, '.qui_dialog_foot .ww_btn_Blue').click()



