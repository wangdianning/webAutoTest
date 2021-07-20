import datetime
import logging
import os
from webbrowser import Chrome
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import Setting


class BasePage:


    def __init__(self, driver:Chrome):

        self.driver = driver



    def screenshot(self):

        """保存截图

        时间戳

        """

        # 图片所在路径

        img_path = Setting.img_path

        # filename = str(int(time.time())) + '.png'

        # 截图文件名

        data = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        filename = data + '.png'

        # 拼接完整是截图文件路径

        file = os.path.join(img_path, filename)

        self.driver.save_screenshot(file)

        return file



    def get_element(self, locator):

        """查找元素"""

        try:

            e = self.driver.find_element(*locator)

            return e

        except Exception as e:

            logging.error("查找元素失败")

            # 截图

            self.screenshot()





    def wait_clickable_element(self, locator, timeout=120, poll=0.2):

        """等待元素可以被点击"""

        try:

            e = WebDriverWait(self.driver, timeout, poll).until(
                EC.element_to_be_clickable(locator)

            )

            return e

        except Exception as e:

            logging.error("查找元素失败")

            # 截图

            self.screenshot()



    def wait_presence_element(self, locator, timeout=120, poll=0.2):

        """等待元素可以加载"""

        try:

            e = WebDriverWait(self.driver, timeout, poll).until(

                EC.presence_of_element_located(locator)

            )

            return e

        except Exception as e:

            logging.error("查找元素失败")

            # 截图

            self.screenshot()



    def wait_visible_element(self, locator, timeout=120, poll=0.2):

        """等待元素可见"""

        try:

            e = WebDriverWait(self.driver, timeout, poll).until(

                EC.visibility_of_element_located(locator)

            )

            return e

        except Exception as e:

            # 截图

            self.screenshot()

            raise e



    def user_input(self, locator, data):

        """用户输入操作"""

        try:

            e = self.get_element(locator)

            e.send_keys(data)

        except Exception as e:

            self.screenshot()

            raise e



    def click(self, locator):

        """点击操作"""

        try:

            e = self.wait_clickable_element(locator)

            e.click()

        except Exception as e:

            self.screenshot()

            raise e



    def select(self, locator, data):

        """selector操作"""

        try:

            e = self.get_element(locator)

            select = Select(e)

            select.select_by_value(data)

        except Exception as e:


            self.screenshot()

            raise e



    def switch_frame(self, name):

        """iframe的切换"""

        self.driver.switch_to.frame(name)



    def double_click(self, locator):

        """双击操作"""

        try:

            e = self.get_element(locator)

            action = ActionChains(self.driver)

            action.double_click(e)

            action.perform()

        except Exception as e:
            self.screenshot()

            raise e



    def move_to(self, locator):

        """悬停操作"""

        try:

            e = self.get_element(locator)

            action = ActionChains(self.driver)

            action.move_to_element(e)

            action.perform()

        except Exception as e:

            self.screenshot()

            raise e


    def right_click(self, locator):

        """右击操作"""

        try:

            e = self.get_element(locator)

            action = ActionChains(self.driver)

            action.context_click(e)

            action.perform()

        except Exception as e:

            self.screenshot()

            raise e



    def drag_and_drop(self, locator1, locator2):

        """拖拽操作"""

        try:

            source = self.get_element(locator1)

            target = self.get_element(locator2)

            action = ActionChains(self.driver)

            action.drag_and_drop(source, target)

            action.perform()

        except Exception as e:

            self.screenshot()

            raise e



    def window_slide_to_bottom(self):

        """窗口滑动到底部"""

        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


    def js_to_bottom(self,locator):
        """js定位点击"""
        try:
            e = self.get_element(locator)
            js_code = 'arguments[0].click();'
            self.driver.execute_script(js_code,e)

        except Exception as e:

            self.screenshot()

            raise e

    def js_to_content(self, locator):
        """js定位选择内容"""
        try:
            e = self.get_element(locator)
            #click_and_hold()指的是按住鼠标左键在源元素上，点击并且不释放
            ActionChains(self.driver).click_and_hold(e).perform()
            js_code = 'arguments[0].readOnly = false;'
            self.driver.execute_script(js_code, e)

        except Exception as e:

            self.screenshot()

            raise e

    def js_to_send_content(self, locator,data):
        """js定位选择内容"""
        try:
            e = self.get_element(locator)
            js_code = "arguments[0].value= '{}'".format(data)
            self.driver.execute_script(js_code, e)

        except Exception as e:

            self.screenshot()

            raise e


    def change_to_alert(self):
        """切换到弹窗"""
        try:
            e = self.driver.switch_to.alert
            result = e.text
            return result

        except Exception as e:

            self.screenshot()

            raise e