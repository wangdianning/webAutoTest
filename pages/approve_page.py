"""

"""
import time

from selenium.webdriver.common.by import By
from config import Setting
from common.base_page import BasePage
from data import landName

class ApprovePage(BasePage):
    # 项目主数据
    xm_locator = (By.XPATH, "//span[@title='项目主数据']")
    # 项目管理
    xmgl_locator = (By.XPATH, "//span[@title='项目管理']")
    # 待办事项
    dbzx_locator = (By.XPATH,"//span[@title='待办事项']")
    #审核
    verify_locator =  (By.XPATH,"//div[contains(text(),'{}')]/../following-sibling::td//button".format(landName))
    #同意
    approve_locator = (By.XPATH,"//span[text()='同意']")
    #不同意
    not_approve_locator = (By.XPATH,"//span[text()='不同意']")

    #弹窗
    approve_success = (By.XPATH, "//p[contains(text(),'操作成功')]")

    def approve(self):
        # 点击项目主数据
        self.js_to_bottom(self.xm_locator)

        # 点击项目管理
        self.js_to_bottom(self.xmgl_locator)

        # 点击待办事项
        self.js_to_bottom(self.dbzx_locator)

        #点击操作按钮
        self.js_to_bottom(self.verify_locator)

        #点击同意按钮
        self.js_to_bottom(self.approve_locator)
        time.sleep(2)

    def get_approve_success_msg(self):
        """投资维护获取正确信息"""
        approve_success_elem = self.wait_presence_element(self.approve_success)
        return approve_success_elem.text


