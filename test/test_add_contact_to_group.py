from model.group import Group
from model.contact import Contact
import random
import pytest


def test_add_contact_to_group(app, db, orm):
    with pytest.allure.step('Given a non-empty contact list'):
        app.contact.ensure_contact_created(Contact(firstname="test"))
    with pytest.allure.step('Given a non-empty group list'):
        app.group.ensure_group_created(Group(name="test"))
    with pytest.allure.step('Given a random contact from the list'):
        contacts = db.get_contact_list()
        contact = random.choice(contacts)
    with pytest.allure.step("Given a random group which doesn't contain this contact"):
        # choose group which doesn't contain this contact
        groups = orm.get_groups_not_with_contact(contact)
        if len(groups) != 0:
            group = random.choice(groups)
        else:
            app.group.create(Group(name="group to add contact"))
            group = sorted(db.get_group_list(), key=Group.id_or_max)[-1]
    with pytest.allure.step('When I add the contact to the group'):
        app.contact.add_contact_to_group(contact, group)
    with pytest.allure.step('Then the group contains this contact'):
        assert (contact in orm.get_contacts_in_group(group))
