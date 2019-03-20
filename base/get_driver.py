# 定义一个get_driver方法，封装app自动化的前置代码
from appium import webdriver


def get_driver():
    # server 启动参数
    desired_caps = {}
    # 设备信息
    # 平台名 是android还是ios
    desired_caps['platformName'] = 'Android'
    # 系统版本号
    desired_caps['platformVersion'] = '5.1'
    # 进程名，后面的值可以不正确但是不能为空或者不传这个参数
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # app的信息
    # 包名
    desired_caps['appPackage'] = 'com.vcooline.aike'
    # 启动名
    desired_caps['appActivity'] = '.umanager.LoginActivity'
    # 声明我们的driver对象
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
