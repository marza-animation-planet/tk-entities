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
import fnmatch
import re


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

        print("Launching Entities Application...")
        self._entity_by_code = True
        self._entity_expr = False
        self._field_by_code = True
        self._field_expr = False
        self._init_entities()

        # display widgets
        self.disp_entities()
        self.disp_fields()

    def _value_str(self, val, ljoin="\n", kvjoin=" = "):
        if isinstance(val, (list, set, tuple)):
            return ljoin.join(map(self._value_str, val))
        elif isinstance(val, dict):
            return ljoin.join(map(lambda x: kvjoin.join(map(self._value_str, x)), val.items()))
        elif isinstance(val, basestring):
            return val
        else:
            return repr(val)

    def _init_entities(self):
        self._entities = {}
        self._name_to_entity = {}

        entities = self._sg.schema_entity_read(self._proj)

        for entity_name, entity_info in entities.iteritems():
            name = entity_info.get("name", {})
            if "value" in name:
                self._name_to_entity[name["value"]] = entity_name

            self._entities[entity_name] = None

    def _get_entity_fields(self, entity_name):
        if not entity_name in self._entities:
            # Unknown entity name
            return ({}, {})

        entity = self._entities[entity_name]
        if entity is not None:
            # Entity fields already initialized
            return entity

        fields = {}
        name_to_field = {}

        _fields = self._sg.schema_field_read(entity_name, None, self._proj)
        if not _fields:
            return ({}, {})

        for field_name, field_info in _fields.iteritems():
            info = {}

            name = field_info.get("name", {})
            if "value" in name:
                _name = name["value"]
                info["name"] = _name
                name_to_field[_name] = field_name

            desc = field_info.get("description", {}).get("value", None)
            if desc is not None:
                info["description"] = desc

            edit = field_info.get("editable", {}).get("value", None)
            if edit is not None:
                info["editable"] = edit

            vis = field_info.get("visible", {}).get("value", None)
            if vis is not None:
                info["visible"] = vis

            typ = field_info.get("data_type", {}).get("value", None)
            if typ is not None:
                info["type"] = typ

            props = field_info.get("properties", None)
            if props is not None:
                defval = props.get("default_value", {}).get("value", None)
                if defval is not None:
                    info["default"] = defval

                vtypes = props.get("valid_types", {}).get("value", None)
                if vtypes is not None:
                    info["valid_types"] = vtypes

            fields[field_name] = info

        self._entities[entity_name] = (fields, name_to_field)

        return (fields, name_to_field)

    def _on_ent_search_edited(self, text):
        """
        Update entity text filter value 
        """
        self.ent_filter = text
        self.disp_entities()

    def _on_fld_search_edited(self, text):
        """
        Update field text filter value 
        """
        self.fld_filter = text
        self.disp_fields()

    def disp_entities(self):
        """
        Display entities
        """
        ent_list_widget = self.ui.ent_listWidget
        item_role = "entity"

        # clear list
        ent_list_widget.clear()

        entity_names = (self._entities if self._entity_by_code else self._name_to_entity).keys()

        _flt = self.ent_filter.strip()
        if _flt:
            if self._entity_expr:
                try:
                    _exp = re.compile(_flt, re.IGNORECASE)
                    flt = lambda x: _exp.search(x) is not None
                except:
                    print("Invalid expression: '%s'" % _flt)
                    # Color field in red
                    return
                else:
                    # Don't color field
                    pass
            else:
                _str = _flt.lower()
                flt = lambda x: _str in x.lower()
        else:
            flt = None

        for entity_name in sorted(entity_names):
            if flt and not flt(entity_name):
                continue
            item = QtWidgets.QListWidgetItem(entity_name)
            item.setData(QtCore.Qt.UserRole, item_role)
            ent_list_widget.addItem(item)

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
        entity_fields, name_to_code = self._get_entity_fields(entity_name)
        field_names = (entity_fields if self._field_by_code else name_to_code).keys()

        _flt = self.fld_filter.strip()
        if _flt:
            if self._field_expr:
                try:
                    _exp = re.compile(_flt, re.IGNORECASE)
                    flt = lambda x: _exp.search(x) is not None
                except:
                    print("Invalid expression: '%s'" % _flt)
                    # Color field in red
                    return
                else:
                    # Don't color field
                    pass
            else:
                _str = _flt.lower()
                flt = lambda x: _str in x.lower()
        else:
            flt = None

        for field_name in sorted(field_names):
            if flt and not flt(field_name):
                continue
            item = QtWidgets.QListWidgetItem(field_name)
            item.setData(QtCore.Qt.UserRole, item_role)
            fld_list_widget.addItem(item)

