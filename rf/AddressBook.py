import json
import os.path
from fixture.application import Application
from fixture.db import DbFixture
from model.group import Group
from model.contact import Contact


class AddressBook:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, config="target.json", browser="chrome"):
        self.browser = browser
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with open(config_file) as f:
            self.target = json.load(f)

    def init_fixtures(self):
        web_config = self.target['web']
        self.fixture = Application(browser=self.browser, base_url=web_config["baseUrl"])
        self.fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
        db_config = self.target['db']
        self.dbFixture = DbFixture(host=db_config["host"], name=db_config["name"], user=db_config["user"],
                              password=db_config["password"])

    def destroy_fixtures(self):
        self.dbFixture.destroy()
        self.fixture.destroy()

    def new_group(self, name, header, footer):
        return Group(name=name, header=header, footer=footer)

    def get_group_list(self):
        return self.dbFixture.get_group_list()

    def create_group(self, group):
        self.fixture.group.create(group)

    def delete_group(self, group):
        self.fixture.group.delete_group_by_id(group.id)

    def group_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Group.id_or_max) == sorted(list2, key=Group.id_or_max)

    def new_contact(self, firstname, middlename, lastname, nickname, title, company, address, fax, mobilephone,
                    workphone, homephone, email, email2, email3, homepage, option1, option2, byear, option3, option4,
                    ayear, address2, secondaryphone, notes):
        return Contact(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname, title=title,
                       company=company, address=address, fax=fax, mobilephone=mobilephone, workphone=workphone,
                       homephone=homephone, email=email, email2=email2, email3=email3, homepage=homepage,
                       option1=option1, option2=option2, byear=byear, option3=option3, option4=option4, ayear=ayear,
                       address2=address2, secondaryphone=secondaryphone, notes=notes)

    def get_contact_list(self):
        return self.dbFixture.get_contact_list()

    def create_contact(self, contact):
        self.fixture.contact.create(contact)

    def delete_contact(self, contact):
        self.fixture.contact.delete_contact_by_id(contact.id)

    def edit_contact(self, contact, new_contact):
        self.fixture.contact.edit_contact_by_id(contact.id, new_contact)

    def fix_new_contact_id(self, contact, new_contact):
        new_contact.id = contact.id
        return new_contact

    def contact_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Contact.id_or_max) == sorted(list2, key=Contact.id_or_max)
