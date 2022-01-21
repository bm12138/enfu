import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome


class AuthTest:
    def __init__(self):
        # 实例化Options()对象
        chrome_options = Options()
        # 添加属性
        # chrome_options.add_argument('--headless')  # 使用无头浏览器  :没有界面
        chrome_options.add_argument('--no-sandbox')  # 使用开发者模式
        # chrome_options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
        chrome_options.add_argument('--incognito')  # 使用无痕浏览
        self.driver = Chrome(options=chrome_options)

    def run(self):
        self.driver.maximize_window()
        self.driver.get("http://pwork.nf1000.com/")

        self.driver.find_element_by_id("LAY-user-login-username").send_keys("endfu01")
        time.sleep(2)
        self.driver.find_element_by_id('LAY-user-login-password').send_keys("123654")

        self.driver.find_element_by_id("login-btn").click()
        self.driver.find_element_by_xpath("//a[@lay-tips='体检管理']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//a[text()='已体检列表']").click()
        time.sleep(3)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@src='physicaledList']"))
        # self.driver.find_element_by_xpath("//table[@id='my-table']/../div[1]/div[1]/div[2]/table/tbody/tr[1]/td[11]/div/a").click()
        self.driver.find_element_by_xpath("//a[text()='体检报告'][1]").click()


if __name__ == '__main__':
    AuthTest().run()
