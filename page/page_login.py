# 定义一个PageLogin类
from base.base import Base
import page


class PageLogin(Base):
    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.pwd, pwd)

    # 点击登录
    def page_click_login_btn(self):
        self.base_click(page.login)

    # 组装方法：
    def page_login(self, username, pwd):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()
