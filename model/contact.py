from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, fax=None, mobilephone=None, workphone=None, homephone=None, email=None, email2=None,
                 email3=None, homepage=None, option1=None, option2=None, byear=None, option3=None, option4=None,
                 ayear=None, address2=None, secondaryphone=None, notes=None, id=None, all_phones_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.fax = fax
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.homephone = homephone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.option1 = option1
        self.option2 = option2
        self.byear = byear
        self.option3 = option3
        self.option4 = option4
        self.ayear = ayear
        self.address2 = address2
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname \
               and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
