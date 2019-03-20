# 定义一个Base类，封装公共方法
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 定义driver属性，获取driver
    def __init__(self, driver):
        self.driver = driver

    # 定义查找元素的方法：
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).\
            until(lambda x: x.find_element(*loc))

    # 定义元素的点击操作方法
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 定义在元素内输入内容的操作方法
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        # 清空
        el.clear()
        # 输入内容
        el.send_keys(value)
