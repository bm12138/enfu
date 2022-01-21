"""
驱动对象获取方法
"""
import time
from selenium import webdriver

def get_driver():

    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    # driver = webdriver.Edge()
    driver.maximize_window()
    return driver
if __name__ == '__main__':

    # get_driver().get("https://pwork.nf1000.com/index")

    get_driver().find_element_by_id("LAY-user-login-username").send_keys("endfu01")
    time.sleep(2)
    get_driver().find_element_by_id('LAY-user-login-password').send_keys("123654")

    get_driver().find_element_by_id("login-btn").click()

    # self.driver.get("http://pwork.nf1000.com/")
    get_driver().find_element_by_xpath("//a[@lay-tips='体检管理']").click()
    time.sleep(3)
    get_driver().find_element_by_xpath("//a[text()='已体检列表']").click()
    time.sleep(3)
    get_driver().switch_to.frame(get_driver().find_element_by_xpath("//iframe[@src='physicaledList']"))
    # self.driver.find_element_by_xpath("//table[@id='my-table']/../div[1]/div[1]/div[2]/table/tbody/tr[1]/td[11]/div/a").click()
    get_driver().find_element_by_xpath("//a[text()='体检报告'][1]").click()
    time.sleep(3)
