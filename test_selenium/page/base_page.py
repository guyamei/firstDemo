from selenium import webdriver


class BasePage:

    def __init__(self, base_driver = None):
        if base_driver is not None:
            self.driver = base_driver
        else:
            # 使用浏览器复用模式
            chrome_arg = webdriver.ChromeOptions()
            # 加入调试地址
            chrome_arg.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=chrome_arg)
            self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
            self.driver.implicitly_wait(3)
