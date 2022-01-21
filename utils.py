"""
驱动对象获取方法
"""
import time

from appium import webdriver


def get_driver():
    """获取驱动对象方法"""
    # 获取驱动对象
    capabilities = {
        "platformName": "Android",  # 测试平台（Android、iOS）
        "platformVersion": "5.1.1",  # 测试系统版本
        "deviceName": "f100",  # 测试设备名称
        # "platformVersion": "6.0.1",  # 测试系统版本
        # "deviceName": "YOGAE7E5EAB0",  # 测试设备名称
        "appPackage": "com.nf.health",  # 待测应用的包名
        "appActivity": ".activity.login.LoginActivity",  # 待测应用的启动名
        # 输入中文设置
        "resetKeyboard": True,
        "unicodeKeyboard": True,
        # 获取toast
        "automationName": "Uiautomator2",
        #"noReset": "true"
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
    return driver  # 添加函数返回值




if __name__ == '__main__':
    a = get_driver()  # 调试使用
    a.find_element_by_id("com.nf.health:id/iv_login_go").click()
    time.sleep(2)