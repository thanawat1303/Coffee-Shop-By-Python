from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import function_db
import confirm 
from threading import Timer

db = function_db.db_function
listMenuDB = db.query_list_menu('menu_list')
ListMenuOrder = {}
_translate = QtCore.QCoreApplication.translate

def addPageConfirm(self , page_order, menu_order , List_all , listMenuDB , price) :
    menu_order.removeTab(0)
    put = {}
    for key , val in List_all.items() :
        print(val)
        try :
            x = val['qty']
            put.update({key : val})
        except :
            print(key)
    # print(page_order.children()[i])
    print(f": {page_order} : {menu_order} :")
    confirm.Ui_MainWindow.setupUi(self , menu_order , put , listMenuDB)
    confirm.Ui_MainWindow.retranslateUi(self , menu_order , put , listMenuDB , price)
class create() :
    def listMenu(self , typeMenu , Box , id_vertical , id_vertical_order , search) :
        for i in reversed(range(id_vertical.count())): 
            id_vertical.itemAt(i).widget().deleteLater()
        "object program , ประเภทเมนู , self.ตามด้วยชื่อ object ที่จะเอาลิสไปใส่"
        qtyMenu = 0
        for key , menu in listMenuDB.items() :
            chk = True
            if search == "" or search == "444"  or search == "0x048":
                chk = True
            elif search in menu['name_menu'] :
                chk = True
            else :
                chk = False
            if int(menu['type_menu']) == int(typeMenu) and chk :
                qtyMenu += 1
                self.listcoffee = QtWidgets.QFrame(Box) #รับไอดี ของ object ที่เป็น box แต่ละ box
                self.listcoffee.setEnabled(True)
                self.listcoffee.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.listcoffee.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.listcoffee.setFrameShadow(QtWidgets.QFrame.Raised)
                self.listcoffee.setObjectName("listcoffee")
                self.name = QtWidgets.QLabel(self.listcoffee)
                self.name.setGeometry(QtCore.QRect(180, 8, 501, 51))
                font = QtGui.QFont()
                font.setFamily("DSN Single")
                font.setPointSize(21)
                font.setBold(True)
                font.setWeight(75)
                self.name.setFont(font)
                self.name.setObjectName("name")
                self.textBath = QtWidgets.QLabel(self.listcoffee)
                self.textBath.setGeometry(QtCore.QRect(220, 120, 91, 36))
                font = QtGui.QFont()
                font.setFamily("DSN PatPong Extend")
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.textBath.setFont(font)
                self.textBath.setFrameShape(QtWidgets.QFrame.VLine)
                self.textBath.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.textBath.setObjectName("textBath")
                self.numOrder = QtWidgets.QFrame(self.listcoffee)
                self.numOrder.setGeometry(QtCore.QRect(680, 10, 151, 51))
                self.numOrder.setStyleSheet("QPushButton {\n"
            "    border-radius:16px;\n"
            "    border:0 solid;\n"
            "    color:white;\n"
            "    padding-bottom:3px;\n"
            "    background-color:#8b5234;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color:;\n"
            "    background-color: rgb(188, 109, 70);\n"
            "}")
                self.numOrder.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.numOrder.setFrameShadow(QtWidgets.QFrame.Raised)
                self.numOrder.setObjectName("numOrder")
                self.positive = QtWidgets.QPushButton(self.numOrder)
                self.positive.setGeometry(QtCore.QRect(110, 10, 33, 33))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.positive.setFont(font)
                self.positive.setStyleSheet("*:pressed{\n"
            "    padding-left:2px;\n"
            "}")
                self.positive.setObjectName("positive")
                self.negative = QtWidgets.QPushButton(self.numOrder)
                self.negative.setGeometry(QtCore.QRect(10, 10, 33, 33))
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.negative.setFont(font)
                self.negative.setStyleSheet("* :pressed{\n"
            "    padding-right:2px;\n"
            "}")
                self.negative.setObjectName("negative")
                self.num = QtWidgets.QLineEdit(self.numOrder)
                self.num.setGeometry(QtCore.QRect(42, 10, 71, 33))
                font = QtGui.QFont()
                font.setPointSize(15)
                font.setBold(True)
                font.setWeight(75)
                self.num.setFont(font)
                self.num.setStyleSheet("* {\n"
            "    \n"
            "    background-color: rgba(255, 255, 255, 0);\n"
            "    border:0;\n"
            "}")
                self.num.setAlignment(QtCore.Qt.AlignCenter)
                self.num.setObjectName("num")
                self.iconBath = QtWidgets.QLabel(self.listcoffee)
                self.iconBath.setGeometry(QtCore.QRect(180, 120, 35, 35))
                font = QtGui.QFont()
                font.setPointSize(5)
                self.iconBath.setFont(font)
                self.iconBath.setText("")
                self.iconBath.setPixmap(QtGui.QPixmap("assets/img_shop/Bath.png"))
                self.iconBath.setScaledContents(True)
                self.iconBath.setAlignment(QtCore.Qt.AlignCenter)
                self.iconBath.setObjectName("iconBath")
                self.radioGroup = QtWidgets.QFrame(self.listcoffee)
                self.radioGroup.setGeometry(QtCore.QRect(180, 65, 341, 41))
                self.radioGroup.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.radioGroup.setFrameShadow(QtWidgets.QFrame.Raised)
                self.radioGroup.setObjectName("radioGroup")
                self.normal = QtWidgets.QRadioButton(self.radioGroup)
                self.normal.setGeometry(QtCore.QRect(112, 10, 95, 20))
                font = QtGui.QFont()
                font.setFamily("DSN AnuRak")
                font.setPointSize(14)
                self.normal.setFont(font)
                self.normal.setObjectName("normal")
                self.max = QtWidgets.QRadioButton(self.radioGroup)
                self.max.setGeometry(QtCore.QRect(220, 10, 95, 20))
                font = QtGui.QFont()
                font.setFamily("DSN AnuRak")
                font.setPointSize(14)
                self.max.setFont(font)
                self.max.setObjectName("max")
                self.min = QtWidgets.QRadioButton(self.radioGroup)
                self.min.setGeometry(QtCore.QRect(4, 10, 95, 20))
                font = QtGui.QFont()
                font.setFamily("DSN AnuRak")
                font.setPointSize(14)
                self.min.setFont(font)
                self.min.setObjectName("min")
                self.img = QtWidgets.QLabel(self.listcoffee)
                self.img.setGeometry(QtCore.QRect(40, 20, 100, 133))
                self.img.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
            "border:1.5 solid #8b5234;\n"
            "border-radius:0px;")
                self.img.setInputMethodHints(QtCore.Qt.ImhNone)

                pix = QtGui.QPixmap()
                if pix.loadFromData(menu['img_menu']) :
                    self.img.setPixmap(pix)
                self.img.setScaledContents(True)
                self.img.setObjectName("img")
                id_vertical.addWidget(self.listcoffee)

                #set text list menu
                self.listcoffee.setAccessibleName(_translate("MainWindow", "listcoffee"))
                self.name.setText(_translate("MainWindow", menu['name_menu']))
                self.textBath.setText(_translate("MainWindow", "50"))
                self.positive.setText(_translate("MainWindow", "+"))
                self.negative.setText(_translate("MainWindow", "-"))
                if search == "444" :
                    print(menu['name_menu'])
                    try :
                        self.num.setText(_translate("MainWindow", str(ListMenuOrder.get(key)['qty'])))
                    except :
                        self.num.setText(_translate("MainWindow", "0"))
                else :
                    self.num.setText(_translate("MainWindow", "0"))
                self.normal.setText(_translate("MainWindow", "หวานปกติ"))
                self.max.setText(_translate("MainWindow", "หวานมาก"))
                self.min.setText(_translate("MainWindow", "หวานน้อย"))

                def changeQtyP(id , idMenu) :
                    try :
                        ListMenuOrder[idMenu] 
                    except : 
                        ListMenuOrder.update({idMenu : {}})

                    if int(id.text()) < 99 :
                        id.setText(_translate("MainWindow", f"{int(id.text()) + 1}"))
                        ListMenuOrder[idMenu].update({'qty' : int(id.text())})
                        addOrder(self , self.list_cf_order , id_vertical_order , id , idMenu)
                        print(ListMenuOrder)

                def changeQtyN(id , idMenu) :
                    try :
                        ListMenuOrder[idMenu] 
                    except : 
                        ListMenuOrder.update({idMenu : {}})
                    
                    if int(id.text()) > 0 :
                        id.setText(_translate("MainWindow", f"{int(id.text()) - 1}"))
                        ListMenuOrder[idMenu].update({'qty' : int(id.text())})
                        if int(id.text()) == 0 :
                            ListMenuOrder.pop(idMenu)
                        addOrder(self , self.list_cf_order , id_vertical_order , id , idMenu)
                        print(ListMenuOrder)

                def changeTaste(id , idMenu) :
                    try :
                        ListMenuOrder[idMenu] 
                    except : 
                        ListMenuOrder.update({idMenu : {}})
                    ListMenuOrder[idMenu].update({'taste' : id.text()})
                    addOrder(self , self.list_cf_order , id_vertical_order , id , idMenu)

                self.positive.clicked.connect(partial(changeQtyP, self.num , key))
                self.negative.clicked.connect(partial(changeQtyN, self.num , key))

                self.max.toggled.connect(partial(changeTaste, self.max , key))
                self.min.toggled.connect(partial(changeTaste, self.min , key))
                self.normal.toggled.connect(partial(changeTaste, self.normal , key))

        if search != '0x048' :
            def autoclick() :
                self.BtMenu.click()
            
            st = Timer(0.1 , autoclick).start()
                
        Box.setGeometry(QtCore.QRect(0, 0, 880, 193 * qtyMenu))
    
    def initOrderPage(self , menu_order , search) :
        self.page_order = QtWidgets.QWidget()
        self.page_order.setObjectName("page_order")
        self.listOrder = QtWidgets.QScrollArea(self.page_order)
        self.listOrder.setGeometry(QtCore.QRect(20, 70, 882, 440))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listOrder.sizePolicy().hasHeightForWidth())
        self.listOrder.setSizePolicy(sizePolicy)
        self.listOrder.setMinimumSize(QtCore.QSize(882, 440))
        self.listOrder.setMaximumSize(QtCore.QSize(882, 440))
        self.listOrder.setStyleSheet("background-color: #8b5234;")
        self.listOrder.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listOrder.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listOrder.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignCenter)
        self.listOrder.setObjectName("listOrder")
        self.list_cf_order = QtWidgets.QWidget()
        self.list_cf_order.setGeometry(QtCore.QRect(0, 0, 880, 193))
        self.list_cf_order.setMinimumSize(QtCore.QSize(0, 193))
        self.list_cf_order.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:0px;\n"
