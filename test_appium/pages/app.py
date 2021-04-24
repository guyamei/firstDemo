#启动 重启 关闭
from time import sleep

from appium import webdriver

from test_appium.pages.base_page import BasePage
from test_appium.pages.index_page import IndexPage


class App(BasePage):

    def start(self):
        if self.driver == None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '10'
            desired_caps['deviceName'] = 'HJS0218C07002713'
            desired_caps['appPackage'] = 'com.tencent.wework'
            desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
            desired_caps['noReset'] = 'true'
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def quit(self):
        self.driver.quit()

    def goto_main(self):
        return IndexPage(self.driver)