from model.group import Group
from model.contact import Contact
import random
import pytest


def test_remove_contact_from_group(app, db, orm):
    with pytest.allure.step('Given a non-empty list of groups which include some contacts'):
        groups = orm.get_groups_with_any_contacts()
        if len(groups) != 0:
            group = random.choice(groups)
            contacts = orm.get_contacts_in_group(group)
        else:
            app.contact.ensure_contact_created(Contact(firstname="test"))
            app.group.ensure_group_created(Group(name="test"))
            groups = db.get_group_list()
            group = random.choice(groups)
            contacts = db.get_contact_list()
    with pytest.allure.step('Given a random contact from a random group'):
        contact = random.choice(contacts)
        if contact not in orm.get_contacts_in_group(group):
            app.contact.add_contact_to_group(contact, group)
            assert (contact in orm.get_contacts_in_group(group))
    with pytest.allure.step('When I remove the contact from the group'):
        app.contact.remove_contact_from_group(contact, group)
    with pytest.allure.step('Then the group does not contain this contact any more'):
        assert (contact not in orm.get_contacts_in_group(group))