"    border-radius:32;\n"
"}")
        self.list_cf_order.setObjectName("list_cf_order")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.list_cf_order)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        #self.verticalLayout_10.count
        #---------------------------------Loop Get List Order------------------------------------------
        #----------------------------------------
        #order list
        self.name_order_list = QtWidgets.QLabel(self.list_cf_order)
        self.name_order_list.setGeometry(QtCore.QRect(20, 20, 531, 33))
        self.name_order_list.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignCenter)
        self.name_order_list.setStyleSheet("*{" "background-color:transparent; color:white;}")
        font = QtGui.QFont()
        font.setFamily("DSN Single")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.name_order_list.setFont(font)
        self.name_order_list.setObjectName("name_order_list")
        self.verticalLayout_10.addWidget(self.name_order_list)
        #----------------------------------------
        self.listOrder.setWidget(self.list_cf_order)
        self.headerOrder = QtWidgets.QFrame(self.page_order)
        self.headerOrder.setGeometry(QtCore.QRect(20, 20, 881, 51))
        self.headerOrder.setStyleSheet("* {\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.headerOrder.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerOrder.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerOrder.setObjectName("headerOrder")
        self.TextHeaderOrder = QtWidgets.QLabel(self.headerOrder)
        self.TextHeaderOrder.setGeometry(QtCore.QRect(30, 0, 851, 51))
        font = QtGui.QFont()
        font.setFamily("DSN PreeCha")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.TextHeaderOrder.setFont(font)
        self.TextHeaderOrder.setObjectName("TextHeaderOrder")
        self.btPageOrder = QtWidgets.QFrame(self.page_order)
        self.btPageOrder.setGeometry(QtCore.QRect(20, 510, 881, 51))
        self.btPageOrder.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btPageOrder.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btPageOrder.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btPageOrder.setObjectName("btPageOrder")
        menu_order.addTab(self.page_order, "")
        
        menu_order.setTabText(menu_order.indexOf(self.page_order), _translate("MainWindow", "เช็ครายการอาหาร"))
        self.TextHeaderOrder.setText(_translate("MainWindow", ""))
        self.name_order_list.setText(_translate("MainWindow", "ไม่พบเมนู"))

        if (search == "" or search == "0x048") and search != "444" :
            ListMenuOrder.clear()
        else :
            genarateSearch(self , self.verticalLayout_10 , self.list_cf_order)

        create.listMenu(self , 1 , self.list , self.verticalLayout , self.verticalLayout_10 , search)
        create.listMenu(self , 2 , self.menu_ice , self.verticalLayout_2 , self.verticalLayout_10 , search)
        create.listMenu(self , 3 , self.menu_fluit , self.verticalLayout_3 , self.verticalLayout_10 , search)
    
def genarateSearch(self , id_vertical_order , Box) :
    price = 0
    for i in reversed(range(id_vertical_order.count())): 
        id_vertical_order.itemAt(i).widget().deleteLater()
    print(f"count {self.btPageOrder.children().count}")
    #if self.btPageOrder.children().count > 0 :
        #   print(f"count {self.btPageOrder.children().count}")
        #  self.btPageOrder.children()[0].deleteLater()
    print(self.btPageOrder.children())
    if len(ListMenuOrder) != 0 : 
        num = 0
        listName = {}
        for key , detail in ListMenuOrder.items() :
            if 'qty' in detail :
                menuDB = listMenuDB.get(key)
                self.cf_order = QtWidgets.QFrame(Box)
                self.cf_order.setEnabled(True)
                self.cf_order.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.cf_order.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.cf_order.setFrameShadow(QtWidgets.QFrame.Raised)
                self.cf_order.setObjectName("cf_order")
                self.name_order_list = QtWidgets.QLabel(self.cf_order)
                self.name_order_list.setGeometry(QtCore.QRect(20, 20, 531, 33))
                font = QtGui.QFont()
                font.setFamily("DSN Single")
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.name_order_list.setFont(font)
                self.name_order_list.setObjectName("name_order_list")
                self.textBath_order = QtWidgets.QLabel(self.cf_order)
                self.textBath_order.setGeometry(QtCore.QRect(452, 130, 351, 35))
                font = QtGui.QFont()
                font.setFamily("DSN PatPong Extend")
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.textBath_order.setFont(font)
                self.textBath_order.setFrameShape(QtWidgets.QFrame.VLine)
                self.textBath_order.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.textBath_order.setObjectName("textBath_order")
                self.buttomOrder = QtWidgets.QFrame(self.cf_order)
                self.buttomOrder.setGeometry(QtCore.QRect(190, 115, 111, 51))
                self.buttomOrder.setStyleSheet("QPushButton {\n"
            "    border-radius:12px;\n"
            "    border:0 solid;\n"
            "    color:white;\n"
            "}\n"
            "\n"
            "QPushButton:selected {\n"
            "    border:0 solid;\n"
            "}")
                self.buttomOrder.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.buttomOrder.setFrameShadow(QtWidgets.QFrame.Raised)
                self.buttomOrder.setObjectName("buttomOrder")
                self.cancel_list_order = QtWidgets.QPushButton(self.buttomOrder)
                self.cancel_list_order.setGeometry(QtCore.QRect(10, 11, 91, 31))
                font = QtGui.QFont()
                font.setFamily("DSN Katreeya")
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.cancel_list_order.setFont(font)
                self.cancel_list_order.setStyleSheet("* {\n"
            "    background-color: rgb(255, 0, 0);\n"
            "    \n"
            "}\n"
            "\n"
            "* :pressed{\n"
            "    border-left:1px solid red;\n"
            "    border-bottom:1px solid red;\n"
            "    background-color: qlineargradient(spread:reflect, x1:0.5, y1:0.534091, x2:0.142, y2:0.0284091, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 140, 140, 255))\n"
            "}")
                self.cancel_list_order.setObjectName("cancel_list_order")
                self.numOrder_2 = QtWidgets.QFrame(self.cf_order)
                self.numOrder_2.setGeometry(QtCore.QRect(40, 115, 151, 51))
                self.numOrder_2.setStyleSheet("QPushButton {\n"
            "    border-radius:16px;\n"
            "    border:0 solid;\n"
            "    color:white;\n"
            "    padding-bottom:3px;\n"
            "    background-color:#8b5234;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color:;\n"
            "    background-color: rgb(188, 109, 70);\n"
            "}")
                self.numOrder_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.numOrder_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.numOrder_2.setObjectName("numOrder_2")
                self.qty_order = QtWidgets.QLabel(self.numOrder_2)
                self.qty_order.setGeometry(QtCore.QRect(2, 12, 150, 33))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.qty_order.setFont(font)
                self.qty_order.setStyleSheet("* {\n"
            "    \n"
            "    background-color: rgba(255, 255, 255, 0);\n"
            "    border:0;\n"
            "}")
                self.qty_order.setAlignment(QtCore.Qt.AlignLeft)
                self.qty_order.setObjectName("qty_order")
                self.iconBathOrder = QtWidgets.QLabel(self.cf_order)
                self.iconBathOrder.setGeometry(QtCore.QRect(810, 128, 35, 35))
                font = QtGui.QFont()
                font.setPointSize(5)
                self.iconBathOrder.setFont(font)
                self.iconBathOrder.setText("")
                self.iconBathOrder.setPixmap(QtGui.QPixmap("assets/img_shop/Bath.png"))
                self.iconBathOrder.setScaledContents(True)
                self.iconBathOrder.setAlignment(QtCore.Qt.AlignCenter)
                self.iconBathOrder.setObjectName("iconBathOrder")
                self.imgOrder = QtWidgets.QLabel(self.cf_order)
                self.imgOrder.setGeometry(QtCore.QRect(740, 10, 80, 106))
                self.imgOrder.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
            "border:1.5 solid #8b5234;\n"
            "border-radius:0px;")
                self.imgOrder.setInputMethodHints(QtCore.Qt.ImhNone)

                pix = QtGui.QPixmap()
                if pix.loadFromData(menuDB['img_menu']) :
                    self.imgOrder.setPixmap(pix)

                self.imgOrder.setScaledContents(True)
                self.imgOrder.setObjectName("imgOrder")
                self.type_order = QtWidgets.QLabel(self.cf_order)
                self.type_order.setGeometry(QtCore.QRect(50, 58, 311, 61))
                font = QtGui.QFont()
                font.setFamily("DSN Single")
                font.setPointSize(18)
                self.type_order.setFont(font)
                self.type_order.setObjectName("type_order")
                id_vertical_order.addWidget(self.cf_order)

                try :
                    taste = detail['taste']
                except :
                    taste = 'หวานปกติ'
                num += 1
                price += int(detail['qty']) * menuDB['price_menu']
                def removeButton(boxDelete , size , key , name) :
                    ListMenuOrder.pop(key)
                    listName.pop(name)
                    num = len(ListMenuOrder)
                    boxDelete.deleteLater()
                    ListNum.get(key)['idText'].setText(_translate("MainWindow", "0"))
                    ListNum.pop(key)
                    no = 1
                    for key , val in listName.items() :
                        key.setText(_translate("MainWindow", f"{no}. {val['name']}"))
                        no += 1
                    if len(ListMenuOrder) == 0 :
                        for x in self.btPageOrder.children() :
                            x.deleteLater()
                    self.TextHeaderOrder.setText(_translate("MainWindow", f"รายการทั้งหมด {num} รายการ" if num > 0 else 'กรุณาเลือกเครื่องดื่ม'))
                    size.setGeometry(QtCore.QRect(0, 0, 880, 193 * num))
                
                self.cancel_list_order.clicked.connect(partial(removeButton , self.cf_order , self.list_cf_order , key , self.name_order_list))

                listName.update({self.name_order_list : {'name' : menuDB['name_menu']}})

                self.cf_order.setAccessibleName(_translate("MainWindow", "listcoffee"))
                self.name_order_list.setText(_translate("MainWindow", f"{num}. {menuDB['name_menu']}"))
                self.textBath_order.setText(_translate("MainWindow", f"ยอดรวม {int(detail['qty']) * menuDB['price_menu']}"))
                self.cancel_list_order.setText(_translate("MainWindow", "Cancel"))
                self.qty_order.setText(_translate("MainWindow", f"จำนวน {detail['qty']} แก้ว"))
                self.type_order.setText(_translate("MainWindow", taste))
        self.TextHeaderOrder.setText(_translate("MainWindow", f"รายการทั้งหมด {num} รายการ" if num > 0 else 'กรุณาเลือกเครื่องดื่ม'))
        if num > 0 :
            self.confirmOrder = QtWidgets.QPushButton(self.btPageOrder)
            self.confirmOrder.setGeometry(QtCore.QRect(365, 5, 150, 39))
            font = QtGui.QFont()
            font.setFamily("DSN SukSaWat")
            font.setPointSize(20)
            self.confirmOrder.setFont(font)
            self.confirmOrder.setStyleSheet("* {\n"
    "    border:1 solid white;\n"
    "    border-radius:19px;\n"
    "    color:white;\n"
    "    background-color: #8b5234;\n"
    "    padding-top:4;\n"
    "}\n"
    "\n"
    "* :pressed{\n"
    "    background-color: qlineargradient(spread:reflect, x1:0.5, y1:0.534091, x2:0, y2:0, stop:0 rgba(0, 0, 127, 255), stop:1 rgba(137, 137, 196, 255));\n"
    "    padding-left:3;\n"
    "}")
            self.confirmOrder.setChecked(False)
            self.confirmOrder.setObjectName("confirmOrder")
            self.confirmOrder.setText(_translate("MainWindow", "CONFIRM"))
            self.listOrder.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
            self.confirmOrder.clicked.connect(partial(addPageConfirm , self , self.page_order , self.menu_order , ListMenuOrder , listMenuDB , price))
        else :
            for x in self.btPageOrder.children() :
                x.deleteLater()
            self.name_order_list.setText(_translate("MainWindow", "ไม่พบเมนู"))
        qtyMenu = num
    else :
        print(len(ListMenuOrder))
        qtyMenu = 1
        self.TextHeaderOrder.setText(_translate("MainWindow", ""))
        self.listOrder.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignCenter)
        self.name_order_list = QtWidgets.QLabel(Box)
        self.name_order_list.setGeometry(QtCore.QRect(20, 20, 531, 33))
        self.name_order_list.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignCenter)
        self.name_order_list.setStyleSheet("*{" "background-color:transparent; color:white;}")
        font = QtGui.QFont()
        font.setFamily("DSN Single")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.name_order_list.setFont(font)
        self.name_order_list.setObjectName("name_order_list")
        id_vertical_order.addWidget(self.name_order_list)
        self.name_order_list.setText(_translate("MainWindow", "ไม่พบเมนู"))
        for x in self.btPageOrder.children() :
            x.deleteLater()
    Box.setGeometry(QtCore.QRect(0, 0, 880, 193 * qtyMenu))

