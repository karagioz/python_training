# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="aaaaa", middlename="bbbb", lastname="cccc", nickname="ddddd", title="dddd",
                               company="eeee", address="fffff", fax="gggg", mobile="hhh", work="iii", home="gggg",
                               email="kkkk", email2="llll", email3="mmm", homepage="nnn", option1="3", option2="3",
                               byear="1990", option3="5", option4="6", ayear="2000", address2="oooo", phone2="pppp",
                               notes="qqqq")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                               fax="", mobile="", work="", home="", email="", email2="", email3="", homepage="",
                               option1="1", option2="1", byear="", option3="1", option4="1", ayear="", address2="",
                               phone2="", notes="")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
