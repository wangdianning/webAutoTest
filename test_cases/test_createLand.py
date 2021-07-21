"""测试登录功能。

流程：
1，启动浏览器，打开url;
2, 定位用户名；
3， 输入用户名；
4， 定位密码；
5， 输入密码；
6， 定位登录按钮；
7， 点击登录按钮；
8，定位错误信息断言
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from config  import user_config
from data import create_land_data_success
from pages.land_page import LandPage
from test_cases.test_login import TestLogin

mdmUser = user_config.tzwh
mdmPwd = user_config.password
expected = user_config.tzwh_expected

@pytest.mark.run(order=1)
@pytest.mark.dependency()
class TestLand():
    @pytest.mark.parametrize('test_info', create_land_data_success)
    @pytest.mark.createLand
    def test_createLand(self, test_info, get_browser):
        #1、启动浏览器
        driver = get_browser
        # 先调用login函数登录
        TestLogin.test_login_success(driver,mdmUser=mdmUser,mdmPwd=mdmPwd,expected=expected)
        #获取预期结果
        save_expected = test_info['save_expected']
        launch_expected = test_info['launch_expected']
        update_expected = test_info['update_expected']
        #2、新增地块
        LandPage(driver).create_land(test_info["land_name"], test_info["land_certificate_name"],
                                     test_info["land_gain_date"], test_info["land_use_period_name"],
                                     test_info["land_remainder_name"], test_info["address_name"],
                                     test_info["land_address_name"], test_info["delisting_unit_name"],
                                     test_info["percent_name"], test_info["parcel_summary_name"],
                                     test_info["total_use_area_name"], test_info["building_area_name"],
                                     test_info["collection_of_land_area_name"], test_info["plot_ratio_name"],
                                     test_info["building_density_name"], test_info["green_ratio_name"],
                                     test_info["limit_height_name"])
        #3、新增地块断言
        save_success_msg = LandPage(driver).get_save_success_msg()
        try:
            assert save_success_msg == save_expected
        except AssertionError as e:
            raise e

        #4、发起审核
        LandPage(driver).get_launch_btn()

        #5、弹出发起审核的确认页面
        launch_success_msg = LandPage(driver).get_launch_msg()
        try:
            assert launch_success_msg == launch_expected
        except AssertionError as e:
            raise e

        #6、点击确认按钮
        LandPage(driver).determine_btn()

        #7、发起审核成功断言
        update_success_msg = LandPage(driver).get_update_success_msg()
        try:
            assert update_success_msg == update_expected
        except AssertionError as e:
            raise e

        #注销登录
        TestLogin.test_loginout_success(driver,mdmUser=mdmUser,expected="盟拓 【产品】V8主数据系统DEV")
