# -*- coding: utf-8 -*-

# ---------------------------------------------- БИБЛИОТЕКИ ------------------------------------------------------------
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)
# ----------------------------------------------------------------------------------------------------------------------


class Ui_Dialog_info(object):
    """Класс Ui_Dialog_info представляет собой пользовательский интерфейс для диалогового окна с информацией о программе.

    Методы:
    -------
    setupUi(self, Dialog_info):
        Настраивает пользовательский интерфейс для диалогового окна, устанавливает свойства и стиль элементов.

    retranslateUi(self, Dialog_info):
        Переводит и устанавливает текст для элементов интерфейса.
    """

    def setupUi(self, Dialog_info):           # Установка параметров UI элементов окна со справочной информацией
        if not Dialog_info.objectName():
            Dialog_info.setObjectName(u"Dialog_info")
        Dialog_info.resize(679, 679)
        Dialog_info.setMinimumSize(QSize(679, 679))
        Dialog_info.setMaximumSize(QSize(679, 679))
        Dialog_info.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 "
            u"rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
            "font-family: Corbel;")
        self.pushButton_back_to_main = QPushButton(Dialog_info)
        self.pushButton_back_to_main.setObjectName(u"pushButton_back_to_main")
        self.pushButton_back_to_main.setGeometry(QRect(10, 10, 51, 51))
        self.pushButton_back_to_main.setStyleSheet(u"\n"
            "QPushButton{\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 16pt;\n"
            "background-color:rgba(255,255,255,30);\n"
            "border: 1px solid rgba(255,255,255,40);\n"
            "border-radius:20px;\n"
            "width: 230;\n"
            "height: 50;\n"
            "border: 1px solid rgba(255,255,255,40);\n"
            "border-radius:25px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color:rgba(255,255,255,30);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "background-color:rgba(255,255,255,70);\n"
            "}")
        icon = QIcon()
        icon.addFile(u"../icons/back_arrow.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_back_to_main.setIcon(icon)
        self.pushButton_back_to_main.setIconSize(QSize(35, 35))
        self.label_every_audio_to_text_9 = QLabel(Dialog_info)
        self.label_every_audio_to_text_9.setObjectName(u"label_every_audio_to_text_9")
        self.label_every_audio_to_text_9.setGeometry(QRect(577, 70, 41, 35))
        font = QFont()
        font.setFamilies([u"Corbel"])
        font.setPointSize(14)
        self.label_every_audio_to_text_9.setFont(font)
        self.label_every_audio_to_text_9.setStyleSheet(u"color: white;\n"
            "font-size: 14pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_every_audio_to_text_9.setPixmap(QPixmap(u"../icons/img/smiles/answer_&_question_45.png"))
        self.label_every_audio_to_text_9.setWordWrap(True)
        self.label_every_audio_to_text_9.setOpenExternalLinks(False)
        self.label_every_audio_to_text_10 = QLabel(Dialog_info)
        self.label_every_audio_to_text_10.setObjectName(u"label_every_audio_to_text_10")
        self.label_every_audio_to_text_10.setGeometry(QRect(160, 136, 41, 41))
        self.label_every_audio_to_text_10.setFont(font)
        self.label_every_audio_to_text_10.setStyleSheet(u"color: white;\n"
            "font-size: 14pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_every_audio_to_text_10.setPixmap(QPixmap(u"../icons/img/smiles/question_info_45.png"))
        self.label_every_audio_to_text_10.setWordWrap(True)
        self.label_every_audio_to_text_10.setOpenExternalLinks(False)
        self.label_every_audio_to_text_11 = QLabel(Dialog_info)
        self.label_every_audio_to_text_11.setObjectName(u"label_every_audio_to_text_11")
        self.label_every_audio_to_text_11.setGeometry(QRect(160, 300, 41, 41))
        self.label_every_audio_to_text_11.setFont(font)
        self.label_every_audio_to_text_11.setStyleSheet(u"color: white;\n"
            "font-size: 14pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_every_audio_to_text_11.setPixmap(QPixmap(u"../icons/img/smiles/question_info_45.png"))
        self.label_every_audio_to_text_11.setWordWrap(True)
        self.label_every_audio_to_text_11.setOpenExternalLinks(False)
        self.label_every_audio_to_text_12 = QLabel(Dialog_info)
        self.label_every_audio_to_text_12.setObjectName(u"label_every_audio_to_text_12")
        self.label_every_audio_to_text_12.setGeometry(QRect(160, 420, 41, 41))
        self.label_every_audio_to_text_12.setFont(font)
        self.label_every_audio_to_text_12.setStyleSheet(u"color: white;\n"
            "font-size: 14pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_every_audio_to_text_12.setPixmap(QPixmap(u"../icons/img/smiles/question_info_45.png"))
        self.label_every_audio_to_text_12.setWordWrap(True)
        self.label_every_audio_to_text_12.setOpenExternalLinks(False)
        self.label_every_audio_to_text_13 = QLabel(Dialog_info)
        self.label_every_audio_to_text_13.setObjectName(u"label_every_audio_to_text_13")
        self.label_every_audio_to_text_13.setGeometry(QRect(160, 550, 41, 41))
        self.label_every_audio_to_text_13.setFont(font)
        self.label_every_audio_to_text_13.setStyleSheet(u"color: white;\n"
            "font-size: 14pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_every_audio_to_text_13.setPixmap(QPixmap(u"../icons/img/smiles/question_info_45.png"))
        self.label_every_audio_to_text_13.setWordWrap(True)
        self.label_every_audio_to_text_13.setOpenExternalLinks(False)
        self.label_every_audio_to_text_14 = QLabel(Dialog_info)
        self.label_every_audio_to_text_14.setObjectName(u"label_every_audio_to_text_14")
        self.label_every_audio_to_text_14.setGeometry(QRect(35, 170, 51, 51))
        self.label_every_audio_to_text_14.setFont(font)
        self.label_every_audio_to_text_14.setStyleSheet(u"color: white;\n"
            "font-size: 14pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_every_audio_to_text_14.setPixmap(QPixmap(u"../icons/img/smiles/check_info_35.png"))
        self.label_every_audio_to_text_14.setWordWrap(True)
        self.label_every_audio_to_text_14.setOpenExternalLinks(False)
        self.label_every_audio_to_text_15 = QLabel(Dialog_info)
        self.label_every_audio_to_text_15.setObjectName(u"label_every_audio_to_text_15")
        self.label_every_audio_to_text_15.setGeometry(QRect(35, 330, 51, 51))
        self.label_every_audio_to_text_15.setFont(font)
        self.label_every_audio_to_text_15.setStyleSheet(u"color: white;\n"
            "font-size: 14pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_every_audio_to_text_15.setPixmap(QPixmap(u"../icons/img/smiles/check_info_35.png"))
        self.label_every_audio_to_text_15.setWordWrap(True)
        self.label_every_audio_to_text_15.setOpenExternalLinks(False)
        self.label_every_audio_to_text_16 = QLabel(Dialog_info)
        self.label_every_audio_to_text_16.setObjectName(u"label_every_audio_to_text_16")
        self.label_every_audio_to_text_16.setGeometry(QRect(35, 450, 51, 51))
        self.label_every_audio_to_text_16.setFont(font)
        self.label_every_audio_to_text_16.setStyleSheet(u"color: white;\n"
            "font-size: 14pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_every_audio_to_text_16.setPixmap(QPixmap(u"../icons/img/smiles/check_info_35.png"))
        self.label_every_audio_to_text_16.setWordWrap(True)
        self.label_every_audio_to_text_16.setOpenExternalLinks(False)
        self.label_every_audio_to_text_17 = QLabel(Dialog_info)
        self.label_every_audio_to_text_17.setObjectName(u"label_every_audio_to_text_17")
        self.label_every_audio_to_text_17.setGeometry(QRect(35, 490, 51, 51))
        self.label_every_audio_to_text_17.setFont(font)
        self.label_every_audio_to_text_17.setStyleSheet(u"color: white;\n"
            "font-size: 14pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_every_audio_to_text_17.setPixmap(QPixmap(u"../icons/img/smiles/check_info_35.png"))
        self.label_every_audio_to_text_17.setWordWrap(True)
        self.label_every_audio_to_text_17.setOpenExternalLinks(False)
        self.label_every_audio_to_text_18 = QLabel(Dialog_info)
        self.label_every_audio_to_text_18.setObjectName(u"label_every_audio_to_text_18")
        self.label_every_audio_to_text_18.setGeometry(QRect(35, 580, 51, 51))
        self.label_every_audio_to_text_18.setFont(font)
        self.label_every_audio_to_text_18.setStyleSheet(u"color: white;\n"
            "font-size: 14pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_every_audio_to_text_18.setPixmap(QPixmap(u"../icons/img/smiles/check_info_35.png"))
        self.label_every_audio_to_text_18.setWordWrap(True)
        self.label_every_audio_to_text_18.setOpenExternalLinks(False)
        self.label_main_label_info = QLabel(Dialog_info)
        self.label_main_label_info.setObjectName(u"label_main_label_info")
        self.label_main_label_info.setGeometry(QRect(61, 71, 563, 41))
        font1 = QFont()
        font1.setFamilies([u"Corbel"])
        font1.setPointSize(25)
        font1.setBold(True)
        self.label_main_label_info.setFont(font1)
        self.label_main_label_info.setStyleSheet(u"color: white;\n"
            "font-weight: bold;\n"
            "font-size: 25pt;\n"
            "background-color: none;\n"
            "border: none; ")
        self.label_main_label_info.setWordWrap(True)
        self.label_main_label_info.setOpenExternalLinks(False)
        self.label_every_audio_to_text_8 = QLabel(Dialog_info)
        self.label_every_audio_to_text_8.setObjectName(u"label_every_audio_to_text_8")
        self.label_every_audio_to_text_8.setGeometry(QRect(80, 70, 41, 35))
        self.label_every_audio_to_text_8.setFont(font)
        self.label_every_audio_to_text_8.setStyleSheet(u"color: white;\n"
            "font-size: 14pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_every_audio_to_text_8.setPixmap(QPixmap(u"../icons/img/smiles/answer_&_question_45.png"))
        self.label_every_audio_to_text_8.setWordWrap(True)
        self.label_every_audio_to_text_8.setOpenExternalLinks(False)
        self.label_6 = QLabel(Dialog_info)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 140, 421, 33))
        font2 = QFont()
        font2.setFamilies([u"Corbel"])
        font2.setPointSize(20)
        self.label_6.setFont(font2)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setStyleSheet(u"color: white;\n"
            "font-size: 20pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_6.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(Dialog_info)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(75, 180, 561, 112))
        font3 = QFont()
        font3.setFamilies([u"Corbel"])
        font3.setPointSize(18)
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"color: white;\n"
            "font-size: 18pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_8.setWordWrap(True)
        self.label_8.setOpenExternalLinks(False)
        self.label_10 = QLabel(Dialog_info)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(50, 550, 364, 33))
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"color: white;\n"
            "font-size: 20pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_11 = QLabel(Dialog_info)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(75, 595, 551, 35))
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"color: white;\n"
            "font-size: 18pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_11.setWordWrap(True)
        self.label_11.setOpenExternalLinks(False)
        self.label_13 = QLabel(Dialog_info)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(75, 465, 561, 82))
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"color: white;\n"
            "font-size: 18pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_13.setWordWrap(True)
        self.label_13.setOpenExternalLinks(False)
        self.label_12 = QLabel(Dialog_info)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(50, 420, 524, 33))
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"color: white;\n"
            "font-size: 20pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_7 = QLabel(Dialog_info)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 300, 489, 33))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: white;\n"
            "font-size: 20pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_9 = QLabel(Dialog_info)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(75, 340, 551, 70))
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"color: white;\n"
            "font-size: 18pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_9.setWordWrap(True)
        self.label_9.setOpenExternalLinks(False)

        self.retranslateUi(Dialog_info)

        QMetaObject.connectSlotsByName(Dialog_info)

    def retranslateUi(self, Dialog_info):         # Установка русского языка для элементов
        Dialog_info.setWindowTitle(QCoreApplication.translate("Dialog_info", u"Dialog", None))

        self.pushButton_back_to_main.setToolTip(QCoreApplication.translate("Dialog_info", u"<html><head/><body><p>"
            u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435, \u0447\u0442\u043e\u0431\u044b "
            u"\u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432 \u0433\u043b\u0430\u0432\u043d\u043e\u0435 "
            u"\u043c\u0435\u043d\u044e</p></body></html>", None))

        self.pushButton_back_to_main.setText("")
        self.label_every_audio_to_text_9.setText("")
        self.label_every_audio_to_text_10.setText("")
        self.label_every_audio_to_text_11.setText("")
        self.label_every_audio_to_text_12.setText("")
        self.label_every_audio_to_text_13.setText("")
        self.label_every_audio_to_text_14.setText("")
        self.label_every_audio_to_text_15.setText("")
        self.label_every_audio_to_text_16.setText("")
        self.label_every_audio_to_text_17.setText("")
        self.label_every_audio_to_text_18.setText("")

        self.label_main_label_info.setText(QCoreApplication.translate("Dialog_info",
            u"         \u041e\u0442 \u0437\u0432\u0443\u043a\u0430 \u043a \u0442\u0435\u043a\u0441\u0442\u0443: "
            u"\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435 ", None))

        self.label_every_audio_to_text_8.setText("")

        self.label_6.setToolTip(QCoreApplication.translate("Dialog_info",
            u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))

        self.label_6.setText(QCoreApplication.translate("Dialog_info",
            u"                                \u0427\u0442\u043e \u0443\u043c\u0435\u0435\u0442 "
            u"\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430?", None))

        self.label_8.setText(QCoreApplication.translate("Dialog_info",
            u"<html><head/><body><p align=\"justify\">Программа &quot;AudioToText&quot; позволит вам легко превратить "
            u"<span style=\" font-weight:700;\">аудио</span> и <span style=\" font-weight:700;\">видео в "
            u"</span><span style=\" font-weight:700; text-decoration: underline;\">текст"
            u"</span>: просто диктуйте свои слова в микрофон и получите текст.</p></body></html>", None))

        self.label_10.setToolTip(QCoreApplication.translate("Dialog_info",
            u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))

        self.label_10.setText(QCoreApplication.translate("Dialog_info",
            u"                                \u041a\u0442\u043e "
            u"\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a?", None))

        self.label_11.setText(QCoreApplication.translate("Dialog_info",
            u"<html><head/><body><p> \u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a - "
            u"\u0441\u0442\u0443\u0434\u0435\u043d\u0442 \u0412\u043e\u043b\u0433\u0413\u0422\u0423 "
            u"\u0421\u0430\u043c\u043e\u0440\u043e\u043a\u043e\u0432 "
            u"\u041d\u0438\u043a\u043e\u043b\u0430\u0439.</p></body></html>", None))

        self.label_13.setText(QCoreApplication.translate("Dialog_info",
            u"<html><head/><body><p align=\"justify\">" 
            u"\u0410\u0443\u0434\u0438\u043e: MP3, FLAC, WAV, AAC, VOC, WMA, ALAC;</p>" u"<p align=\"justify\">"
            u"\u0412\u0438\u0434\u0435\u043e: MP4, AVI, MOV, WMV, MKV, FLV.</p>" u"</body></html>", None))

        self.label_12.setToolTip(QCoreApplication.translate("Dialog_info",
            u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))

        self.label_12.setText(QCoreApplication.translate("Dialog_info",
            u"                                \u041a\u0430\u043a\u0438\u0435 "
            u"\u0444\u043e\u0440\u043c\u0430\u0442\u044b "
            u"\u043f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u0442?", None))

        self.label_7.setToolTip(QCoreApplication.translate("Dialog_info",
            u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))

        self.label_7.setText(QCoreApplication.translate("Dialog_info",
            u"                                \u041a\u0430\u043a\u0430\u044f \u043c\u043e\u0434\u0435\u043b\u044c "
            u"\u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f?", None))

        self.label_9.setText(QCoreApplication.translate("Dialog_info",
            u"<html><head/><body><p align=\"justify\">Используется модель <span style=\" font-weight:700;\">"
            u"vosk-ru-0.22</span>, обученная на русском языке.</p></body></html>", None))