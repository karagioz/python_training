import re
from model.contact import Contact


def test_contact_info_on_home_page(app, db):
    app.contact.ensure_contact_created(Contact(firstname="test"))
    contacts_app = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(contacts_app) == len(contacts_db)
    for i in range(len(contacts_db)):
        assert contacts_app[i].lastname == contacts_db[i].lastname
        assert contacts_app[i].firstname == contacts_db[i].firstname
        assert contacts_app[i].address == contacts_db[i].address
        assert contacts_app[i].all_emails_from_home_page == merge_emails_like_on_home_page(contacts_db[i])
        assert contacts_app[i].all_phones_from_home_page == merge_phones_like_on_home_page(contacts_db[i])


# def test_phones_on_contact_view_page(app):
#     contact_from_view_page = app.contact.get_contact_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.homephone == contact_from_edit_page.homephone
#     assert contact_from_view_page.workphone == contact_from_edit_page.workphone
#     assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
#     assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            [contact.email, contact.email2, contact.email3]))
