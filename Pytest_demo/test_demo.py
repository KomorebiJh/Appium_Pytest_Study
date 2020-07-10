import time
#测试一下老哥
import pytest
import yaml
from appium import webdriver

def assert_that(param, param1):
    pass

def equal_to(param):
    pass


class TestDemo:

    search_data = yaml.safe_load(open("search.yaml","r"))

    print(search_data)

    def setup(self):
        desired_caps = {'platformName': 'Android', # 平台名称
                        'platformVersion': '5.1.1',  # 系统版本号
                        'deviceName': '127.0.0.1:62001',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                        'appPackage': 'com.xueqiu.android',  # apk的包名
                        'appActivity': '.common.MainActivity',# activity 名称com.xueqiu.android/.common.MainActivity
                        'unicodeKeyboard':True
                       }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        self.driver.implicitly_wait(15)

    # 外部数据驱动测试用例
    @pytest.mark.parametrize("keyword,expected_price",search_data)
    def test_search_from_yaml(self,keyword,expected_price):
        self.driver.find_element_by_id('home_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys(keyword)
        price = self.driver.find_element_by_id("current_price")
        print(price.text)

        assert float(price.text) > expected_price
        assert "price" in price.get_attribute("resource-id")
        assert_that(price.get_attribute("package"), equal_to("com.xueqiu.android"))

    #
    # #测试用例驱动
    # def test_search_from_testcase(self):
    #     TestCase("testcase.yaml").run(self.driver)

    def teardown(self):
        self.driver.quit()

# class TestCase:
#     def __init__(self,path):
#         file = open(path,"r")
#         self.steps = yaml.safe_load(file)
#
#     def run(self,driver:webdriver):
#         for step in self.steps:
#             element=None
#             print(step)
#
#             if isinstance(step,dict):
#                 if "id" in step.keys():
#                     element=driver.find_element_by_id(step["id"])
#                 elif "xpath" in step.keys():
#                     element=driver.find_elements_by_xpath(step["xpath"])
#                 else:
#                     print(step.keys())
#                 if "input" in step.keys():
#                     element.send_keys(step["input"])
#                 else:
#                     element.click()
#                 if "get" in step.keys():
#                     print(element.get_attribute(step["get"]))









