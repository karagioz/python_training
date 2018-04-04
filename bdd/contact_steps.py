from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <firstname>, <middlename>, <lastname>, <nickname>, <title>, <company>, <address>, <fax>, <mobilephone>, <workphone>, <homephone>, <email>, <email2>, <email3>, <homepage>, <option1>, <option2>, <byear>, <option3>, <option4>, <ayear>, <address2>, <secondaryphone> and <notes>')
def new_contact(firstname, middlename, lastname, nickname, title, company, address, fax, mobilephone, workphone,
                homephone, email, email2, email3, homepage, option1, option2, byear, option3, option4, ayear, address2,
                secondaryphone, notes):
    return Contact(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname, title=title,
                   company=company, address=address, fax=fax, mobilephone=mobilephone, workphone=workphone,
                   homephone=homephone, email=email, email2=email2, email3=email3, homepage=homepage, option1=option1,
                   option2=option2, byear=byear, option3=option3, option4=option4, ayear=ayear, address2=address2,
                   secondaryphone=secondaryphone, notes=notes)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then('the new contact list is equal the old list with the added contact')
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(name='some name'))
    return db.get_contact_list()


@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@then('the new contact list is equal the old list without the deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@when('I edit the contact according to the new contact information')
def edit_contact(app, random_contact, new_contact):
    app.contact.edit_contact_by_id(random_contact.id, new_contact)


@then('the new contact list is equal the old list with the updated contact')
def verify_contact_edited(db, non_empty_contact_list, random_contact, new_contact):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    index = -1
    for c in old_contacts:
        if c.id == random_contact.id:
            index = old_contacts.index(c)
            break
    new_contact.id = random_contact.id
    old_contacts[index] = new_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
