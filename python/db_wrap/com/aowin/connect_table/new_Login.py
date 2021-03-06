"""
    操作用户登录表，增加和查询功能
"""
from com.aowin.connect_library import DB_util
from com.aowin.modal import modal
import re


def insert(stu):
    """
        新增用户
    :param stu: 用户对象Tuple(全部列)
    :return: 返回新增条数
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO login (USERNAME, USERPWD, USERTEL, USERSEX) values (%s, %s, %s, %s)'
        cur.execute(sql, stu)
        conn.commit()
        return cur.rowcount
    finally:
        if conn:
            conn.close()


def select_data(stu):
    """
        查询用户信息
    :param stu: 用户对象Tuple(用户名列和用户信息列)
    :return: 返回查询到的信息
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'SELECT * FROM login WHERE USERNAME=%s AND USERPWD=%s'
        print(sql)
        cur.execute(sql, stu)
        return cur.fetchall()
    finally:
        if conn:
            conn.close()


def login(name, pwd):
    """
        用户登录功能
    :param name: 用户姓名
    :param pwd: 用户登录密码
    :return: 查询到的用户信息
    """
    conn = DB_util.getConn()
    try:
        cur = conn.cursor()
        sql = 'SELECT * FROM login WHERE USERNAME=%s AND USERPWD=%s'
        cur.execute(sql, (name, pwd))

        user = cur.fetchone()
        return user
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    # user = login('tom', '123')
    # print(user)

    # stu = ('jun', '222', '12345678900', '男')
    # n = insert(stu)
    # print(n)

    print(re.search('^[男|女|保密]$', '保密'))
    if not re.search('^[男|女]$', '保密'):
        print('error')
    else:
        print('ok')

