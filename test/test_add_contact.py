# -*- coding: utf-8 -*-
from model.contact import Contact
import string
import random
import pytest

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

def random_dig_string(maxlen):
    symbols = string.digits + " "
    return "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

def random_date(minlen, maxlen):
    return random.randrange(minlen,maxlen)

def random_month():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]
    return months[random.randrange(len(months))]

empty = Contact(firstname="", middlename="", lastname="", nickname="",
                    title="", company="", address="",
                    homephone="", mobilephone="", workphone="", fax="",
                    email="", email2="", email3="", homepage="",
                    day="", month="", year="",
                    address2="", secondaryphone="", notes="")
testdata = [empty] + [
            Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                    title=random_string("title", 10), company=random_string("company", 10), address=random_string("address", 10),
                    homephone=random_dig_string(10), mobilephone=random_dig_string(10), workphone=random_dig_string(10), fax=random_dig_string(10),
                    email=random_string("email", 5), email2=random_string("email2", 5), email3=random_string("email3", 5), homepage=random_string("homepage", 5),
                    day=str(random_date(1, 31)), month=random_month(), year=str(random_date(1900, 2020)),
                    address2=random_string("address2", 5), secondaryphone=random_dig_string(10), notes=random_string("notes", 5))
    for i in range(2)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)








