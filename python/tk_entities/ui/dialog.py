# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
#      by: pyside-uic 0.2.13 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCore, QtWidgets
from . import resources_rc
import qjsonmodel

class SearchWidget(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super(SearchWidget, self).__init__(parent=parent)

class ROJsonModel(qjsonmodel.QJsonModel):
    def __init__(self, parent=None):
        super(ROJsonModel, self).__init__(parent)

    def flags(self, index):
        flags = super(ROJsonModel, self).flags(index)
        return flags & ~QtCore.Qt.ItemIsEditable

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(702, 625)

        # Top layout
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Entities column layout
        self.ent_vlay = QtWidgets.QVBoxLayout()
        self.ent_vlay.setObjectName("ent_vlay")

        # Label + display name toggle
        lbllay = QtWidgets.QHBoxLayout()
        lbllay.setContentsMargins(0, 0, 0, 0)
        lbllay.setSpacing(5)
        self.ent_label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ent_label.sizePolicy().hasHeightForWidth())
        self.ent_label.setSizePolicy(sizePolicy)
        self.ent_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ent_label.setObjectName("ent_label")
        self.ent_code = QtWidgets.QCheckBox("Show Displayed Names", parent=Dialog)
        lbllay.addWidget(self.ent_label, 1)
        lbllay.addWidget(self.ent_code, 0)
        #self.ent_vlay.addWidget(self.ent_label)
        self.ent_vlay.addLayout(lbllay)

        # Field + regexp toogle
        fldlay = QtWidgets.QHBoxLayout()
        fldlay.setContentsMargins(0, 0, 0, 0)
        fldlay.setSpacing(5)
        self.ent_search = SearchWidget(Dialog)
        self.ent_search.setBaseSize(QtCore.QSize(0, 0))
        self.ent_search.setObjectName("ent_search")
        self.ent_regexp = QtWidgets.QCheckBox("As Regexp", parent=Dialog)
        fldlay.addWidget(self.ent_search, 1)
        fldlay.addWidget(self.ent_regexp, 0)
        #self.ent_vlay.addWidget(self.ent_search)
        self.ent_vlay.addLayout(fldlay)

        # List
        self.ent_listWidget = QtWidgets.QListWidget(Dialog)
        self.ent_listWidget.setObjectName("ent_listWidget")
        self.ent_vlay.addWidget(self.ent_listWidget)

        # Info
        self.ent_ilabel = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ent_ilabel.sizePolicy().hasHeightForWidth())
        self.ent_ilabel.setSizePolicy(sizePolicy)
        self.ent_ilabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ent_ilabel.setObjectName("ent_ilabel")
        self.ent_vlay.addWidget(self.ent_ilabel)

        self.ent_info = QtWidgets.QTreeView(Dialog)
        self.ent_model = ROJsonModel()
        self.ent_info.setModel(self.ent_model)
        self.ent_vlay.addWidget(self.ent_info)

        self.ent_vlay.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.ent_vlay)

        # Fields column layout
        self.fld_vlay = QtWidgets.QVBoxLayout()
        self.fld_vlay.setObjectName("fld_vlay")

        # Label + display name toggle
        lbllay = QtWidgets.QHBoxLayout()
        lbllay.setContentsMargins(0, 0, 0, 0)
        lbllay.setSpacing(5)
        self.fld_label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fld_label.sizePolicy().hasHeightForWidth())
        self.fld_label.setSizePolicy(sizePolicy)
        self.fld_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fld_label.setObjectName("fld_label")
        self.fld_code = QtWidgets.QCheckBox("Show Displayed Names", parent=Dialog)
        lbllay.addWidget(self.fld_label, 1)
        lbllay.addWidget(self.fld_code, 0)
        #self.fld_vlay.addWidget(self.fld_label)
        self.fld_vlay.addLayout(lbllay)

        # Field + regex toggle
        fldlay = QtWidgets.QHBoxLayout()
        fldlay.setContentsMargins(0, 0, 0, 0)
        fldlay.setSpacing(5)
        self.fld_search = SearchWidget(Dialog)
        self.fld_search.setObjectName("fld_search")
        self.fld_regexp = QtWidgets.QCheckBox("As Regexp", parent=Dialog)
        fldlay.addWidget(self.fld_search, 1)
        fldlay.addWidget(self.fld_regexp, 0)
        #self.fld_vlay.addWidget(self.fld_search)
        self.fld_vlay.addLayout(fldlay)

        # List
        self.fld_listWidget = QtWidgets.QListWidget(Dialog)
        self.fld_listWidget.setObjectName("fld_listWidget")
        self.fld_vlay.addWidget(self.fld_listWidget)

        # Info
        self.fld_ilabel = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fld_ilabel.sizePolicy().hasHeightForWidth())
        self.fld_ilabel.setSizePolicy(sizePolicy)
        self.fld_ilabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fld_ilabel.setObjectName("fld_ilabel")
        self.fld_vlay.addWidget(self.fld_ilabel)

        self.fld_info = QtWidgets.QTreeView(Dialog)
        self.fld_model = ROJsonModel()
        self.fld_info.setModel(self.fld_model)
        self.fld_vlay.addWidget(self.fld_info)

        self.fld_vlay.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.fld_vlay)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Shotgun Entity Browser", None))
        self.ent_label.setText(QtWidgets.QApplication.translate("Dialog", "Entities", None))
        self.ent_ilabel.setText(QtWidgets.QApplication.translate("Dialog", "Entitiy  Info", None))
        self.fld_label.setText(QtWidgets.QApplication.translate("Dialog", "Fields", None))
        self.fld_ilabel.setText(QtWidgets.QApplication.translate("Dialog", "Field Info", None))
