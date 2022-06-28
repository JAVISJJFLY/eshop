import unittest
from ddt import ddt, data, unpack
from ecshop.common import web_driver, data_interface
from ecshop.common import settings
import os

# 管理员登录信息
# 先获取管理员登录信息的路径，使用os模块拼接出文件的绝对路径
login_admin_path = os.path.join(
    settings.USE_PATH_DATA, 'login_admin_info.xlsx'
)
login_admin_info = data_interface.readfile(login_admin_path)
# print(login_admin_info)
# 增加会员信息
# 先获取会员注册信息的路径，使用os模块拼接出文件的绝对路径
add_member_path = os.path.join(
    settings.USE_PATH_DATA, 'add_member_info.xlsx'
)
add_member_info = data_interface.readfile(add_member_path)
# print(add_member_info)
# 会员登录信息
# 先获取会员登录信息的路径，使用os模块拼接出文件的绝对路径
login_member_path = os.path.join(
    settings.USE_PATH_DATA, 'login_member_info.csv'
)

login_member_info = data_interface.readfile(login_member_path)
# print(login_member_info)
# print(login_member_info)

# class Common:
#     # @classmethod
#     # def test_execute(cls):
#     #     # test_cases = TestEcShop()1
#     #     print(cls.__name__)
#     #     test_cases = unittest.defaultTestLoader.loadTestsFromTestCase(cls)
#     #     file_path = '../report/HtmlReport%s.html' % time.strftime('%Y%m%d %H%M%S')
#     #     runner = HTMLTestRunner(stream=open(file_path, 'wb'), title='测试报告', description='详细描述')
#     #     runner.run(test_cases)
#     pass


@ddt
class TestAdminLogin(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls) -> None:
    #     pass
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     pass
    #
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @data(*login_admin_info)
    @unpack
    def test_loginAdmin(self, user, pwd):
        self.web = web_driver.WebFunc()
        msg = self.web.login_admin(user, pwd)
        self.assertEqual('退出', msg, '登录失败')


@ddt
class TestAddMember(unittest.TestCase):
    #
    # @classmethod
    # def setUpClass(cls) -> None:
    #     pass
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     pass
    #
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @data(*add_member_info)
    @unpack
    def test_addMember(self, user, email, pwd, re_pwd, msg):
        self.web = web_driver.WebFunc()
        add_info = self.web.add_member(user, email, pwd, re_pwd, msg)
        self.assertIn(user, add_info, '添加失败')


@ddt
class TestMemberLogin(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls) -> None:
    #     pass
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     pass
    #
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @data(*login_member_info)
    @unpack
    def test_loginMember(self, user, pwd, msg):
        self.web = web_driver.WebFunc()
        login_info = self.web.login_member(user, pwd, msg)
        self.assertEqual(user, login_info, '登录失败')


# if __name__ == '__main__':
#     import time
#     from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
#     test3 = unittest.defaultTestLoader.loadTestsFromTestCase(TestAddMember)
#     # file_path = '../report/HtmlReport%s.html' % time.strftime('%Y%m%d %H%M%S')
#     # runner = HTMLTestRunner(stream=open(file_path, 'wb'), title='测试报告', description='详细描述')
#     # runner.run(test3)
#     runner = unittest.TextTestRunner()
#     runner.run(test3)