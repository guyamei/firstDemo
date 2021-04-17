import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.wait import WebDriverWait

from test_selenium.page.add_member_page import AddMemberPage
from test_selenium.page.base_page import BasePage
from test_selenium.page.contact_page import ContactPage


class MainPage(BasePage):

    def goto_add_member(self):

        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.ww_indexImg_AddMember')))

        self.driver.find_element(By.CSS_SELECTOR, '.ww_indexImg_AddMember').click()

        return AddMemberPage(self.driver)


    def goto_contact(self):

        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'menu_contacts')))

        self.driver.find_element(By.ID, 'menu_contacts').click()

        return ContactPage(self.driver)




