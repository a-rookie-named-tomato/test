import psycopg2
from psycopg2 import OperationalError

if __name__ == '__main__':
    username = input()
    try:
        conn = psycopg2.connect("dbname=user user=tomoto password=040720")
        print("数据库连接成功！")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM login WHERE password = %s", (username,))
        result = cursor.fetchall()
        if result:
            print("登录成功")
        else:
            print("账号或密码错误")
        cursor.close()
        conn.close()
    except OperationalError as e:
        print(f"数据库连接失败: {e}")


# import psycopg2
# from psycopg2 import OperationalError

# if __name__ == '__main__':
#     try:
#         conn = psycopg2.connect("dbname=user user=tomoto password=040720")
#         print("数据库连接成功！")
#         cursor = conn.cursor()
#         cursor.execute("SELECT username, password FROM login")
#         results = cursor.fetchall()
#         for result in results:
#             print(f"账号: {result[1]}, 密码: {result[1]}")
#         cursor.close()
#         conn.close()
#     except OperationalError as e:
#         print(f"数据库连接失败: {e}")
