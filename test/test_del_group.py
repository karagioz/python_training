# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):
    app.group.ensure_group_created(Group(name="test"))
    app.group.delete_first_group()
