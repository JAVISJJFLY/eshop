from test_case import test_case
from common import connect_SQL
import unittest
from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
import time


def login_admin():
    test1 = unittest.defaultTestLoader.loadTestsFromTestCase(test_case.TestAdminLogin)
    file_path = './report/HtmlReport%s.html' % time.strftime('%Y%m%d %H%M%S')
    runner = HTMLTestRunner(stream=open(file_path, 'wb'), title='测试报告', description='详细描述')
    runner.run(test1)


def add_member():
    suites = unittest.TestSuite()
    test2 = unittest.defaultTestLoader.loadTestsFromTestCase(test_case.TestAddMember)
    suites.addTests(test2)
    file_path = './report/HtmlReport%s.html' % time.strftime('%Y%m%d %H%M%S')
    runner = HTMLTestRunner(stream=open(file_path, 'wb'), title='测试报告', description='详细描述')
    runner.run(suites)


def login_member():
    test3 = unittest.defaultTestLoader.loadTestsFromTestCase(test_case.TestMemberLogin)
    file_path = './report/HtmlReport%s.html' % time.strftime('%Y%m%d %H%M%S')
    runner = HTMLTestRunner(stream=open(file_path, 'wb'), title='测试报告', description='详细描述')
    runner.run(test3)


def del_member():
    sql = connect_SQL.ConnectSQL()


# 字典值和函数的名称相对应,获取值就可以直接调用上面的函数功能
func_dic = {
    1: login_admin,
    2: add_member,
    3: login_member,
    4: del_member
}


def choose_func():
    while True:
        print("""
            请选择你要测试的功能：
            1.登录管理员
            2.增加会员
            3.登录用户
            4.删除会员信息
    
        """)

        choice = input("请输入你要测试的功能编号：").strip()
        if choice.isdigit():

            # 通过字典的键来获取函数的值 将输入的值转化为1，2，3，4的整数
            choice = int(choice)
            if choice in func_dic:
                func_dic[choice]()
            else:
                print("超出范围")
        elif choice.upper() == 'Q':
            break

        else:
            print("请输入数字")


choose_func()

