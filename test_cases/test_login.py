import pytest
from data import login_data_error, login_data_invalid, login_data_success
from pages.login_page import LoginPage
from pages.loginout_page import LoginOutPage
from config  import user_config
from selenium import webdriver




class TestLogin():
    #登录
    @classmethod
    def test_login_success(self,driver,mdmUser,mdmPwd,expected):
        LoginPage(driver).login(mdmUser,mdmPwd)
        if mdmUser == user_config.tzwh:
            success_msg = LoginPage(driver).get_tzwh_success_msg()
            try:
                assert success_msg == expected
            except AssertionError as e:
                raise e
        if mdmUser == user_config.tzsp:
            success_msg = LoginPage(driver).get_tzsp_success_msg()
            try:
                assert success_msg == expected
            except AssertionError as e:
                raise e

    #注销
    @classmethod
    def test_loginout_success(self,driver,mdmUser,expected):
        #投资维护注销
        if mdmUser == user_config.tzwh:
            LoginOutPage(driver).tzwh_loginout()
            success_msg = LoginOutPage(driver).get_success_msg()
            try:
                assert success_msg == expected
            except AssertionError as e:
                raise e
        #投资审批注销
        if mdmUser == user_config.tzsp:
            LoginOutPage(driver).tzsp_loginout()
            success_msg = LoginOutPage(driver).get_success_msg()
            try:
                assert success_msg == expected
            except AssertionError as e:
                raise e