import datetime

from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from Pytest_demo.pagebase.main_page import MainPage


class App:

    driver:WebDriver=None
    @classmethod

    def start(cls):
        desired_caps = {'platformName': 'Android',  # 平台名称
                        'platformVersion': '5.1.1',  # 系统版本号
                        'deviceName': '127.0.0.1:62001',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                        'appPackage': 'com.xueqiu.android',  # apk的包名
                        'appActivity': '.common.MainActivity',  # activity 名称com.xueqiu.android/.common.MainActivity
                        'unicodeKeyboard': True
                        }
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        cls.driver.implicitly_wait(15)


        def loaded(driver):
            print(datetime.datetime.now())
            if len(cls.driver.find_element_by_id('image_cancel')) >=1:
               cls.driver.find_element_by_id('image_cancel').click()
               return True
            else:
               return False

        try:
           WebDriverWait(cls.driver, 20).until(loaded)
        except:
           print('no update')

        return MainPage(cls.driver)

    @classmethod
    def quit(cls):
        cls.driver.quit()






