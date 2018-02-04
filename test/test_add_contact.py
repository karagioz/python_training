# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="aaaaa", middlename="bbbb", lastname="cccc", nickname="ddddd", title="dddd",
                               company="eeee", address="fffff", fax="gggg", mobile="hhh", work="iii", home="gggg",
                               email="kkkk", email2="llll", email3="mmm", homepage="nnn", option1="3", option2="3",
                               byear="1990", option3="5", option4="6", ayear="2000", address2="oooo", phone2="pppp",
                               notes="qqqq"))
    app.open_home_page()
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                               fax="", mobile="", work="", home="", email="", email2="", email3="", homepage="",
                               option1="1", option2="1", byear="", option3="1", option4="1", ayear="", address2="",
                               phone2="", notes=""))
    app.open_home_page()
    app.logout()
