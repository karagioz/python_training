# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_some_contact(app):
    app.contact.ensure_contact_created(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="new_firstname", middlename="new_middlename",
                      lastname="new_lastname", nickname="new_nickname", title="new_title",
                      company="new_company", address="new_address", fax="new_fax",
                      mobilephone="new_mobile", workphone="new_work", homephone="new_home", email="new_email",
                      email2="new_email2", email3="new_email3", homepage="new_homepage",
                      option1="4", option2="5", byear="1991", option3="6", option4="7",
                      ayear="2001", address2="new_address2", secondaryphone="new_phone2",
                      notes="new_notes")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
