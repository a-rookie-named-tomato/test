from fastapi import APIRouter
from fastapi import Form
import psycopg2
from fastapi import Request
from pydantic import BaseModel
from fastapi import File,UploadFile
from fastapi import WebSocket
import asyncio
from fastapi.responses import JSONResponse





fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

app_request = APIRouter(
    tags=['客户端模块'],
)

class UserL(BaseModel):
    username: str
    password: str

@app_request.post('/login')
def login(user: UserL):
    with psycopg2.connect("dbname=user user=tomoto password=040720") as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM login WHERE username=%s AND password=%s", (user.username, user.password))
            result = cursor.fetchall()
            if result:
                # Return a success response with the username
                return {"code": 200, "message": "登录成功", "username": user.username}
            else:
                # Return an error response with a message
                return {"code": 400, "message": "账号或密码错误"}
            

@app_request.post("/register")
async def register(user:UserL):
    try:
        with psycopg2.connect("dbname=user user=tomoto password=040720") as conn:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO login VALUES (%s, %s)", (user.username, user.password))
                conn.commit()
                return {"code": 200, "message": "注册成功", "username": user.username}
    except Exception as e:
        return {"code": 500, "message": f"注册失败：{str(e)}"}



# WebSocket 路由
import asyncio
import websockets
@app_request.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    conn = psycopg2.connect("dbname=user user=tomoto password=040720")
    cursor = conn.cursor()
    try:
        while True:
            cursor.execute("SELECT * FROM car")
            database_data = cursor.fetchall()
            await websocket.send_json(database_data)
            await asyncio.sleep(1)  # 60s
    except websockets.exceptions.ConnectionClosedOK:
        print("Connection closed by client.")
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()





class Car(BaseModel):
    id: str
    model: str
    make: str
    color:str
    year:str
    price:float
    owner_name:str
    phone:str
    s_id:str
    sale_time:str
    sale_price:str





import logging
logging.basicConfig(level=logging.DEBUG)
    
@app_request.post('/add')
async def addcar(car: Car):
    try:
        logging.debug(f"Received car data: {car}")
        conn = psycopg2.connect("dbname=user user=tomoto password=040720")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO car (id, model, make, color, year, price, owner_name, phone, \"4s_id\",sale_time,sale_price,sold) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s)",
                    (car.id, car.model, car.make, car.color, car.year, car.price, car.owner_name, car.phone, car.s_id,car.sale_time,car.sale_price,'0'))
        conn.commit()
        logging.info(f"Car data for ID {car.id} added successfully")
        return {'Car': car.id}
    except Exception as e:
        logging.error(f"Error adding car data: {str(e)}")
        raise 
    finally:
        if conn:
            conn.close()

class CarEdit(BaseModel):
    id: str
    owner_name: str
    phone: str
    sale_time: str
    sale_price: str

def update_car(id, owner_name, phone, sale_time, sale_price):
    conn = psycopg2.connect("dbname=user user=tomoto password=040720")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM car WHERE id = %s AND sold = '0'", (id,))
    result = cursor.fetchall()
    if result:
        cursor.execute("UPDATE car SET owner_name = %s, phone = %s, sale_time = %s, sale_price = %s, sold = '1' WHERE id = %s",
                       (owner_name, phone, sale_time, sale_price, id))
        conn.commit()
        return None  # Return None when there is no error
    else:
        return {"code": 400, "message": "Invalid car ID"}

@app_request.put('/edit')
async def car_change(car: CarEdit):
    try:
        result = update_car(car.id, car.owner_name, car.phone, car.sale_time, car.sale_price)
        if result:
            return result  #ERROR
        else:
            return {'message': f'Car information for ID {car.id} has been updated'}
    except Exception as e:
        return {'code': 500, 'message': str(e)}
    


class Car_id(BaseModel):
    id:str

def delete_car(car_id):
    conn = psycopg2.connect("dbname=user user=tomoto password=040720")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM car WHERE id = %s ", (car_id,))
    conn.commit()

@app_request.delete('/delete')
async def car_delete(car: Car_id):
    try:
        await delete_car(car.id)
    except Exception as e:
        print(e)
        return e
    finally:
        return {'message': car.id + '车辆已删除'} 
    




# @app_request.post('/select')
# def select_car(
#           id: str = Form()
# ):
#     conn = psycopg2.connect("dbname=user user=tomoto password=040720")
#     cursor = conn.cursor()
#     model=id
#     cursor.execute("SELECT * FROM car WHERE id=%s OR model LIKE %s", (id, '%' + model + '%'))
#     cars = cursor.fetchall() 
#     if cars:
#         car_list = []
#         for car in cars:

