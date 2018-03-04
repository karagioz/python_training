# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_edit_group_name(app):
    app.group.ensure_group_created(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="new_name", header="new_header", footer="new_footer")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
