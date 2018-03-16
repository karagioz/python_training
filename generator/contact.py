# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                    fax="", mobilephone="", workphone="", homephone="", email="", email2="", email3="", homepage="",
                    option1="0", option2="-", byear="", option3="0", option4="-", ayear="", address2="",
                    secondaryphone="", notes="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
            title=random_string("title", 10), company=random_string("company", 15),
            address=random_string("address", 15), fax=random_string("fax", 10), mobilephone=random_string("mobile", 10),
            workphone=random_string("work", 10), homephone=random_string("home", 10), email=random_string("email", 15),
            email2=random_string("email2", 15), email3=random_string("email3", 15),
            homepage=random_string("homepage", 10), option1=1+random.randrange(30), option2=random.choice(months),
            byear=random_string("byear", 4), option3=1+random.randrange(30), option4=random.choice(months),
            ayear=random_string("ayear", 4), address2=random_string("address2", 15),
            secondaryphone=random_string("secondary", 10), notes=random_string("notes", 15))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
