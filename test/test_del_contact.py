# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    app.contact.ensure_contact_created(Contact(firstname="test"))
    app.contact.delete_first_contact()
