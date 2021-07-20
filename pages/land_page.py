"""

"""
import time

from selenium.webdriver.common.by import By
from common.base_page import BasePage
from data import landName


class LandPage(BasePage):
    # url = '/login'
    #项目主数据
    xm_locator = (By.XPATH,"//span[@title='项目主数据']")
    #项目管理
    xmgl_locator = (By.XPATH, "//span[@title='项目管理']")
    #地块列表
    dk_locator = (By.XPATH,"//span[@title='地块列表']")
    #新增列表
    create_land_locator = (By.XPATH, "//span[contains(text(),'新增列表')]")
    #变更列表
    change_land_locator = (By.XPATH, "//span[contains(text(),'变更列表')]")
    #已审核列表
    land_locator = (By.XPATH, "//span[contains(text(),'已审核列表')]")
    #城市公司
    city_locator = (By.XPATH,"//span[contains(text(),'苏州城市公司')]")
    #新增按钮
    btn_create_locator = (By.XPATH,"//button[@type='button']/span[contains(text(),'新增')]")
    #保存按钮
    btn_save_locator = (By.XPATH,"//span[contains(text(),'保存')]")

    #选择项
    project_gain_value = (By.XPATH, "//span[contains(text(),'勾地')]")
    land_usage_value = (By.XPATH, "//span[contains(text(),'产业用地')]")
    province_value = (By.XPATH, "//span[contains(text(),'江苏省')]")
    city_value = (By.XPATH, "//span[contains(text(),'苏州市')]")
    region_value = (By.XPATH, "//span[contains(text(),'苏州市本级')]")

    #基本信息
    land_name = (By.XPATH,"//input[@placeholder='地块名称']")
    land_certificate_no = (By.XPATH,"//input[@placeholder='土地证编号']")
    project_gain_type = (By.XPATH,"//span[@title='土地获取方式']/..//following-sibling::div//input")
    land_gain_date = (By.XPATH,"//span[@title='获取时间']/..//following-sibling::div//input")
    land_usage_type = (By.XPATH,"//span[@title='用地性质']/..//following-sibling::div//input")
    land_use_period_type = (By.XPATH,"//input[@placeholder='土地法定使用年限(年)']")
    land_remainder_period = (By.XPATH,"//input[@placeholder='土地剩余使用年限(年)']")
    address = (By.XPATH,"//textarea[@placeholder='地块所在四至范围']")
    province_code =  (By.XPATH,"//span[@title='地块所在省']/..//following-sibling::div//input")
    city_code = (By.XPATH,"//span[@title='地块所在市']/..//following-sibling::div//input")
    region_code = (By.XPATH,"//span[@title='地块所在区县']/..//following-sibling::div//input")
    land_address = (By.XPATH,"//textarea[@placeholder='地块地址']")
    delisting_unit = (By.XPATH,"//input[@placeholder='摘牌单位']")
    percent = (By.XPATH,"//input[@placeholder='我方权益比例(%)']")
    parcel_summary = (By.XPATH,"//input[@placeholder='地块汇总测试字段']")

    # 规划指标信息
    total_use_area = (By.XPATH,"//input[@placeholder='总用地面积(㎡)']")
    building_area = (By.XPATH,"//input[@placeholder='净用地面积(㎡)']")
    collection_of_land_area = (By.XPATH,"//input[@placeholder='代征用地面积(㎡)']")
    plot_ratio = (By.XPATH,"//input[@placeholder='容积率']")
    building_density = (By.XPATH,"//input[@placeholder='建筑密度(%)']")
    green_ratio = (By.XPATH,"//input[@placeholder='绿地率(%)']")
    limit_height = (By.XPATH,"//input[@placeholder='限高(m)']")

    #弹窗
    save_success = (By.XPATH,"//p[contains(text(),'保存成功')]")
    update_success = (By.XPATH,"//p[contains(text(),'更新成功')]")

    #获取发起审核按钮
    launch_btn = (By.XPATH,"//span[text()='{}']/../../parent::tr//button[@title='详情']//following-sibling::span//button[@title='发起审核']".format(landName))
    #获取发起审核的内容
    launch_locator =(By.XPATH,"//div[@class='el-message-box']//span[contains(text(),'发起审核')]")
    #点击确定
    determine_locator = (By.XPATH,"//div[@class='el-message-box']//span[contains(text(),'确定')]")

    wait_time = 20
    # def get(self):
    #     """访问登录页面"""
        # login_url = Setting.host + self.url
        # self.driver.get(login_url)

    def create_land(self, land_name, land_certificate_name, land_gain_date,
                    land_use_period_name, land_remainder_name, address_name,
                    land_address_name, delisting_unit_name, percent_name, parcel_summary_name,
                    total_use_area_name, building_area_name, collection_of_land_area_name, plot_ratio_name,
                    building_density_name, green_ratio_name, limit_height_name):

        #点击项目主数据
        self.js_to_bottom(self.xm_locator)

        #点击项目管理
        self.js_to_bottom(self.xmgl_locator)

        #点击地块
        self.js_to_bottom(self.dk_locator)

        #定位城市公司
        self.js_to_bottom(self.city_locator)

        #定位新增列表
        self.js_to_bottom(self.create_land_locator)

        #定位新增按钮
        self.js_to_bottom(self.btn_create_locator)

        #输入基本信息
        #1、用户输入地块名称
        self.user_input(self.land_name,land_name)

        # 2、用户输入土地证编号
        self.user_input(self.land_certificate_no, land_certificate_name)

        # 3、用户选择土地获取方式
        time.sleep(1)
        self.js_to_content(self.project_gain_type)
        self.js_to_bottom(self.project_gain_value)

        # 4、用户选择获取时间
        self.js_to_send_content(self.land_gain_date, land_gain_date)

        # 5、用户选择用地性质
        time.sleep(1)
        self.js_to_content(self.land_usage_type)
        self.js_to_bottom(self.land_usage_value)

        # 6、土地法定使用年限(年)
        self.user_input(self.land_use_period_type, land_use_period_name)

        # 7、土地剩余使用年限(年)
        self.user_input(self.land_remainder_period, land_remainder_name)

        # 8、地块所在四至范围
        self.user_input(self.address, address_name)

        # 9、地块所在省
        time.sleep(1)
        self.js_to_content(self.province_code)
        self.js_to_bottom(self.province_value)

        # 10、地块所在市
        time.sleep(1)
        self.js_to_content(self.city_code)
        self.js_to_bottom(self.city_value)

        # 11、地块所在区县
        time.sleep(1)
        self.js_to_content(self.region_code)
        self.js_to_bottom(self.region_value)

        # 12、地块地址
        self.user_input(self.land_address, land_address_name)

        # 13、摘牌单位
        self.user_input(self.delisting_unit, delisting_unit_name)

        # 13、我方权益比例(%)
        self.user_input(self.percent, percent_name)

        # 14、地块汇总测试字段
        self.user_input(self.parcel_summary, parcel_summary_name)

        # 规划指标信息
        # 1、总用地面积(㎡)
        self.user_input(self.total_use_area, total_use_area_name)

        # 2、净用地面积
        self.user_input(self.building_area, building_area_name)

        # 3、代征用地面积
        self.user_input(self.collection_of_land_area, collection_of_land_area_name)

        # 4、容积率
        self.user_input(self.plot_ratio, plot_ratio_name)

        # 5、建筑密度(%)
        self.user_input(self.building_density, building_density_name)

        # 6、绿地率(%)
        self.user_input(self.green_ratio, green_ratio_name)

        # 7、限高(m)
        self.user_input(self.limit_height, limit_height_name)


        #点击保存按钮
        self.js_to_bottom(self.btn_save_locator)
        time.sleep(3)





    def get_launch_btn(self):
        """发起审核"""
        time.sleep(3)
        self.js_to_bottom(self.launch_btn)

    def determine_btn(self):
        """点击确定"""
        time.sleep(3)
        self.js_to_bottom(self.determine_locator)
        time.sleep(3)


    def get_save_success_msg(self):
        """获取正确信息"""
        save_success_elem = self.wait_presence_element(self.save_success)
        return save_success_elem.text

    def get_launch_msg(self):
        """获取发起审核信息"""
        launch_elem = self.wait_presence_element(self.launch_locator)
        return launch_elem.text

    def get_update_success_msg(self):
        """获取更新成功信息"""
        update_success_elem = self.wait_presence_element(self.update_success)
        return update_success_elem.text








