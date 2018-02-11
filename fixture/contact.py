class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # switch to edit mode
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        self.fill_contact_form(contact)
        # submit updates
        wd.find_element_by_xpath("//input[@value='Update']").click()

    def ensure_contact_created(self, contact):
        if self.count() == 0:
            self.create(contact)

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_select_option(1, contact.option1)
        self.change_select_option(2, contact.option2)
        self.change_field_value("byear", contact.byear)
        self.change_select_option(3, contact.option3)
        self.change_select_option(4, contact.option4)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_select_option(self, select, option):
        wd = self.app.wd
        if option is not None:
            select_xpath = "//div[@id='content']/form/select[" + str(select) + "]//option[" + option + "]"
            if not wd.find_element_by_xpath(select_xpath).is_selected():
                wd.find_element_by_xpath(select_xpath).click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)
