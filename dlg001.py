# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '001.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(384, 274)
        Dialog.setMinimumSize(QtCore.QSize(384, 255))
        Dialog.setMaximumSize(QtCore.QSize(384, 600))
        Dialog.setStyleSheet("background-color: rgb(43, 43, 43);\n"
"color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_label = QtWidgets.QLabel(Dialog)
        self.title_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.language_label = QtWidgets.QLabel(Dialog)
        self.language_label.setMaximumSize(QtCore.QSize(16777215, 16))
        self.language_label.setObjectName("language_label")
        self.verticalLayout_2.addWidget(self.language_label)
        self.language_combo = QtWidgets.QComboBox(Dialog)
        self.language_combo.setMaximumSize(QtCore.QSize(16777215, 25))
        self.language_combo.setStyleSheet("border-color: rgb(255, 119, 0);\n"
"selection-background-color: rgb(161, 75, 0);")
        self.language_combo.setObjectName("language_combo")
        self.verticalLayout_2.addWidget(self.language_combo)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.profiles_name = QtWidgets.QLabel(Dialog)
        self.profiles_name.setMaximumSize(QtCore.QSize(16777215, 16))
        self.profiles_name.setObjectName("profiles_name")
        self.verticalLayout.addWidget(self.profiles_name)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setStyleSheet("border-color: rgb(255, 119, 0);\n"
"selection-background-color: rgb(161, 75, 0);")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(29)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_profile_btn = QtWidgets.QPushButton(Dialog)
        self.add_profile_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.add_profile_btn.setStyleSheet("border-color: rgb(255, 119, 0);\n"
"selection-background-color: rgb(255, 119, 0);")
        self.add_profile_btn.setObjectName("add_profile_btn")
        self.horizontalLayout.addWidget(self.add_profile_btn)
        self.connect_btn = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connect_btn.sizePolicy().hasHeightForWidth())
        self.connect_btn.setSizePolicy(sizePolicy)
        self.connect_btn.setMinimumSize(QtCore.QSize(106, 0))
        self.connect_btn.setStyleSheet("border-color: rgb(255, 119, 0);\n"
"selection-background-color: rgb(255, 119, 0);")
        self.connect_btn.setObjectName("connect_btn")
        self.horizontalLayout.addWidget(self.connect_btn)
        self.change_profile_btn = QtWidgets.QPushButton(Dialog)
        self.change_profile_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.change_profile_btn.setStyleSheet("border-color: rgb(255, 119, 0);\n"
"selection-background-color: rgb(255, 119, 0);")
        self.change_profile_btn.setObjectName("change_profile_btn")
        self.horizontalLayout.addWidget(self.change_profile_btn)
        self.del_profile_btn = QtWidgets.QPushButton(Dialog)
        self.del_profile_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.del_profile_btn.setStyleSheet("border-color: rgb(255, 119, 0);\n"
"selection-background-color: rgb(255, 119, 0);")
        self.del_profile_btn.setObjectName("del_profile_btn")
        self.horizontalLayout.addWidget(self.del_profile_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStyleSheet("selection-background-color: rgb(255, 119, 0);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tinelix IRC Client"))
        self.title_label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Первоначальная настройка клиента</span></p></body></html>"))
        self.language_label.setText(_translate("Dialog", "Язык (Language):"))
        self.profiles_name.setText(_translate("Dialog", "Профили:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Профиль"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Сервер/порт"))
        self.add_profile_btn.setText(_translate("Dialog", "Добавить"))
        self.connect_btn.setText(_translate("Dialog", "Подключиться"))
        self.change_profile_btn.setText(_translate("Dialog", "Настроить"))
        self.del_profile_btn.setText(_translate("Dialog", "Удалить"))
