"""

"""
from selenium.webdriver.common.by import By
from config import Setting,user_config
from common.base_page import BasePage


class LoginPage(BasePage):
    """登录页面"""
    url = '/login'

    user_locator = (By.NAME, 'username')
    pwd_locator = (By.NAME, 'password')
    btn_locator = (By.XPATH, "//span[contains(text(),'登录')]")

    tzwh_success_info_locator = (By.XPATH, "//div[contains(text(),'{}')]".format(user_config.tzwh_expected))
    tzsp_success_info_locator = (By.XPATH, "//div[contains(text(),'{}')]".format(user_config.tzsp_expected))

    def get(self):
        """访问登录页面"""
        login_url = Setting.host + self.url
        self.driver.get(login_url)

    def login(self, username, pwd):
        """登录操作"""
        self.get()

        # 定位用户名
        user_elem = self.get_element(self.user_locator)
        # 3， 输入用户名；
        user_elem.send_keys(username)

        # 4， 定位密码；
        pwd_elem = self.get_element(self.pwd_locator)
        # 5, 输入密码
        pwd_elem.send_keys(pwd)

        # 6, 定位登录按钮；
        self.js_to_bottom(self.btn_locator)

    def get_tzwh_success_msg(self):
        """投资维护获取正确信息"""
        tzwh_success_elem = self.wait_presence_element(self.tzwh_success_info_locator)
        return tzwh_success_elem.text

    def get_tzsp_success_msg(self):
        """投资审批获取正确信息"""
        tzsp_success_elem = self.wait_presence_element(self.tzsp_success_info_locator)
        return tzsp_success_elem.text

    def get_invalid_msg(self):
        """获取未授权信息"""
        invalid_elem = self.get_element(self.invalid_info_locator)
        return invalid_elem.text
