from appium.webdriver.webdriver import WebDriver


class SearchPage(object):

    def __init__(self,driver:WebDriver):
        self.driver=driver

    def search(self,keyword):

        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys(keyword)
        return self

    def get_current_price(self):

        return float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)


