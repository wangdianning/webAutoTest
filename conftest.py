"""conftest.py 文件名称是固定的。

统一存放 fixture 的地方。
"""
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions


@pytest.fixture(scope="session",autouse=True)
def get_browser():
    options = ChromeOptions()
    #设置浏览器路径
    options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    driver = webdriver.Chrome(options = options)
    # 最大化当前页
    driver.maximize_window()

    # 设置隐式等待
    wait_time = 20
    driver.implicitly_wait(wait_time)



    yield driver
    driver.quit()
