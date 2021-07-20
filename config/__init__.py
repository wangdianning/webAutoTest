"""配置文件

ini, yaml, py文件， constant.py
"""
import os

class Setting:
    # host 地址
    host = 'http://172.18.50.87:37080'

    # login_url
    login_url = '/Index/login.html'


    # root_path 项目的根目录
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # img_path, 截图目录 img
    img_path = os.path.join(root_path, 'img')
    if not os.path.exists(img_path):
        os.mkdir(img_path)
