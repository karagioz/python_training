# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                      fax="", mobilephone="", workphone="", homephone="", email="", email2="", email3="", homepage="",
                      option1="1", option2="1", byear="", option3="1", option4="1", ayear="", address2="",
                      secondaryphone="", notes="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
            title=random_string("title", 10), company=random_string("company", 15), address=random_string("address", 15),
            fax=random_string("fax", 10), mobilephone=random_string("mobile", 10), workphone=random_string("work", 10),
            homephone=random_string("home", 10), email=random_string("email", 15), email2=random_string("email2", 15),
            email3=random_string("email3", 15), homepage=random_string("homepage", 10), option1=random.randrange(32),
            option2=random.randrange(13), byear=random_string("byear", 4), option3=random.randrange(32),
            option4=random.randrange(13), ayear=random_string("ayear", 4), address2=random_string("address2", 15),
            secondaryphone=random_string("secondary", 10), notes=random_string("notes", 15))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
