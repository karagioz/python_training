# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_edit_some_contact(app, db, check_ui):
    app.contact.ensure_contact_created(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    old_contact = random.choice(old_contacts)
    new_contact = Contact(id=old_contact.id, firstname="new_firstname", middlename="new_middlename",
                      lastname="new_lastname", nickname="new_nickname", title="new_title",
                      company="new_company", address="new_address", fax="new_fax",
                      mobilephone="new_mobile", workphone="new_work", homephone="new_home", email="new_email",
                      email2="new_email2", email3="new_email3", homepage="new_homepage",
                      option1="4", option2="May", byear="1991", option3="6", option4="october",
                      ayear="2001", address2="new_address2", secondaryphone="new_phone2",
                      notes="new_notes")
    app.contact.edit_contact_by_id(old_contact.id, new_contact)
    new_contacts = db.get_contact_list()
    index = -1
    for c in old_contacts:
        if c.id == old_contact.id:
            index = old_contacts.index(c)
            break
    old_contacts[index] = new_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
