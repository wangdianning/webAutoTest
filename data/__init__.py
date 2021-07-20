"""测试数据的保存。

接口自动化自动化测试放在 Excel 当中，
web 自动化测试数据：1， py 文件当中，  2， Excel 当中

数据分组：把不同的测试用例方法需要用到的数据放入不同的组
分组的依据：是因为测试步骤不一样。

# 通过表单
# 2，接口当中也是有数据分组，不同的表单当中，

"""
from data.creatLand import creatLand

login_data_error = [
    {"mobile":"", "pwd":"", "expected": "请输入手机号"},
    {"mobile":"18675467432", "pwd":"", "expected": "输入密码"},
]


login_data_invalid = [
    {"mobile": "18745678943", "pwd": "12", "expected": "此账号没有经过授权，请联系管理员!"},
]


login_data_success = [
    {"mdmUser":"shaoy", "mdmPwd":"123456", "expected": "邵某某"},
]

#创建地块
landName = creatLand.random_land_name()
create_land_data_success = [
    {"land_name": "{}".format(landName), "land_certificate_name": "{}".format(landName),
     "land_gain_date": "2021-07-12", "land_use_period_name": "70",
     "land_remainder_name": "70", "address_name": "江苏省苏州市工业园区",
     "land_address_name": "江苏省苏州市工业园区", "delisting_unit_name": "江苏省苏州市工业园区",
     "percent_name": "50", "parcel_summary_name": "111", "total_use_area_name": "100000",
     "building_area_name": "50000", "collection_of_land_area_name": "50000",
     "plot_ratio_name": "5000", "building_density_name": "5000", "green_ratio_name": "5000",
     "limit_height_name": "22","save_expected": "保存成功","update_expected": "更新成功",
     "launch_expected":"发起审核"}
]

