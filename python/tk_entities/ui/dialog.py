# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
#      by: pyside-uic 0.2.13 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCore, QtWidgets, QtGui
from . import resources_rc
import qjsonmodel
import os

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
        iconpath = os.path.join(os.path.dirname(__file__), "sg_logo.png")
        if os.path.isfile(iconpath):
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(iconpath), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            Dialog.setWindowIcon(icon)

        # Top layout
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Entities column layout
        self.ent_split = QtWidgets.QSplitter(QtCore.Qt.Vertical, parent=Dialog)

        self.ent_lwidget = QtWidgets.QWidget(self.ent_split)

        # Label + display name toggle
        self.ent_label = QtWidgets.QLabel(self.ent_lwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ent_label.sizePolicy().hasHeightForWidth())
        self.ent_label.setSizePolicy(sizePolicy)
        self.ent_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ent_label.setObjectName("ent_label")
        self.ent_code = QtWidgets.QCheckBox("Show Displayed Names", parent=self.ent_lwidget)

        lbllay = QtWidgets.QHBoxLayout()
        lbllay.setContentsMargins(0, 0, 0, 0)
        lbllay.setSpacing(5)
        lbllay.addWidget(self.ent_label, 1)
        lbllay.addWidget(self.ent_code, 0)

        # Field + regexp toogle
        self.ent_search = SearchWidget(self.ent_lwidget)
        self.ent_search.setBaseSize(QtCore.QSize(0, 0))
        self.ent_search.setObjectName("ent_search")
        self.ent_regexp = QtWidgets.QCheckBox("As Regexp", parent=self.ent_lwidget)

        fldlay = QtWidgets.QHBoxLayout()
        fldlay.setContentsMargins(0, 0, 0, 0)
        fldlay.setSpacing(5)
        fldlay.addWidget(self.ent_search, 1)
        fldlay.addWidget(self.ent_regexp, 0)

        # List
        self.ent_listWidget = QtWidgets.QListWidget(self.ent_lwidget)
        self.ent_listWidget.setObjectName("ent_listWidget")

        self.ent_llay = QtWidgets.QVBoxLayout(self.ent_lwidget)
        self.ent_llay.setObjectName("ent_llay")
        self.ent_llay.addLayout(lbllay)
        self.ent_llay.addLayout(fldlay)
        self.ent_llay.addWidget(self.ent_listWidget)
        self.ent_llay.setStretch(2, 1)

        # Info
        self.ent_iwidget = QtWidgets.QWidget(self.ent_split)

        self.ent_ilabel = QtWidgets.QLabel(self.ent_iwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ent_ilabel.sizePolicy().hasHeightForWidth())
        self.ent_ilabel.setSizePolicy(sizePolicy)
        self.ent_ilabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ent_ilabel.setObjectName("ent_ilabel")

        self.ent_info = QtWidgets.QTreeView(self.ent_iwidget)
        #
        self.ent_model = ROJsonModel()
        self.ent_info.setModel(self.ent_model)

        self.ent_ilay = QtWidgets.QVBoxLayout(self.ent_iwidget)
        self.ent_ilay.setContentsMargins(0, 0, 0, 0)
        self.ent_ilay.setSpacing(5)
        self.ent_ilay.addWidget(self.ent_ilabel, 0)
        self.ent_ilay.addWidget(self.ent_info, 1)

        self.horizontalLayout.addWidget(self.ent_split, 1)

        # Fields column layout
        self.fld_split = QtWidgets.QSplitter(QtCore.Qt.Vertical, parent=Dialog)

        self.fld_lwidget = QtWidgets.QWidget(self.fld_split)

        # Label + display name toggle
        self.fld_label = QtWidgets.QLabel(self.fld_lwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fld_label.sizePolicy().hasHeightForWidth())
        self.fld_label.setSizePolicy(sizePolicy)
        self.fld_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fld_label.setObjectName("fld_label")
        self.fld_code = QtWidgets.QCheckBox("Show Displayed Names", parent=self.fld_lwidget)

        lbllay = QtWidgets.QHBoxLayout()
        lbllay.setContentsMargins(0, 0, 0, 0)
        lbllay.setSpacing(5)
        lbllay.addWidget(self.fld_label, 1)
        lbllay.addWidget(self.fld_code, 0)

        # Field + regex toggle
        self.fld_search = SearchWidget(self.fld_lwidget)
        self.fld_search.setObjectName("fld_search")
        self.fld_regexp = QtWidgets.QCheckBox("As Regexp", parent=self.fld_lwidget)

        fldlay = QtWidgets.QHBoxLayout()
        fldlay.setContentsMargins(0, 0, 0, 0)
        fldlay.setSpacing(5)
        fldlay.addWidget(self.fld_search, 1)
        fldlay.addWidget(self.fld_regexp, 0)

        # List
        self.fld_listWidget = QtWidgets.QListWidget(self.fld_lwidget)
        self.fld_listWidget.setObjectName("fld_listWidget")

        self.fld_llay = QtWidgets.QVBoxLayout(self.fld_lwidget)
        self.fld_llay.setContentsMargins(0, 0, 0, 0)
        self.fld_llay.setSpacing(5)
        self.fld_llay.addLayout(lbllay)
        self.fld_llay.addLayout(fldlay)
        self.fld_llay.addWidget(self.fld_listWidget)
        self.fld_llay.setStretch(2, 1)

        # Info
        self.fld_iwidget = QtWidgets.QWidget(self.fld_split)

        self.fld_ilabel = QtWidgets.QLabel(self.fld_iwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fld_ilabel.sizePolicy().hasHeightForWidth())
        self.fld_ilabel.setSizePolicy(sizePolicy)
        self.fld_ilabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fld_ilabel.setObjectName("fld_ilabel")

        self.fld_info = QtWidgets.QTreeView(self.fld_iwidget)
        self.fld_model = ROJsonModel()
        self.fld_info.setModel(self.fld_model)

        self.fld_ilay = QtWidgets.QVBoxLayout(self.fld_iwidget)
        self.fld_ilay.setContentsMargins(0, 0, 0, 0)
        self.fld_ilay.setSpacing(5)
        self.fld_ilay.addWidget(self.fld_ilabel, 0)
        self.fld_ilay.addWidget(self.fld_info, 1)

        self.horizontalLayout.addWidget(self.fld_split, 1)

        self.ent_split.setSizes([500, 100])
        self.ent_split.setStretchFactor(0, 1)
        self.fld_split.setSizes([300, 300])
        self.fld_split.setStretchFactor(0, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Shotgun Entity Browser", None))
        self.ent_label.setText(QtWidgets.QApplication.translate("Dialog", "Entities", None))
        self.ent_ilabel.setText(QtWidgets.QApplication.translate("Dialog", "Entitiy  Info", None))
        self.fld_label.setText(QtWidgets.QApplication.translate("Dialog", "Fields", None))
        self.fld_ilabel.setText(QtWidgets.QApplication.translate("Dialog", "Field Info", None))
