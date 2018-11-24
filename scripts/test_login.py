import pytest
import os,sys
sys.path.append(os.getcwd())
from base.get_driver import getdriver
from page.page_login import PageLogin
import demo

class TestLogin():
    def setup_class(self):
        self.login = PageLogin(getdriver())
    def teardown_class(self):
        self.login.driver.quit()
    # 定义test方法,来输入,姓名,密码.点击登录
    @pytest.mark.parametrize('username,password,result',demo.read())
    def test_login(self,username,password,result):
        self.login.page_input_username(username)
        self.login.page_input_password(password)

        self.login.page_click_login_btn()
        print(result)

# if __name__ == '__main__':
#     pytest.main()