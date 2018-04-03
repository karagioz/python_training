# -*- coding: utf-8 -*-
from model.group import Group
import random
import pytest


def test_edit_group(app, db, check_ui):
    with pytest.allure.step('Given a non-empty group list'):
        app.group.ensure_group_created(Group(name="test"))
        old_groups = db.get_group_list()
    with pytest.allure.step('Given a random group from the list'):
        old_group = random.choice(old_groups)
    with pytest.allure.step('Given the new group information'):
        new_group = Group(id=old_group.id, name="new_name", header="new_header", footer="new_footer")
    with pytest.allure.step('When I edit the group according to the new group information'):
        app.group.edit_group_by_id(old_group.id, new_group)
    with pytest.allure.step('Then the new group list is equal the old list with the updated group'):
        new_groups = db.get_group_list()
        index = -1
        for g in old_groups:
            if g.id == old_group.id:
                index = old_groups.index(g)
                break
        old_groups[index] = new_group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
