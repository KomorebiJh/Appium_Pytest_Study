from appium.webdriver.webdriver import WebDriver

from Pytest_demo.pagebase.search_page import SearchPage


class MainPage(object):

    def __init__(self,driver:WebDriver):
        self.driver=driver
    def to_search(self):
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        return SearchPage(self.driver)

