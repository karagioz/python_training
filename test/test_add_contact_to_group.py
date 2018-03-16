from model.group import Group
from model.contact import Contact
import random


def test_add_contact_to_group(app, db, orm):
    app.contact.ensure_contact_created(Contact(firstname="test"))
    app.group.ensure_group_created(Group(name="test"))
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    # choose group which doesn't contain this contact
    groups = orm.get_groups_not_with_contact(contact)
    if len(groups) != 0:
        group = random.choice(groups)
    else:
        app.group.create(Group(name="group to add contact"))
        group = sorted(db.get_group_list(), key=Group.id_or_max)[-1]
    app.contact.add_contact_to_group(contact, group)
    assert (contact in orm.get_contacts_in_group(group))
