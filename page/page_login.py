from selenium.webdriver.common.by import By

from base.base import Base
loc_username = (By.ID, "com.vcooline.aike:id/etxt_username")
loc_pwd = By.ID, "com.vcooline.aike:id/etxt_pwd"
loc_login_btn = By.ID, "com.vcooline.aike:id/btn_login"
class PageLogin(Base):
    # 输入用户名
    def page_input_username(self,name):
        self.base_input(loc_username,name)

    # 输入密码
    def page_input_password(self,pwd):
        self.base_input(loc_pwd,pwd)
    # 点击登录
    def page_click_login_btn(self):
        self.base_click(loc_login_btn)

