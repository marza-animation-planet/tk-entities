# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import os
import sys
import threading
import shotgun_api3


from Qt import QtCore, QtWidgets
from .ui.dialog import Ui_Dialog


class AppDialog(QtWidgets.QDialog):
    """
    Main application dialog window
    """

    def __init__(self, project, url, script, key, parent=None):
        """
        Constructor
        """
        # first, call the base class and let it do its thing.
        super(AppDialog, self).__init__(parent)

        # now load in the UI that was created in the UI designer
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ent_filter = ""
        self.fld_filter = ""

        self._proj = project
        self._sg = shotgun_api3.Shotgun(url, script, key)

        ent_list_widget = self.ui.ent_listWidget
        fld_list_widget = self.ui.fld_listWidget

        ent_search = self.ui.ent_search
        fld_search = self.ui.fld_search

        # TODO
        # setup this properties in .ui files
        single_selection = QtWidgets.QAbstractItemView.SingleSelection
        ent_list_widget.setSelectionMode(single_selection)
        fld_list_widget.setSelectionMode(single_selection)
        # ent_list_widget.setStyleSheet("QListWidget {font: 20px;}")

        # connect signals
        ent_search.textEdited.connect(self._on_ent_search_edited)
        fld_search.textEdited.connect(self._on_fld_search_edited)

        ent_list_widget.itemSelectionChanged.connect(self.disp_fields)

        # display widgets
        self.disp_entities()
        self.disp_fields()

        print("Launching Entities Application...")

        return

    def _on_ent_search_edited(self, text):
        """
        Update entity text filter value 
        """
        self.ent_filter = text
        self.disp_entities()
        return

    def _on_fld_search_edited(self, text):
        """
        Update field text filter value 
        """
        self.fld_filter = text
        self.disp_fields()
        return

    def disp_entities(self):
        """
        Display entities
        """
        ent_list_widget = self.ui.ent_listWidget
        item_role = "entity"

        # clear list
        ent_list_widget.clear()

        entities = self._sg.schema_entity_read(self._proj)
        entity_names = entities.keys()

        for entity_name in sorted(entity_names):
            if self.ent_filter:
                if not entity_name.lower().startswith(self.ent_filter.lower()):
                    continue
            item = QtWidgets.QListWidgetItem(entity_name)
            item.setData(QtCore.Qt.UserRole, item_role)
            ent_list_widget.addItem(item)
            # print("{} = {}".format(entity_name, entities[entity_name]))
        return

    def disp_fields(self):
        """
        Display entities
        """
        fld_list_widget = self.ui.fld_listWidget
        ent_list_widget = self.ui.ent_listWidget
        item_role = "field"

        # clear list
        fld_list_widget.clear()

        entity_item = ent_list_widget.currentItem()
        if not entity_item:
            return

        entity_name = entity_item.text()
        fields = self._sg.schema_field_read(entity_name, None, self._proj)
        field_names = fields.keys()

        # print '*' * 40
        # print entity_name.center(40)
        # print '*' * 40
        for field_name in sorted(field_names):
            if self.fld_filter:
                if not field_name.lower().startswith(self.fld_filter.lower()):
                    continue
            item = QtWidgets.QListWidgetItem(field_name)
            item.setData(QtCore.Qt.UserRole, item_role)
            fld_list_widget.addItem(item)
            # print("{} = {}".format(field_name, fields[field_name]))
        return

