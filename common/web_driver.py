import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class WebFunc:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def __quit(self):
        self.driver.quit()

    def __login_admin(self, user, pwd):
        self.driver.get('http://localhost/ecshop/admin/privilege.php?act=login')
        self.driver.find_element(By.NAME, 'username').send_keys(user)  # 输入用户名
        self.driver.find_element(By.NAME, 'password').send_keys(pwd)  # 输入密码
        self.driver.find_element(By.CSS_SELECTOR, 'input[value="进入管理中心"]').click()  # 点击确定

    def login_admin(self, user, pwd):
        self.__login_admin(user, pwd)
        time.sleep(1)
        # 获取登录成功的信息:
        try:
            self.driver.switch_to.frame('header-frame')
            login_info = self.driver.find_element(By.CSS_SELECTOR, '#submenu-div > ul > li:nth-child(1) > a').text
            print(login_info)
            self.__quit()
            return login_info
        except:
            self.__quit()
            return ''

    def add_member(self, user, email, pwd, re_pwd, msg):
        # 添加会员需要先登录账号，调用login的方法，并传入正确的管理员登录信息
        self.__login_admin('admin', '12345678a')

        # 进入窗口点击会员
        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, 'frameset>#menu-frame'))
        self.driver.find_element(By.CSS_SELECTOR, '#menu-ul > li.collapse.lis.ico_7').click()
        self.driver.find_element(By.CSS_SELECTOR, '#menu-ul > li.explode.lis.ico2_7 > ul > li:nth-child(2) > a').click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, 'frameset>#main-frame'))

        # 输入会员注册信息
        self.driver.find_element(By.CSS_SELECTOR,
                                 "tbody > tr:nth-child(1) > td:nth-child(2) > input[type=text]").send_keys(user)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "tbody > tr:nth-child(2) > td:nth-child(2) > input[type=text]").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "tbody > tr:nth-child(3) > td:nth-child(2) > input[type=password]").send_keys(pwd)
        self.driver.find_element(By.CSS_SELECTOR,
                                 'tbody > tr:nth-child(4) > td:nth-child(2) > input[type=password]').send_keys(re_pwd)
        self.driver.find_element(By.CSS_SELECTOR, 'tbody > tr:nth-child(14) > td > input:nth-child(1)').click()
        time.sleep(1)
        print(f'\n {msg}--->', end='')  # print格式： --->msg  ./F(成功/失败) msg即子列表得最后一位元素如：密码为空,

        # 如果添加成功，获取返回值，失败则不获取，直接返回空字符串
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, 'frameset#frame-body > #main-frame'))
        add_info = self.driver.find_element(By.CSS_SELECTOR, "tbody > tr > td:nth-child(2)").text

        # 关闭窗口
        self.__quit()
        if add_info:
            return add_info

        # 若add_info不存在，返回空
        return ''

    def login_member(self, user, pwd, msg):
        self.driver.get('http://localhost/ecshop/user.php')
        self.driver.find_element(By.NAME, "username").send_keys(user)
        self.driver.find_element(By.NAME, "password").send_keys(pwd)
        self.driver.find_element(By.NAME, "submit").click()
        print(f'\n {msg}--->', end='')
        time.sleep(1)
        # 如果登录成功，获取返回值，失败则不获取，直接返回空字符串
        username = ''
        try:
            username = self.driver.find_element(By.CSS_SELECTOR, "#ECS_MEMBERZONE > a:nth-child(1)").text
            print(f'\n {msg}--->', end='')

        except:
            print("登录会员失败")

        finally:
            # 关闭网页
            self.__quit()
            # 返回查询到的信息
            return username


if __name__ == '__main__':

    web = WebFunc()
    web.login_admin('admin', '12345678a')