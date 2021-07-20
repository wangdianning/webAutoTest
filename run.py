import pytest

if __name__ == '__main__':
    # pytest.main(['-m  createLand and approveLand', '--reruns', '1'])
    pytest.main(["-v", "-s", ".","--alluredir=allure_report/"])