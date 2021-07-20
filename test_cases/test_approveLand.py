import pytest
from config  import user_config
from pages.approve_page  import ApprovePage
from test_cases.test_login import TestLogin

mdmUser = user_config.tzsp
mdmPwd = user_config.password
expected = user_config.tzsp_expected


@pytest.mark.run(order=2)
@pytest.mark.dependency(depends=["test_createLand.py::TestLand::test_createLand"],
                        scope = 'session')
class TestApproveLand():
    @pytest.mark.approveLand
    def test_approveLand(self, get_browser):
        #1、启动浏览器
        driver = get_browser
        # 先调用login函数登录
        TestLogin.test_login_success(driver,mdmUser=mdmUser,mdmPwd=mdmPwd,expected=expected)
        # 获取预期结果
        approve_expected = "操作成功"
        #2、新增地块
        ApprovePage(driver).approve()
        #3、新增地块断言
        approve_success_msg = ApprovePage(driver).get_approve_success_msg()
        try:
            assert approve_success_msg == approve_expected
        except AssertionError as e:
            raise e

        # 注销登录
        TestLogin.test_loginout_success(driver, mdmUser=mdmUser, expected="盟拓 【产品】V8主数据系统DEV")
