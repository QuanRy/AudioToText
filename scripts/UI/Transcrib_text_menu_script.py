# -*- coding: utf-8 -*-

# ---------------------------------------------- БИБЛИОТЕКИ ------------------------------------------------------------
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget)
# ----------------------------------------------------------------------------------------------------------------------

class Ui_Dialog_audio_file_to_text(object):
    """
        Класс Ui_Dialog_audio_file_to_text представляет окно для работы с аудио / видео файлами и их преобразования в текст.

        Атрибуты экземпляра:
        --------------------
        lineEdit_way_open_file : QLineEdit
            Поле для ввода пути к файлу, который нужно преобразовать в текст.

        pushButton_choose_file : QPushButton
            Кнопка для выбора аудиофайла для преобразования.

        label_audio_to_text_slogan : QLabel
            Метка, отображающая слоган "Аудио или видео в текст - легко!".

        label_file_to_translate_info : QLabel
            Метка с информацией о том, какой файл необходимо преобразовать в текст.

        lineEdit_way_save_file : QLineEdit
            Поле для ввода пути, куда сохранить текстовый файл с результатом преобразования.

        label_save_as__info : QLabel
            Метка с информацией о том, куда будет сохранен текстовый файл.

        pushButton_save_files : QPushButton
            Кнопка для сохранения текстового файла.

        textEdit_field_to_text : QTextEdit
            Поле для отображения текста, полученного в результате преобразования аудиофайла.

        pushButton_back_to_main : QPushButton
            Кнопка для возврата в главное меню.

        Методы:
        -------
        setupUi(self, Dialog_audio_file_to_text):
            Настраивает пользовательский интерфейс диалогового окна.

        retranslateUi(self, Dialog_dict_audio):
            Устанавливает текст для элементов интерфейса на русском языке.
        """

    def setupUi(self, Dialog_audio_file_to_text):
        if not Dialog_audio_file_to_text.objectName():
            Dialog_audio_file_to_text.setObjectName(u"Dialog_audio_file_to_text")
        Dialog_audio_file_to_text.resize(760, 671)
        Dialog_audio_file_to_text.setMinimumSize(QSize(760, 671))
        Dialog_audio_file_to_text.setMaximumSize(QSize(760, 671))
        Dialog_audio_file_to_text.setStyleSheet(u"background-color: qlineargradient(spread:pad, "
            u"x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 "
            u"rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
            "font-family: Corbel;")
        Dialog_audio_file_to_text.setSizeGripEnabled(False)
        Dialog_audio_file_to_text.setModal(False)
        self.lineEdit_way_open_file = QLineEdit(Dialog_audio_file_to_text)
        self.lineEdit_way_open_file.setObjectName(u"lineEdit_way_open_file")
        self.lineEdit_way_open_file.setGeometry(QRect(60, 110, 421, 41))
        self.lineEdit_way_open_file.setAcceptDrops(True)
        self.lineEdit_way_open_file.setStyleSheet(u"color: rgba(255, 255, 255, 200); /* "
            u"\u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0431\u0435\u043b\u044b\u0439 "
            u"\u0442\u0435\u043a\u0441\u0442 */\n"
            "font-size: 12pt;\n"
            "background-color: rgba(255, 255, 255, 30);\n"
            "border: 1px solid rgba(255, 255, 255, 40);\n"
            "border-radius: 20px;\n"
            "width: 230px;\n"
            "height: 50px;\n"
            "")
        self.lineEdit_way_open_file.setFrame(True)
        self.pushButton_choose_file = QPushButton(Dialog_audio_file_to_text)
        self.pushButton_choose_file.setObjectName(u"pushButton_choose_file")
        self.pushButton_choose_file.setGeometry(QRect(500, 110, 201, 41))
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
        self.label_audio_to_text_slogan = QLabel(Dialog_audio_file_to_text)
        self.label_audio_to_text_slogan.setObjectName(u"label_audio_to_text_slogan")
        self.label_audio_to_text_slogan.setGeometry(QRect(140, 30, 481, 31))
        font = QFont()
        font.setFamilies([u"Corbel"])
        font.setPointSize(25)
        font.setBold(True)
        self.label_audio_to_text_slogan.setFont(font)
        self.label_audio_to_text_slogan.setStyleSheet(u"color: white;\n"
            "font-weight: bold;\n"
            "font-size: 25pt;\n"
            "background-color: none;\n"
            "border: none; ")
        self.label_audio_to_text_slogan.setWordWrap(True)
        self.label_audio_to_text_slogan.setOpenExternalLinks(False)
        self.label_file_to_translate_info = QLabel(Dialog_audio_file_to_text)
        self.label_file_to_translate_info.setObjectName(u"label_file_to_translate_info")
        self.label_file_to_translate_info.setGeometry(QRect(80, 80, 391, 31))
        font1 = QFont()
        font1.setFamilies([u"Corbel"])
        font1.setPointSize(14)
        self.label_file_to_translate_info.setFont(font1)
        self.label_file_to_translate_info.setStyleSheet(u"color: white;\n"
            "font-size: 14pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.lineEdit_way_save_file = QLineEdit(Dialog_audio_file_to_text)
        self.lineEdit_way_save_file.setObjectName(u"lineEdit_way_save_file")
        self.lineEdit_way_save_file.setGeometry(QRect(60, 600, 421, 41))
        self.lineEdit_way_save_file.setAcceptDrops(True)
        self.lineEdit_way_save_file.setStyleSheet(u"color: rgba(255, 255, 255, 200); /* "
            u"\u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0431\u0435\u043b\u044b\u0439 "
            u"\u0442\u0435\u043a\u0441\u0442 */\n"
            "font-size: 12pt;\n"
            "background-color: rgba(255, 255, 255, 30);\n"
            "border: 1px solid rgba(255, 255, 255, 40);\n"
            "border-radius: 20px;\n"
            "width: 230px;\n"
            "height: 50px;\n"
            "")
        self.lineEdit_way_save_file.setFrame(True)
        self.label_save_as__info = QLabel(Dialog_audio_file_to_text)
        self.label_save_as__info.setObjectName(u"label_save_as__info")
        self.label_save_as__info.setGeometry(QRect(80, 570, 391, 31))
        self.label_save_as__info.setFont(font1)
        self.label_save_as__info.setStyleSheet(u"color: white;\n"
            "font-size: 14pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.pushButton_save_files = QPushButton(Dialog_audio_file_to_text)
        self.pushButton_save_files.setObjectName(u"pushButton_save_files")
        self.pushButton_save_files.setGeometry(QRect(500, 600, 201, 41))
        self.pushButton_save_files.setStyleSheet(u"\n"
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
        icon1.addFile(u"../icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_save_files.setIcon(icon1)
        self.pushButton_save_files.setIconSize(QSize(25, 25))
        self.textEdit_field_to_text = QTextEdit(Dialog_audio_file_to_text)
        self.textEdit_field_to_text.setObjectName(u"textEdit_field_to_text")
        self.textEdit_field_to_text.setGeometry(QRect(60, 170, 641, 391))
        self.textEdit_field_to_text.setStyleSheet(u"""
            QTextEdit {
                color: rgba(255, 255, 255, 200); 
                font-size: 12pt;
                background-color: rgba(255, 255, 255, 30);
                border: 1px solid rgba(255, 255, 255, 40);
                border-radius: 20px;
            }
            QScrollBar:vertical {          /* Редактирует скролбар */
                width: 25px;
                background: rgba(255, 255, 255, 30);                           
                border: 1px solid rgba(255, 255, 255, 40);
                border-radius: 20px;
            }
            QScrollBar::handle:vertical {
                min-height: 30px;
                background: rgba(255, 255, 255, 30);                            
                border: 1px solid rgba(255, 255, 255, 40);
                border-radius: 20px;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical  {
                background-color: rgba(255, 255, 255, 110);                    
            }
            """)

        self.pushButton_back_to_main = QPushButton(Dialog_audio_file_to_text)
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
        icon2 = QIcon()
        icon2.addFile(u"../icons/back_arrow.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_back_to_main.setIcon(icon2)
        self.pushButton_back_to_main.setIconSize(QSize(35, 35))
        self.label_every_audio_to_text_7 = QLabel(Dialog_audio_file_to_text)
        self.label_every_audio_to_text_7.setObjectName(u"label_every_audio_to_text_7")
        self.label_every_audio_to_text_7.setGeometry(QRect(620, 20, 41, 51))
        self.label_every_audio_to_text_7.setFont(font1)
        self.label_every_audio_to_text_7.setStyleSheet(u"color: white;\n"
            "font-size: 14pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            "")
        self.label_every_audio_to_text_7.setPixmap(QPixmap(u"../icons/img/smiles/audio_to_text_45.png"))
        self.label_every_audio_to_text_7.setWordWrap(True)
        self.label_every_audio_to_text_7.setOpenExternalLinks(False)

        self.retranslateUi(Dialog_audio_file_to_text)

        QMetaObject.connectSlotsByName(Dialog_audio_file_to_text)

    def retranslateUi(self, Dialog_audio_file_to_text):          # Установка текста для элементов UI на русский язык
        Dialog_audio_file_to_text.setWindowTitle(QCoreApplication.translate("Dialog_audio_file_to_text", u"Dialog", None))

        self.lineEdit_way_open_file.setToolTip(QCoreApplication.translate("Dialog_audio_file_to_text",
            u"<html><head/><body><p>\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b, "
            u"\u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0445\u043e\u0442\u0438\u0442\u0435 "
            u"\u043f\u0435\u0440\u0435\u0432\u0435\u0441\u0442\u0438 \u0432 "
            u"\u0442\u0435\u043a\u0441\u0442</p></body></html>", None))

        self.lineEdit_way_open_file.setText(QCoreApplication.translate("Dialog_audio_file_to_text",
            u"    \u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b", None))

        self.pushButton_choose_file.setToolTip(QCoreApplication.translate("Dialog_audio_file_to_text",
            u"<html><head/><body><p>\u041d\u0430\u0436\u043c\u0438\u0442\u0435, \u0447\u0442\u043e\u0431\u044b "
            u"\u0437\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043f\u0440\u043e\u0446\u0435\u0441\u0441 "
            u"\u043f\u0435\u0440\u0435\u0432\u043e\u0434\u0430 \u0432\u0430\u0448\u0435\u0433\u043e "
            u"\u0444\u0430\u0439\u043b\u0430 \u0432 \u0442\u0435\u043a\u0441\u0442</p></body></html>", None))

        self.pushButton_choose_file.setText(QCoreApplication.translate("Dialog_audio_file_to_text",
            u" \u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.label_audio_to_text_slogan.setText(QCoreApplication.translate("Dialog_audio_file_to_text",
            u"\u0410\u0443\u0434\u0438\u043e \u0438\u043b\u0438 \u0432\u0438\u0434\u0435\u043e \u0432 "
            u"\u0442\u0435\u043a\u0441\u0442 - \u043b\u0435\u0433\u043a\u043e!", None))
        self.label_file_to_translate_info.setText(QCoreApplication.translate("Dialog_audio_file_to_text",
            u"\u0424\u0430\u0439\u043b \u043a\u043e\u0442\u043e\u0440\u044b\u0439 "
            u"\u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e "
            u"\u043f\u0435\u0440\u0435\u0432\u0435\u0441\u0442\u0438 \u0432 \u0442\u0435\u043a\u0441\u0442:", None))

        self.lineEdit_way_save_file.setToolTip(QCoreApplication.translate("Dialog_audio_file_to_text",
            u"<html><head/><body><p>\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435, \u043a\u0443\u0434\u0430 "
            u"\u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c "
            u"\u0442\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u0439 \u0444\u0430\u0439\u043b "
            u"\u043f\u0435\u0440\u0435\u0432\u043e\u0434\u0430</p></body></html>", None))

        self.lineEdit_way_save_file.setText(QCoreApplication.translate("Dialog_audio_file_to_text",
            u"    \u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b", None))
        self.label_save_as__info.setText(QCoreApplication.translate("Dialog_audio_file_to_text",
            u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c "
            u"\u043f\u0435\u0440\u0435\u0432\u043e\u0434 \u0432:", None))

        self.pushButton_save_files.setToolTip(QCoreApplication.translate("Dialog_audio_file_to_text",
            u"<html><head/><body><p>\u041d\u0430\u0436\u043c\u0438\u0442\u0435, \u0447\u0442\u043e\u0431\u044b "
            u"\u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043f\u0435\u0440\u0435\u0432\u043e\u0434 "
            u"\u0432\u0430\u0448\u0435\u0433\u043e \u0444\u0430\u0439\u043b\u0430 </p></body></html>", None))

        self.pushButton_save_files.setText(QCoreApplication.translate("Dialog_audio_file_to_text",
            u" \u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))

        self.textEdit_field_to_text.setToolTip(QCoreApplication.translate("Dialog_audio_file_to_text",
            u"<html><head/><body><p align=\"justify\">\u0417\u0434\u0435\u0441\u044c "
            u"\u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u0442\u0441\u044f "
            u"\u0442\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u0439 \u043f\u0435\u0440\u0435\u0432\u043e\u0434 "
            u"\u0432\u0430\u0448\u0435\u0433\u043e \u0430\u0443\u0434\u0438\u043e</p></body></html>", None))

        self.textEdit_field_to_text.setHtml(QCoreApplication.translate("Dialog_audio_file_to_text",
            u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "hr { height: 1px; border-width: 0; }\n"
            "li.unchecked::marker { content: \"\\2610\"; }\n"
            "li.checked::marker { content: \"\\2612\"; }\n"
            "</style></head><body style=\" font-family:'Corbel'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; "
            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))

        self.pushButton_back_to_main.setToolTip(QCoreApplication.translate("Dialog_audio_file_to_text",
            u"<html><head/><body><p>\u041d\u0430\u0436\u043c\u0438\u0442\u0435, \u0447\u0442\u043e\u0431\u044b "
            u"\u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432 "
            u"\u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e</p></body></html>", None))

        self.pushButton_back_to_main.setText("")
        self.label_every_audio_to_text_7.setText("")