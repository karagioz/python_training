# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="new_firstname", middlename="new_middlename",
                                           lastname="new_lastname", nickname="new_nickname", title="new_title",
                                           company="new_company", address="new_address", fax="new_fax",
                                           mobile="new_mobile", work="new_work", home="new_home", email="new_email",
                                           email2="new_email2", email3="new_email3", homepage="new_homepage",
                                           option1="4", option2="5", byear="1991", option3="6", option4="7",
                                           ayear="2001", address2="new_address2", phone2="new_phone2",
                                           notes="new_notes"))
    app.session.logout()