ListNum = {}
def addOrder(self , Box , id_vertical_order , idText , idMenu) :
    print(f"Lis {ListMenuOrder}")
    ListNum.update({idMenu : { 'idText' : idText }})
    price = 0
    for i in reversed(range(id_vertical_order.count())): 
        id_vertical_order.itemAt(i).widget().deleteLater()
    print(f"count {self.btPageOrder.children().count}")
    #if self.btPageOrder.children().count > 0 :
     #   print(f"count {self.btPageOrder.children().count}")
      #  self.btPageOrder.children()[0].deleteLater()
    print(self.btPageOrder.children())
    if len(ListMenuOrder) != 0 : 
        num = 0
        listName = {}
        for key , detail in ListMenuOrder.items() :
            if 'qty' in detail :
                menuDB = listMenuDB.get(key)
                self.cf_order = QtWidgets.QFrame(Box)
                self.cf_order.setEnabled(True)
                self.cf_order.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.cf_order.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.cf_order.setFrameShadow(QtWidgets.QFrame.Raised)
                self.cf_order.setObjectName("cf_order")
                self.name_order_list = QtWidgets.QLabel(self.cf_order)
                self.name_order_list.setGeometry(QtCore.QRect(20, 20, 531, 33))
                font = QtGui.QFont()
                font.setFamily("DSN Single")
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.name_order_list.setFont(font)
                self.name_order_list.setObjectName("name_order_list")
                self.textBath_order = QtWidgets.QLabel(self.cf_order)
                self.textBath_order.setGeometry(QtCore.QRect(452, 130, 351, 35))
                font = QtGui.QFont()
                font.setFamily("DSN PatPong Extend")
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.textBath_order.setFont(font)
                self.textBath_order.setFrameShape(QtWidgets.QFrame.VLine)
                self.textBath_order.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.textBath_order.setObjectName("textBath_order")
                self.buttomOrder = QtWidgets.QFrame(self.cf_order)
                self.buttomOrder.setGeometry(QtCore.QRect(190, 115, 111, 51))
                self.buttomOrder.setStyleSheet("QPushButton {\n"
            "    border-radius:12px;\n"
            "    border:0 solid;\n"
            "    color:white;\n"
            "}\n"
            "\n"
            "QPushButton:selected {\n"
            "    border:0 solid;\n"
            "}")
                self.buttomOrder.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.buttomOrder.setFrameShadow(QtWidgets.QFrame.Raised)
                self.buttomOrder.setObjectName("buttomOrder")
                self.cancel_list_order = QtWidgets.QPushButton(self.buttomOrder)
                self.cancel_list_order.setGeometry(QtCore.QRect(10, 11, 91, 31))
                font = QtGui.QFont()
                font.setFamily("DSN Katreeya")
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.cancel_list_order.setFont(font)
                self.cancel_list_order.setStyleSheet("* {\n"
            "    background-color: rgb(255, 0, 0);\n"
            "    \n"
            "}\n"
            "\n"
            "* :pressed{\n"
            "    border-left:1px solid red;\n"
            "    border-bottom:1px solid red;\n"
            "    background-color: qlineargradient(spread:reflect, x1:0.5, y1:0.534091, x2:0.142, y2:0.0284091, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 140, 140, 255))\n"
            "}")
                self.cancel_list_order.setObjectName("cancel_list_order")
                self.numOrder_2 = QtWidgets.QFrame(self.cf_order)
                self.numOrder_2.setGeometry(QtCore.QRect(40, 115, 151, 51))
                self.numOrder_2.setStyleSheet("QPushButton {\n"
            "    border-radius:16px;\n"
            "    border:0 solid;\n"
            "    color:white;\n"
            "    padding-bottom:3px;\n"
            "    background-color:#8b5234;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color:;\n"
            "    background-color: rgb(188, 109, 70);\n"
            "}")
                self.numOrder_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.numOrder_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.numOrder_2.setObjectName("numOrder_2")
                self.qty_order = QtWidgets.QLabel(self.numOrder_2)
                self.qty_order.setGeometry(QtCore.QRect(2, 12, 150, 33))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.qty_order.setFont(font)
                self.qty_order.setStyleSheet("* {\n"
            "    \n"
            "    background-color: rgba(255, 255, 255, 0);\n"
            "    border:0;\n"
            "}")
                self.qty_order.setAlignment(QtCore.Qt.AlignLeft)
                self.qty_order.setObjectName("qty_order")
                self.iconBathOrder = QtWidgets.QLabel(self.cf_order)
                self.iconBathOrder.setGeometry(QtCore.QRect(810, 128, 35, 35))
                font = QtGui.QFont()
                font.setPointSize(5)
                self.iconBathOrder.setFont(font)
                self.iconBathOrder.setText("")
                self.iconBathOrder.setPixmap(QtGui.QPixmap("assets/img_shop/Bath.png"))
                self.iconBathOrder.setScaledContents(True)
                self.iconBathOrder.setAlignment(QtCore.Qt.AlignCenter)
                self.iconBathOrder.setObjectName("iconBathOrder")
                self.imgOrder = QtWidgets.QLabel(self.cf_order)
                self.imgOrder.setGeometry(QtCore.QRect(740, 10, 80, 106))
                self.imgOrder.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
            "border:1.5 solid #8b5234;\n"
            "border-radius:0px;")
                self.imgOrder.setInputMethodHints(QtCore.Qt.ImhNone)

                pix = QtGui.QPixmap()
                if pix.loadFromData(menuDB['img_menu']) :
                    self.imgOrder.setPixmap(pix)

                self.imgOrder.setScaledContents(True)
                self.imgOrder.setObjectName("imgOrder")
                self.type_order = QtWidgets.QLabel(self.cf_order)
                self.type_order.setGeometry(QtCore.QRect(50, 58, 311, 61))
                font = QtGui.QFont()
                font.setFamily("DSN Single")
                font.setPointSize(18)
                self.type_order.setFont(font)
                self.type_order.setObjectName("type_order")
                id_vertical_order.addWidget(self.cf_order)

                try :
                    taste = detail['taste']
                except :
                    taste = 'หวานปกติ'
                num += 1
                price += int(detail['qty']) * menuDB['price_menu']
                
                def removeButton(boxDelete , size , key , name) :
                    ListMenuOrder.pop(key)
                    listName.pop(name)
                    num = len(ListMenuOrder)
                    boxDelete.deleteLater()
                    ListNum.get(key)['idText'].setText(_translate("MainWindow", "0"))
                    ListNum.pop(key)
                    no = 1
                    for key , val in listName.items() :
                        key.setText(_translate("MainWindow", f"{no}. {val['name']}"))
                        no += 1
                    if len(ListMenuOrder) == 0 :
                        for x in self.btPageOrder.children() :
                            x.deleteLater()
                    self.TextHeaderOrder.setText(_translate("MainWindow", f"รายการทั้งหมด {num} รายการ" if num > 0 else 'กรุณาเลือกเครื่องดื่ม'))
                    size.setGeometry(QtCore.QRect(0, 0, 880, 193 * num))
                
                self.cancel_list_order.clicked.connect(partial(removeButton , self.cf_order , self.list_cf_order , key , self.name_order_list))

                listName.update({self.name_order_list : {'name' : menuDB['name_menu']}})

                self.cf_order.setAccessibleName(_translate("MainWindow", "listcoffee"))
                self.name_order_list.setText(_translate("MainWindow", f"{num}. {menuDB['name_menu']}"))
                self.textBath_order.setText(_translate("MainWindow", f"ยอดรวม {int(detail['qty']) * menuDB['price_menu']}"))
                self.cancel_list_order.setText(_translate("MainWindow", "Cancel"))
                self.qty_order.setText(_translate("MainWindow", f"จำนวน {detail['qty']} แก้ว"))
                self.type_order.setText(_translate("MainWindow", taste))
        self.TextHeaderOrder.setText(_translate("MainWindow", f"รายการทั้งหมด {num} รายการ" if num > 0 else 'กรุณาเลือกเครื่องดื่ม'))
        if num > 0 :
            self.confirmOrder = QtWidgets.QPushButton(self.btPageOrder)
            print(f"con ::::: {self.confirmOrder}")
            self.confirmOrder.setGeometry(QtCore.QRect(365, 5, 150, 39))
            font = QtGui.QFont()
            font.setFamily("DSN SukSaWat")
            font.setPointSize(20)
            self.confirmOrder.setFont(font)
            self.confirmOrder.setStyleSheet("* {\n"
    "    border:1 solid white;\n"
    "    border-radius:19px;\n"
    "    color:white;\n"
    "    background-color: #8b5234;\n"
    "    padding-top:4;\n"
    "}\n"
    "\n"
    "* :pressed{\n"
    "    background-color: qlineargradient(spread:reflect, x1:0.5, y1:0.534091, x2:0, y2:0, stop:0 rgba(0, 0, 127, 255), stop:1 rgba(137, 137, 196, 255));\n"
    "    padding-left:3;\n"
    "}")
            self.confirmOrder.setChecked(False)
            self.confirmOrder.setObjectName("confirmOrder")
            self.confirmOrder.setText(_translate("MainWindow", "CONFIRM"))
            self.listOrder.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
            self.confirmOrder.clicked.connect(partial(addPageConfirm , self , self.page_order , self.menu_order , ListMenuOrder , listMenuDB , price))
        else :
            for x in self.btPageOrder.children() :
                x.deleteLater()
            self.name_order_list.setText(_translate("MainWindow", "ไม่พบเมนู"))
        qtyMenu = num
    else :
        print(len(ListMenuOrder))
        print(self.confirmOrder)
        qtyMenu = 1
        print("chk------------------")
        self.TextHeaderOrder.setText(_translate("MainWindow", ""))
        self.listOrder.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignCenter)
        self.name_order_list = QtWidgets.QLabel(Box)
        self.name_order_list.setGeometry(QtCore.QRect(20, 20, 531, 33))
        self.name_order_list.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignCenter)
        self.name_order_list.setStyleSheet("*{" "background-color:transparent; color:white;}")
        font = QtGui.QFont()
        font.setFamily("DSN Single")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.name_order_list.setFont(font)
        self.name_order_list.setObjectName("name_order_list")
        id_vertical_order.addWidget(self.name_order_list)
        self.name_order_list.setText(_translate("MainWindow", "ไม่พบเมนู"))
        for x in self.btPageOrder.children() :
            x.deleteLater()
    Box.setGeometry(QtCore.QRect(0, 0, 880, 193 * qtyMenu))