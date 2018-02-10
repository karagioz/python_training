# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group_name(app):
    app.group.edit_first_group(Group(name="new_name"))


def test_edit_group_header(app):
    app.group.edit_first_group(Group(header="new_header"))


def test_edit_group_footer(app):
    app.group.edit_first_group(Group(footer="new_footer"))
