import pymysql
# from pymysql.constants import CLIENT

class ConnectSQL:
    conn = pymysql.connect(
        host="127.0.0.1",  # ip
        port=3306,  # 端口号
        user='root',  # 账户名
        password='',  # 密码
        db='ecshop',  # 库名
        # client_flag=CLIENT.MULTI_STATEMENTS
    )
    cur = conn.cursor()

    def query(self,sql):
        self.cur.execute(sql)
        query_info = self.cur.fetchall()
        print(query_info)
        return query_info

    def modify(self,sql):
        self.cur.execute(sql)
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()

    # def delInfo(self, sql):
    #     self.query('select * from ')
    #     self.cur.execute(sql)
    #     self.conn.commit()

