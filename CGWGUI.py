from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(700, 400)
        Main.setMinimumSize(QtCore.QSize(700, 400))
        Main.setMaximumSize(QtCore.QSize(700, 400))
        Main.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.Vvdonoe = QtWidgets.QLabel(self.centralwidget)
        self.Vvdonoe.setGeometry(QtCore.QRect(0, -1, 700, 40))
        self.Vvdonoe.setMinimumSize(QtCore.QSize(700, 40))
        self.Vvdonoe.setMaximumSize(QtCore.QSize(700, 40))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Vvdonoe.setFont(font)
        self.Vvdonoe.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.Vvdonoe.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Vvdonoe.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Vvdonoe.setText("Добро пожаловать в генератор поздравлений \"Хванессо\"!")
        self.Vvdonoe.setTextFormat(QtCore.Qt.PlainText)
        self.Vvdonoe.setScaledContents(False)
        self.Vvdonoe.setIndent(45)
        self.Vvdonoe.setObjectName("Vvdonoe")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(240, 300, 211, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.horizontalLayoutWidget.setFont(font)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 260, 230, 40))
        self.label.setMinimumSize(QtCore.QSize(230, 40))
        self.label.setMaximumSize(QtCore.QSize(230, 40))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(85, 170, 255);")
        self.label.setText("Сгенерировать ещё?")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setWordWrap(False)
        self.label.setIndent(5)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 252, 134))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.verticalLayoutWidget.setFont(font)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(250, 40))
        self.label_3.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setText("Разработчик: Nekochort")
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(250, 40))
        self.label_4.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 85, 255);")
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setText("Автор идеи: alicehwan")
        self.label_4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(250, 40))
        self.label_5.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setText("Дизайнер: Sonchous")
        self.label_5.setTextFormat(QtCore.Qt.PlainText)
        self.label_5.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(26, 200, 650, 50))
        self.label_2.setMinimumSize(QtCore.QSize(650, 50))
        self.label_2.setMaximumSize(QtCore.QSize(650, 50))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_2.setText("Нажмите \"Да\" ниже для генерации")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setIndent(1)
        self.label_2.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.label_2.setObjectName("label_2")
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

        self.add_funcs()

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Хванессо"))
        self.Vvdonoe.setText(_translate("Main", "Добро пожаловать в генератор поздравлений \"Хванессо\"!"))
        self.pushButton.setText(_translate("Main", "Да"))
        self.pushButton_2.setText(_translate("Main", "Нет"))
        self.label.setText(_translate("Main", "Сгенерировать ещё?"))
        self.label_3.setText(_translate("Main", "Разработчик: Nekochort"))
        self.label_4.setText(_translate("Main", "Автор идеи: alicehwan"))
        self.label_5.setText(_translate("Main", "Дизайнер: Sonchous"))

    def add_funcs(self):
        self.pushButton.clicked.connect(self.congrats)
        self.pushButton_2.clicked.connect(self.stop)

    def congrats(self, congr):
        from random import randint
        your_list = ['Днём Рождения', 'Новым годом', 'Рождеством', 'Днём заповедников и национальных парков',
                     'Днём работника прокуратуры', 'Днём российской печати', 'Старым Новым годом', 'Крещением Господне',
                     'Днём инженерных войск в России', 'Днём студентов', 'Днём воинской славы России', 'Днём бармена',
                     'Масленицей', 'Днём российской науки', 'Международным днём стоматолога',
                     'Днём рождения гражданского воздушного флота в России', 'Днём дипломатического работника',
                     'Днём Святого Валентина', 'последним Днём Масленицы', 'Днём транспортной милиции России',
                     'Международным днём родного языка', 'Днём защитника Отечества', 'Днём эксперта-криминалиста МВД',
                     'Всемирным Днём гражданской обороны', 'Международным женским днём', 'Днём работника архивов',
                     'Днём работников органов наркоконтроля',
                     'Днём работников уголовно-исполнительной системы Министерства юстиции России',
                     'Днём работников геодезии и картографии',
                     'Днём образования подразделений экономической безопасности в МВД России', 'Днём моряка-подводника',
                     'Днём работников торговли', 'Днём работников гидрометеорологической службы России',
                     'Днём работника культуры России', 'Днём внутренних войск МВД России',
                     'Днём специалиста юридической службы в Вооруженных Силах', 'Днём смеха',
                     'Днём единения народов Белоруссии и России', 'Пасхой', 'Днём геолога',
                     'Днём работника следственных органов', 'Днём рождения Рунета',
                     'Днём войск противовоздушной обороны',
                     'Всемирным днём авиации и космонавтики', 'Днём специалиста по радиоэлектронной борьбе',
                     'Всемирным днём интеллектуальной собственности', 'Всемирным днём охраны труда',
                     'Днём пожарной охраны',
                     'Праздником труда', 'Днём шифровальщика', 'Днём водолаза', 'Днём святого Георгия Победоносца',
                     'Днём радио', 'Днём Черноморского флота', 'Днём фрилансера', 'Международным днём музеев',
                     'Днём Балтийского флота', 'Всемирным днём метрологии', 'Днём Тихоокеанского флота',
                     'Днём военного переводчика', 'Днём кадровика', 'Днём славянской письменности и культуры',
                     'Днём филолога', 'Днём российского предпринимательства', 'Днём библиотекаря', 'Днём пограничника',
                     'Днём военного автомобилиста', 'Днём ветеранов таможенной службы', 'Днём химика',
                     'Днём российской адвокатуры', 'Международным днём защиты детей', 'Днём Северного флота России',
                     'Днём эколога', 'Днём социального работника', 'Днём независимости России', 'Днём пивовара',
                     'Днём мебельщика', 'Днём работников легкой промышленности', 'Днём работников миграционной службы',
                     'Днём медицинского работника', 'Днём кинологических подразделений МВД России',
                     'Днём дружбы и единения славян', 'Днём изобретателя и рационализатора', 'Днём молодежи России',
                     'Днём ГАИ', 'Днём работников морского и речного флота',
                     'Всероссийским днём семьи, любви и верности',
                     'Днём рыбака', 'Днём российской почты', 'Днём рождения морской авиации ВМФ России',
                     'Днём металлурга',
                     'Днём военно-морского флота', 'Днём парашютиста', 'Днём PR-специалиста',
                     'Днём системного администратора', 'Днём тыла вооруженных сил РФ',
                     'профессиональным праздником сотрудников инкассации', 'Днём железнодорожника',
                     'Днём воздушно-десантных войск', 'Днём железнодорожных войск', 'Днём строителя',
                     'Днём Военно-воздушных сил', 'Днём физкультурника', 'Днём Воздушного флота России',
                     'Днём археолога',
                     'Днём Государственного флага Российской Федерации', 'Днём российского кино',
                     'Днём шахтера в России',
                     'Днём знаний', 'Днём российской гвардии', 'Днём солидарности в борьбе с терроризмом',
                     'Днём специалиста по ядерному обеспечению',
                     'Днём работников нефтяной, газовой и топливной промышленности', 'Днём финансиста России',
                     'Днём тестировщика', 'Днём воинской славы России', 'Днём танкиста в России 2010', 'Днём Байкала',
                     'Днём секретаря', 'Днём работника леса', 'Днём рекрутера', 'Днём машиностроителя',
                     'Днём воспитателя и всех дошкольных работников', 'Днём работника атомной промышленности',
                     'Днём интернета в России', 'Международным днём пожилых людей в России', 'Днём сухопутных войск РФ',
                     'Днём ОМОНа', 'Днём Космических войск', 'Днём гражданской обороны МЧС России', 'Днём учителя',
                     'Днём работников уголовного розыска', 'Днём российского страховщика',
                     'Днём образования штабных подразделений МВД РФ',
                     'Днём командира надводного, подводного и воздушного корабля',
                     'Днём работника сельского хозяйства и перерабатывающей промышленности',
                     'Днём создания адресно-справочной службы Российского государства', 'Всемирным днём анестезиолога',
                     'Днём работников пищевой промышленности', 'Днём работников дорожного хозяйства',
                     'Днём рождения Российского военно-морского флота', 'Днём военного связиста',
                     'Литературным праздником «Белые журавли»', 'Днём работников рекламы',
                     'Днём подразделений специального назначения', 'Днём таможенника Российской Федерации',
                     'Днём работника кабельной промышленности', 'Днём создания армейской авиации России',
                     'Днём работников службы вневедомственной охраны МВД', 'Днём инженера-механика',
                     'Днём автомобилиста',
                     'Днём сурдопереводчика', 'Днём судебного пристава', 'Днём судебного пристава',
                     'Днём народного единства', 'Днём военного разведчика', 'Всемирным днём мужчин',
                     'Международным днём КВН', 'Днём российской милиции', 'Всемирным днём качества',
                     'Днём работников Сбербанка России', 'Днём специалиста по безопасности',
                     'Днём войск радиационной, химической и биологической защиты', 'Днём социолога',
                     'Днём создания подразделений по борьбе с организованной преступностью',
                     'Всероссийский днём призывника', 'Днём участкового', 'Днём рождения Деда Мороза',
                     'Днём ракетных войск и артиллерии', 'Днём работника стекольной промышленности',
                     'Днём бухгалтера России', 'Днём работника налоговых органов РФ', 'Днём психолога в России',
                     'Днём морской пехоты', 'Днём оценщика в России', 'Днём матери в России',
                     'Всемирным днём борьбы со СПИДом', 'Днём банковского работника России', 'Днём юриста в России',
                     'Днём информатики в России', 'Днём сетевика в России', 'Днём образования российского казначейства',
                     'Днём Героев Отечества в России', 'Днём создания службы связи МВД России',
                     'Днём Конституции Российской Федерации', 'Днём Ракетных войск стратегического назначения',
                     'Днём подразделений собственной безопасности органов внутренних дел РФ',
                     'Днём работников органов ЗАГСа', 'Днём риэлтора',
                     'Днём работника органов государственной безопасности РФ', 'Днём энергетика',
                     'Днём дальней авиации ВВС России', 'Днём спасателя в России', 'Хэлоуином']
        congr = ("С " + your_list[randint(0, len(your_list) - 1)] + "!")

        self.label_2.setText(f"{congr}")

    def stop(self):
        exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())
