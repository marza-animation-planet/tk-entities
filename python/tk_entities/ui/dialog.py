# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
#      by: pyside-uic 0.2.13 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCore, QtWidgets
from . import resources_rc

class SearchWidget(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super(SearchWidget, self).__init__(parent=parent)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(702, 625)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ent_vlay = QtWidgets.QVBoxLayout()
        self.ent_vlay.setObjectName("ent_vlay")
        self.ent_label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ent_label.sizePolicy().hasHeightForWidth())
        self.ent_label.setSizePolicy(sizePolicy)
        self.ent_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ent_label.setObjectName("ent_label")
        self.ent_vlay.addWidget(self.ent_label)
        self.ent_search = SearchWidget(Dialog)
        self.ent_search.setBaseSize(QtCore.QSize(0, 0))
        self.ent_search.setObjectName("ent_search")
        self.ent_vlay.addWidget(self.ent_search)
        self.ent_listWidget = QtWidgets.QListWidget(Dialog)
        self.ent_listWidget.setObjectName("ent_listWidget")
        self.ent_vlay.addWidget(self.ent_listWidget)
        self.ent_vlay.setStretch(2, 1)
        self.horizontalLayout.addLayout(self.ent_vlay)
        self.fld_vlay = QtWidgets.QVBoxLayout()
        self.fld_vlay.setObjectName("fld_vlay")
        self.fld_label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fld_label.sizePolicy().hasHeightForWidth())
        self.fld_label.setSizePolicy(sizePolicy)
        self.fld_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fld_label.setObjectName("fld_label")
        self.fld_vlay.addWidget(self.fld_label)
        self.fld_search = SearchWidget(Dialog)
        self.fld_search.setObjectName("fld_search")
        self.fld_vlay.addWidget(self.fld_search)
        self.fld_listWidget = QtWidgets.QListWidget(Dialog)
        self.fld_listWidget.setObjectName("fld_listWidget")
        self.fld_vlay.addWidget(self.fld_listWidget)
        self.fld_vlay.setStretch(2, 1)
        self.horizontalLayout.addLayout(self.fld_vlay)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Shotgun Entity Browser", None))
        self.ent_label.setText(QtWidgets.QApplication.translate("Dialog", "Entities", None))
        self.fld_label.setText(QtWidgets.QApplication.translate("Dialog", "Fields", None))
