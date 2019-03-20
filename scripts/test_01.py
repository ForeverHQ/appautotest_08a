import pytest
import os
import sys
# 将当前路径添加到环境变量中
sys.path.append(os.getcwd())
from base.get_driver import get_driver
from page.page_login import PageLogin


# 定义一个测试类
class TestLogin:
    # 定义setup方法
    def setup(self):
        self.login = PageLogin(get_driver())

    # 定义teardown方法
    def teardown(self):
        self.login.driver.quit()

    # 定义测试类
    @pytest.mark.parametrize("username, pwd", [("admin", "123")])
    def test_login(self, username, pwd):
        self.login.page_login(username, pwd)
