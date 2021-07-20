"""

"""
from selenium.webdriver.common.by import By
from config import user_config
from common.base_page import BasePage


class LoginOutPage(BasePage):
    """注销页面"""
    tzwh_userinfo_locator = (By.XPATH, "//div[contains(text(),'{}')]".format(user_config.tzwh_expected))
    tzsp_userinfo_locator = (By.XPATH, "//div[contains(text(),'{}')]".format(user_config.tzsp_expected))
    loginout_locator = (By.XPATH, "//span[contains(text(),'注销')]")
    success_info_locator =(By.XPATH, "//div[contains(text(),'盟拓 【产品】V8主数据系统DEV')]")


    def tzwh_loginout(self):
        # 1、移动到用户名
        self.move_to(self.tzwh_userinfo_locator)

        # 2、点击注销
        self.js_to_bottom(self.loginout_locator)

    def tzsp_loginout(self):
        # 1、移动到用户名
        self.move_to(self.tzsp_userinfo_locator)

        # 2、点击注销
        self.js_to_bottom(self.loginout_locator)



    def get_success_msg(self):
        """获取正确信息"""
        success_elem = self.wait_presence_element(self.success_info_locator)
        return success_elem.text

