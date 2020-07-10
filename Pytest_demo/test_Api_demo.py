
from appium import webdriver


class TestApiDemo:

    def setup(self):
        desired_caps = {'platformName': 'Android', # 平台名称
                        'platformVersion': '5.1.1',  # 系统版本号
                        'deviceName': '127.0.0.1:62001',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                        'appPackage': 'io.appium.android.apis',  # apk的包名
                        'appActivity': '.ApiDemos',# activity 名称
                        'unicodeKeyboard':True
                       }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        self.driver.implicitly_wait(10)

    def test_apidemo(self):
        self.driver.find_element_by_accessibility_id('Views').click()
        #android下特定能用，滑屏操作
        self.driver.find_element_by_android_uiautomator(
        'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Popup Menu").instance(0));'
        ).click()
        #self.driver.swipe()
        #self.driver.find_element_by_accessibility_id('Popup Menu').click()
        self.driver.find_element_by_accessibility_id('Make a Popup!').click()

        assert len(self.driver.find_elements_by_xpath('//*[@text="Edit"]')) == 1

        self.driver.find_element_by_xpath('//*[@text="Search"]').click()

        assert 'Clicked popup menu item Search' in self.driver.find_element_by_xpath('//*[@class="android.widget.Toast"]').text




    def teardown(self):

        self.driver.quit()
