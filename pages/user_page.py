from selenium.webdriver.common.by import By

from common.base_page import BasePage


class UserPage(BasePage):
    # 获取余额
    money_locator = (By.XPATH, "//li[@class='color_sub']")

    def get_money(self):
        """获取最新的用户余额"""
        e = self.get_element(self.money_locator)
        money = e.text[:-1]  #split
        return money
