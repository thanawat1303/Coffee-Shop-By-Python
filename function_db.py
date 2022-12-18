import pymysql
import math
import datetime
import hashlib

def connect() :
    return pymysql.connect(host="127.0.0.1", database="coffee_shop_db", user="root", password="1660500178936Ff", charset="utf8")

con = connect()

class db_function() :
    def query_list_menu(collect) :
        ListMenu = {}
        try:
            cur = con.cursor()
            cur.execute(f'SELECT * FROM coffee_shop_db.{collect} ;')
            data = cur.fetchall()
            
            for i in data:
                ListMenu.update({ i[0] : {
                    'name_menu' : i[1] ,
                    'price_menu' : math.trunc(i[2]) ,
                    'img_menu' : i[3] , 
                    'type_menu' : i[4]
                }})
            return ListMenu
        
        except:
            print("มี Error")

    def addreceipt(List, listBD , price) :
        "List order , List Database , price sum"
        try:
            cur = con.cursor()
            idCon = hashlib.md5(str(datetime.datetime.now()).encode()).hexdigest()
            cur.execute(f'INSERT INTO contrat_submit (id_contrat_text, sum_menu, date_menu) VALUES ("{idCon}", "{int(price)}", "{str(datetime.datetime.now())}")')
            con.commit()
            idContart = cur.lastrowid
            for key , detail in List.items() :
                menuDB = listBD.get(key)
                priceSun = int(detail['qty']) * menuDB['price_menu']
                qty = detail['qty']
                try :
                    taste = detail['taste']
                except :
                    taste = 'หวานปกติ'
                cur = con.cursor()
                cur.execute(f'INSERT INTO order_list (id_contrat, idmenu_list, order_money, order_qty, order_taste) VALUES ("{int(idContart)}", "{key}", "{int(priceSun)}", "{int(qty)}", "{taste}")')
                con.commit() #ยืนยันการเปลี่ยนแปลงข้อมูล
            print("เพิ่มข้อมูลลงในตารางข้อมูลเรียบร้อยแล้ว")

            cur.close()  # สั่งปิดเคอร์เซอร์
        except :
            con.rollback() # ยกเลิกการทำคำสั่ง sql และดึงข้อมูลเดิมกลับมา
            print("ไม่สามารถเพิ่มข้อมูลลงในตารางข้อมูลได้")

#db = db_function
#menu = db.query_list_menu('menu_list')
#for i in menu :
    #print('กาแฟ' if i['type_menu'] == 1 else 'น้ำเย็น' if i['type_menu'] == 2 else 'ผลไม้' if i['type_menu'] == 3 else '')