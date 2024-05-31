# -*- coding: utf-8 -*-

# ---------------------------------------------- БИБЛИОТЕКИ ------------------------------------------------------------
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
# ----------------------------------------------------------------------------------------------------------------------


class Ui_MainWindow(object):
    """
        Класс Ui_MainWindow отвечает за создание и настройку графического интерфейса главного окна приложения.

        Атрибуты экземпляра:
        --------------------
        centralwidget : QWidget
            Центральный виджет, содержащий все элементы интерфейса.

        label_hello_main : QLabel
            Метка с приветственным сообщением.

        pushButton_choose_file : QPushButton
            Кнопка ВЫБРАТЬ (открывает окно, где можно выбрать файл и транскрибировать его).

        pushButton_record_audio : QPushButton
            Кнопка ЗАПИСАТЬ (Открывает окно, где можно транскрибировать прямую речь).

        label_what_u_want : QLabel
            Метка с вопросом, что пользователь хочет сделать.

        pushButton_about_prog : QPushButton
            Кнопка О ПРОГРАММЕ (открывает окно. где можно прочитать про программу подробней).

        label_img_man_with_pc : QLabel
            Метка с изображением человека с компьютером.

        label_img_pc : QLabel
            Метка с изображением компьютера.

        label_easy_fast_slogan : QLabel
            Метка с слоганом программы.

        label_every_audio_to_text : QLabel
            Метка с описанием функции программы.

        label_about_left : QLabel
            Метка с дополнительной информацией о программе (левая часть).

        label_about_right : QLabel
            Метка с дополнительной информацией о программе (правая часть).

        label_every_audio_to_text_2 : QLabel
            Метка с иконкой микрофона.

        label_every_audio_to_text_3 : QLabel
            Метка с иконкой шестеренки.

        label_every_audio_to_text_4 : QLabel
            Метка с иконкой руки вниз.

        label_every_audio_to_text_5 : QLabel
            Метка с иконкой документа.

        label_every_audio_to_text_6 : QLabel
            Метка с иконкой таймера.

        label_every_audio_to_text_7 : QLabel
            Метка с иконкой приветствующей руки (слева).

        label_every_audio_to_text_8 : QLabel
            Метка с иконкой приветствующей руки (справа).

        menubar : QMenuBar
            Меню-бар приложения.

        statusbar : QStatusBar
            Статус-бар приложения.

        Методы:
        -------
        setupUi(self, MainWindow):
            Настраивает пользовательский интерфейс диалогового окна.

        retranslateUi(self, MainWindow):
            Устанавливает текст для элементов интерфейса на русском языке.

        """
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(947, 843)
        MainWindow.setMinimumSize(QSize(947, 843))
        MainWindow.setMaximumSize(QSize(947, 843))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, "
            u"stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
            "font-family: Corbel;")
        self.label_hello_main = QLabel(self.centralwidget)
        self.label_hello_main.setObjectName(u"label_hello_main")
        self.label_hello_main.setGeometry(QRect(70, 20, 901, 51))
        font = QFont()
        font.setFamilies([u"Corbel"])
        font.setPointSize(22)
        font.setBold(True)
        self.label_hello_main.setFont(font)
        self.label_hello_main.setStyleSheet(u"color: white;\n"
            "font-weight: bold;\n"
            "background-color: none;\n"
            "border: none; ")
        self.pushButton_choose_file = QPushButton(self.centralwidget)
        self.pushButton_choose_file.setObjectName(u"pushButton_choose_file")
        self.pushButton_choose_file.setGeometry(QRect(120, 730, 201, 41))
        self.pushButton_choose_file.setStyleSheet(u"\n"
            "QPushButton{\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 16pt;\n"
            "background-color:rgba(255,255,255,30);\n"
            "border: 1px solid rgba(255,255,255,40);\n"
            "border-radius:20px;\n"
            "width: 230;\n"
            "height: 50;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color:rgba(255,255,255,30);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "background-color:rgba(255,255,255,70);\n"
            "}")
        icon = QIcon()
        icon.addFile(u"../icons/file_folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_choose_file.setIcon(icon)
        self.pushButton_choose_file.setIconSize(QSize(25, 25))
        self.pushButton_record_audio = QPushButton(self.centralwidget)
        self.pushButton_record_audio.setObjectName(u"pushButton_record_audio")
        self.pushButton_record_audio.setGeometry(QRect(390, 730, 201, 41))
        self.pushButton_record_audio.setStyleSheet(u"\n"
            "QPushButton{\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 16pt;\n"
            "background-color:rgba(255,255,255,30);\n"
            "border: 1px solid rgba(255,255,255,40);\n"
            "border-radius:20px;\n"
            "width: 230;\n"
            "height: 50;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color:rgba(255,255,255,30);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "background-color:rgba(255,255,255,70);\n"
            "}")
        icon1 = QIcon()
        icon1.addFile(u"../icons/mic_on.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_record_audio.setIcon(icon1)
        self.pushButton_record_audio.setIconSize(QSize(25, 25))
        self.label_what_u_want = QLabel(self.centralwidget)
        self.label_what_u_want.setObjectName(u"label_what_u_want")
        self.label_what_u_want.setGeometry(QRect(300, 660, 391, 41))
        font1 = QFont()
        font1.setFamilies([u"Corbel"])
        font1.setPointSize(25)
        font1.setBold(True)
        self.label_what_u_want.setFont(font1)
        self.label_what_u_want.setStyleSheet(u"color: white;\n"
            "font-size: 25pt;\n"
            "font-weight: bold;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.pushButton_about_prog = QPushButton(self.centralwidget)
        self.pushButton_about_prog.setObjectName(u"pushButton_about_prog")
        self.pushButton_about_prog.setGeometry(QRect(660, 730, 201, 41))
        self.pushButton_about_prog.setStyleSheet(u"\n"
            "QPushButton{\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 16pt;\n"
            "background-color:rgba(255,255,255,30);\n"
            "border: 1px solid rgba(255,255,255,40);\n"
            "border-radius:20px;\n"
            "width: 230;\n"
            "height: 50;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color:rgba(255,255,255,30);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "background-color:rgba(255,255,255,70);\n"
            "}")
        icon2 = QIcon()
        icon2.addFile(u"../icons/help_question.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_about_prog.setIcon(icon2)
        self.pushButton_about_prog.setIconSize(QSize(25, 25))
        self.label_img_man_with_pc = QLabel(self.centralwidget)
        self.label_img_man_with_pc.setObjectName(u"label_img_man_with_pc")
        self.label_img_man_with_pc.setEnabled(True)
        self.label_img_man_with_pc.setGeometry(QRect(130, 190, 321, 321))
        self.label_img_man_with_pc.setFocusPolicy(Qt.NoFocus)
        self.label_img_man_with_pc.setStyleSheet(u"border: 1px solid rgba(255,255,255,40);\n" "border-radius:130px;")
        self.label_img_man_with_pc.setFrameShape(QFrame.NoFrame)
        self.label_img_man_with_pc.setPixmap(QPixmap(u"../icons/img/dict_text_monitor_round.png"))
        self.label_img_man_with_pc.setScaledContents(True)
        self.label_img_man_with_pc.setWordWrap(False)
        self.label_img_pc = QLabel(self.centralwidget)
        self.label_img_pc.setObjectName(u"label_img_pc")
        self.label_img_pc.setEnabled(True)
        self.label_img_pc.setGeometry(QRect(520, 190, 321, 321))
        self.label_img_pc.setFocusPolicy(Qt.NoFocus)
        self.label_img_pc.setStyleSheet(u"border: 1px solid rgba(255,255,255,40);\n" "border-radius:130px;")
        self.label_img_pc.setFrameShape(QFrame.NoFrame)
        self.label_img_pc.setPixmap(QPixmap(u"../icons/img/trancribation_round.png"))
        self.label_img_pc.setScaledContents(True)
        self.label_easy_fast_slogan = QLabel(self.centralwidget)
        self.label_easy_fast_slogan.setObjectName(u"label_easy_fast_slogan")
        self.label_easy_fast_slogan.setGeometry(QRect(60, 80, 841, 41))
        self.label_easy_fast_slogan.setFont(font1)
        self.label_easy_fast_slogan.setStyleSheet(u"color: white;\n"
            "font-weight: bold;\n"
            "font-size: 25pt;\n"
            "background-color: none;\n"
            "border: none; ")
        self.label_easy_fast_slogan.setWordWrap(True)
        self.label_easy_fast_slogan.setOpenExternalLinks(False)
        self.label_every_audio_to_text = QLabel(self.centralwidget)
        self.label_every_audio_to_text.setObjectName(u"label_every_audio_to_text")
        self.label_every_audio_to_text.setGeometry(QRect(150, 130, 691, 61))
        font2 = QFont()
        font2.setFamilies([u"Corbel"])
        font2.setPointSize(18)
        self.label_every_audio_to_text.setFont(font2)
        self.label_every_audio_to_text.setStyleSheet(u"color: white;\n"
            "font-size: 18pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_every_audio_to_text.setWordWrap(True)
        self.label_every_audio_to_text.setOpenExternalLinks(False)
        self.label_about_left = QLabel(self.centralwidget)
        self.label_about_left.setObjectName(u"label_about_left")
        self.label_about_left.setGeometry(QRect(120, 520, 351, 128))
        self.label_about_left.setFont(font2)
        self.label_about_left.setStyleSheet(u"color: white;\n"
            "font-size: 18pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_about_left.setWordWrap(True)
        self.label_about_left.setOpenExternalLinks(False)
        self.label_about_right = QLabel(self.centralwidget)
        self.label_about_right.setObjectName(u"label_about_right")
        self.label_about_right.setGeometry(QRect(510, 520, 381, 128))
        self.label_about_right.setFont(font2)
        self.label_about_right.setStyleSheet(u"color: white;\n"
            "font-size: 18pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_about_right.setWordWrap(True)
        self.label_about_right.setOpenExternalLinks(False)
        self.label_every_audio_to_text_2 = QLabel(self.centralwidget)
        self.label_every_audio_to_text_2.setObjectName(u"label_every_audio_to_text_2")
        self.label_every_audio_to_text_2.setGeometry(QRect(90, 520, 31, 51))
        font3 = QFont()
        font3.setFamilies([u"Corbel"])
        font3.setPointSize(14)
        self.label_every_audio_to_text_2.setFont(font3)
        self.label_every_audio_to_text_2.setStyleSheet(u"color: white;\n"
            "font-size: 14pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_every_audio_to_text_2.setPixmap(QPixmap(u"../icons/img/smiles/micro_28_new.png"))
        self.label_every_audio_to_text_2.setWordWrap(True)
        self.label_every_audio_to_text_2.setOpenExternalLinks(False)
        self.label_every_audio_to_text_3 = QLabel(self.centralwidget)
        self.label_every_audio_to_text_3.setObjectName(u"label_every_audio_to_text_3")
        self.label_every_audio_to_text_3.setGeometry(QRect(478, 520, 41, 51))
        self.label_every_audio_to_text_3.setFont(font3)
        self.label_every_audio_to_text_3.setStyleSheet(u"color: white;\n"
            "font-size: 14pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_every_audio_to_text_3.setPixmap(QPixmap(u"../icons/img/smiles/gear_32.png"))
        self.label_every_audio_to_text_3.setWordWrap(True)
        self.label_every_audio_to_text_3.setOpenExternalLinks(False)
        self.label_every_audio_to_text_4 = QLabel(self.centralwidget)
        self.label_every_audio_to_text_4.setObjectName(u"label_every_audio_to_text_4")
        self.label_every_audio_to_text_4.setGeometry(QRect(650, 660, 51, 51))
        self.label_every_audio_to_text_4.setFont(font3)
        self.label_every_audio_to_text_4.setStyleSheet(u"color: white;\n"
            "font-size: 14pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_every_audio_to_text_4.setPixmap(QPixmap(u"../icons/img/smiles/hand_down_48.png"))
        self.label_every_audio_to_text_4.setWordWrap(True)
        self.label_every_audio_to_text_4.setOpenExternalLinks(False)
        self.label_every_audio_to_text_5 = QLabel(self.centralwidget)
        self.label_every_audio_to_text_5.setObjectName(u"label_every_audio_to_text_5")
        self.label_every_audio_to_text_5.setGeometry(QRect(120, 130, 31, 61))
        self.label_every_audio_to_text_5.setFont(font3)
        self.label_every_audio_to_text_5.setStyleSheet(u"color: white;\n"
            "font-size: 14pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_every_audio_to_text_5.setPixmap(QPixmap(u"../icons/img/smiles/doc-28.png"))
        self.label_every_audio_to_text_5.setWordWrap(True)
        self.label_every_audio_to_text_5.setOpenExternalLinks(False)
        self.label_every_audio_to_text_6 = QLabel(self.centralwidget)
        self.label_every_audio_to_text_6.setObjectName(u"label_every_audio_to_text_6")
        self.label_every_audio_to_text_6.setGeometry(QRect(770, 130, 31, 61))
        self.label_every_audio_to_text_6.setFont(font3)
        self.label_every_audio_to_text_6.setStyleSheet(u"color: white;\n"
            "font-size: 14pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_every_audio_to_text_6.setPixmap(QPixmap(u"../icons/img/smiles/taimer_28.png"))
        self.label_every_audio_to_text_6.setWordWrap(True)
        self.label_every_audio_to_text_6.setOpenExternalLinks(False)
        self.label_every_audio_to_text_7 = QLabel(self.centralwidget)
        self.label_every_audio_to_text_7.setObjectName(u"label_every_audio_to_text_7")
        self.label_every_audio_to_text_7.setGeometry(QRect(30, 30, 35, 35))
        self.label_every_audio_to_text_7.setFont(font3)
        self.label_every_audio_to_text_7.setStyleSheet(u"color: white;\n"
            "font-size: 14pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_every_audio_to_text_7.setPixmap(QPixmap(u"../icons/img/smiles/hello_hand_35.png"))
        self.label_every_audio_to_text_7.setWordWrap(True)
        self.label_every_audio_to_text_7.setOpenExternalLinks(False)
        self.label_every_audio_to_text_8 = QLabel(self.centralwidget)
        self.label_every_audio_to_text_8.setObjectName(u"label_every_audio_to_text_8")
        self.label_every_audio_to_text_8.setGeometry(QRect(885, 30, 35, 35))
        self.label_every_audio_to_text_8.setFont(font3)
        self.label_every_audio_to_text_8.setStyleSheet(u"color: white;\n"
            "font-size: 14pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_every_audio_to_text_8.setPixmap(QPixmap(u"../icons/img/smiles/hello_hand_35.png"))
        self.label_every_audio_to_text_8.setWordWrap(True)
        self.label_every_audio_to_text_8.setOpenExternalLinks(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 947, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):   #  Устанавливает текст для элементов интерфейса на русском языке
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AudioToText", None))
        self.label_hello_main.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u043e "
            u"\u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c \u0432 "
            u"\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0443 "
            u"\u0442\u0440\u0430\u043d\u0441\u043a\u0440\u0438\u0431\u0430\u0446\u0438\u0438 \"AudioToText\"", None))

        self.pushButton_choose_file.setToolTip(QCoreApplication.translate("MainWindow",
            u"<html><head/><body><p>\u041d\u0430\u0436\u043c\u0438\u0442\u0435, \u0447\u0442\u043e\u0431\u044b "
            u"\u043f\u0435\u0440\u0435\u0439\u0442\u0438 \u043a \u043f\u0435\u0440\u0435\u0432\u043e\u0434\u0443 "
            u"\u0430\u0443\u0434\u0438\u043e / \u0432\u0438\u0434\u0435\u043e \u0432 "
            u"\u0442\u0435\u043a\u0441\u0442</p></body></html>", None))

        self.pushButton_choose_file.setText(QCoreApplication.translate("MainWindow",
            u" \u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))

        self.pushButton_record_audio.setToolTip(QCoreApplication.translate("MainWindow",
            u"<html><head/><body><p>\u041d\u0430\u0436\u043c\u0438\u0442\u0435, "
            u"\u0447\u0442\u043e\u0431\u044b \u043f\u0435\u0440\u0435\u0439\u0442\u0438 \u043a "
            u"\u0437\u0430\u043f\u0438\u0441\u0438 \u0441\u0432\u043e\u0435\u0433\u043e "
            u"\u0430\u0443\u0434\u0438\u043e</p></body></html>", None))

        self.pushButton_record_audio.setText(QCoreApplication.translate("MainWindow",
            u" \u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c", None))
        self.label_what_u_want.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0442\u043e \u0432\u044b "
            u"\u0445\u043e\u0442\u0438\u0442\u0435 \u0441\u0434\u0435\u043b\u0430\u0442\u044c?", None))

        self.pushButton_about_prog.setToolTip(QCoreApplication.translate("MainWindow",
            u"<html><head/><body><p>\u041d\u0430\u0436\u043c\u0438\u0442\u0435, "
            u"\u0447\u0442\u043e\u0431\u044b \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u044c "
            u"\u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e "
            u"\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435</p></body></html>", None))

        self.pushButton_about_prog.setText(QCoreApplication.translate("MainWindow",
            u" \u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435?", None))

        self.label_img_man_with_pc.setText("")
        self.label_img_pc.setText("")

        self.label_easy_fast_slogan.setText(QCoreApplication.translate("MainWindow",
            u"\u041f\u0440\u0435\u0432\u0440\u0430\u0442\u0438 \u0440\u0435\u0447\u044c "
            u"\u0432 \u0441\u043b\u043e\u0432\u0430: \"\u041f\u0440\u043e\u0441\u0442\u043e, "
            u"\u0411\u044b\u0441\u0442\u0440\u043e, "
            u"\u0412\u043f\u0435\u0447\u0430\u0442\u043b\u044f\u044e\u0449\u0435!\"", None))

        self.label_every_audio_to_text.setText(QCoreApplication.translate("MainWindow",
            u" \u0417\u0434\u0435\u0441\u044c \u043a\u0430\u0436\u0434\u043e\u0435 "
            u"\u0430\u0443\u0434\u0438\u043e \u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u0441\u044f "
            u"\u0442\u0435\u043a\u0441\u0442\u043e\u043c \u0432 "
            u"\u043c\u0433\u043d\u043e\u0432\u0435\u043d\u0438\u0435 \u043e\u043a\u0430! ", None))
        self.label_about_left.setText(QCoreApplication.translate("MainWindow",
            u"<html><head/><body><p>\u041d\u0430\u0434\u0438\u043a\u0442\u0443\u0439\u0442\u0435 "
            u"\u0442\u0435\u043a\u0441\u0442 \u0432 \u043c\u0438\u043a\u0440\u043e\u0444\u043e\u043d "
            u"\u0438 \u043f\u043e\u043b\u0443\u0447\u0438\u0442\u0435 \u0435\u0433\u043e "
            u"\u0442\u0435\u043a\u0441\u0442\u043e\u043c \u043f\u0440\u044f\u043c\u043e "
            u"\u043d\u0430 \u0432\u0430\u0448\u0435 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e!</p>"
            u"</body></html>", None))

        self.label_about_right.setText(QCoreApplication.translate("MainWindow",
            u"<html><head/><body><p>\u041d\u0430\u0448 "
            u"\u0438\u0441\u043a\u0443\u0441\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 "
            u"\u0438\u043d\u0442\u0435\u043b\u043b\u0435\u043a\u0442 \u043e\u0431\u0435\u0449\u0430\u0435\u0442 "
            u"\u0442\u0440\u0430\u043d\u0441\u043a\u0440\u0438\u0431\u0438\u0440\u043e\u0432\u0430\u0442\u044c "
            u"\u043b\u044e\u0431\u043e\u0435 \u0430\u0443\u0434\u0438\u043e, \u0430 \u0442\u0430\u043a\u0436\u0435 "
            u"\u0432\u0438\u0434\u0435\u043e! </p></body></html>", None))

        self.label_every_audio_to_text_2.setText("")
        self.label_every_audio_to_text_3.setText("")
        self.label_every_audio_to_text_4.setText("")
        self.label_every_audio_to_text_5.setText("")
        self.label_every_audio_to_text_6.setText("")
        self.label_every_audio_to_text_7.setText("")
        self.label_every_audio_to_text_8.setText("")