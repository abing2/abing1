from selenium.webdriver.support.wait import WebDriverWait
class Base():
    # "这里写的都是常用的方法"
    def __init__(self,driver):
        self.driver = driver
    def base_find_element(self,loc,time=30,poll=0.5):
        # "查找元素使用显示等待来查找,"
        return WebDriverWait(self.driver,timeout=time,poll_frequency=poll)\
            .until(lambda x:x.find_element(*loc))
    def base_click(self,click_loc):
        self.base_find_element(click_loc).click()
    def base_input(self,input_loc,input):
        # "找到元素,先清空在输入"
        el = self.base_find_element(loc=input_loc)
        # '清空'
        el.clear()
        # "输入"
        el.send_keys(input)