#             car_data = {
#                 "id": car[0],
#                 "model": car[1],  
#                 "make": car[2],
#                 "color": car[3],
#                 "year": car[4],
#                 "price": car[5],
#                 "owner_name": car[6],
#                 "phone": car[7],
#                 "shop_id": car[8],
#                 "sale_time": car[9],
#                 "sale_price": car[10],
#                 "sold": car[11],
#             }
#             car_list.append(car_data)
#         return JSONResponse(content=car_list)
#     else:
#         return {"message": "未找到车辆"}

import base64
@app_request.post('/select')
def select_car(id: str = Form()):
    conn = psycopg2.connect("dbname=user user=tomoto password=040720")
    cursor = conn.cursor()

    try:
        model = id
        cursor.execute("SELECT * FROM car WHERE id=%s OR model LIKE %s", (id, '%' + model + '%'))
        cars = cursor.fetchall()

        if cars:
            car_list = []
            for car in cars:
                car_id = car[0]
                image_data = get_image_data_from_database(conn, car_id)
                # print(image_data)  

                car_data = {
                    "id": car_id,
                    "model": car[1],
                    "make": car[2],
                    "color": car[3],
                    "year": car[4],
                    "price": car[5],
                    "owner_name": car[6],
                    "phone": car[7],
                    "shop_id": car[8],
                    "sale_time": car[9],
                    "sale_price": car[10],
                    "sold": car[11],
                    "image_data": image_data,
                }
                car_list.append(car_data)

            return JSONResponse(content=car_list)
        else:
            return {"message": "未找到车辆"}
    finally:
        cursor.close()
        conn.close()

def get_image_data_from_database(conn, car_id):
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT picture FROM images WHERE id=%s", (car_id,))
        image_data = cursor.fetchone()
        return base64.b64encode(image_data[0]).decode('utf-8') if image_data else None
    finally:
        cursor.close()







from fastapi import HTTPException
from psycopg2 import sql
# 连接数据库
try:
    conn = psycopg2.connect("postgresql://tomoto:040720@localhost/user")
except psycopg2.Error as e:
    # 处理连接错误，比如打印错误信息或者抛出适当的异常
    print("Unable to connect to the database. Error:", e)
    raise


def save_image_to_database(image_id: str, content: bytes):
    # 使用上下文管理器确保正确处理连接
    with conn.cursor() as cur:
        query = sql.SQL("INSERT INTO images (id, picture) VALUES ({}, {})").format(
            sql.Literal(image_id),
            sql.Literal(content),
        )
        cur.execute(query)
    conn.commit()

def is_image_file(filename: str) -> bool:
    valid_extensions = {".jpg", ".jpeg", ".png", ".gif"}
    return any(filename.lower().endswith(ext) for ext in valid_extensions)

@app_request.post('/upload')
async def upload_image(id: str=Form(), file: UploadFile = File(...)):
    if not is_image_file(file.filename):
        raise HTTPException(status_code=400, detail="只能上传图片文件")
    # 将文件内容读取为 bytes
    content = file.file.read()
    save_image_to_database(id, content)
    return {"id": id, "filename": file.filename}





# from fastapi import HTTPException, FastAPI, Form, File, UploadFile
# from fastapi.responses import JSONResponse
# from psycopg2 import sql
# import psycopg2


# # 连接数据库
# try:
#     conn = psycopg2.connect("postgresql://tomoto:040720@localhost/user")
# except psycopg2.Error as e:
#     # 处理连接错误，比如打印错误信息或者抛出适当的异常
#     print("Unable to connect to the database. Error:", e)
#     raise

# def save_image_to_database(image_id: str, content: bytes):
#     # 使用上下文管理器确保正确处理连接
#     with conn.cursor() as cur:
#         query = sql.SQL("INSERT INTO images (id, picture) VALUES ({}, {})").format(
#             sql.Literal(image_id),
#             sql.Literal(content),
#         )
#         cur.execute(query)
#     conn.commit()

# def is_image_file(filename: str) -> bool:
#     valid_extensions = {".jpg", ".jpeg", ".png", ".gif"}
#     return any(filename.lower().endswith(ext) for ext in valid_extensions)

# @app_request.post('/upload')
# async def upload_image(id: str = Form(...), file: UploadFile = File(...)):
#     if not is_image_file(file.filename):
#         raise HTTPException(status_code=400, detail="只能上传图片文件")

#     # 将文件内容读取为 bytes
#     content = file.file.read()

#     # 将文件内容存储到数据库
#     save_image_to_database(id, content)

#     # 返回包含文件名的响应
#     response_data = {"id": id, "filename": file.filename}
#     return JSONResponse(content=response_data, status_code=200)


