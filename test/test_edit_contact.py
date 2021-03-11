from random import randrange

from model.contact import Contact


def test_edit_first_contact(app):
    edit_contact = Contact(firstname="qwerty", middlename="qwerty", lastname="qwerty", nickname="qwerty", title="qwerty",
                          company="qwerty", address="qwerty",
                          homephone="1212", mobilephone="54564", workphone="456445", fax="545345", email="54t@hj.try",
                          email2="tyty@tyty.tyty",
                          email3="tyt@uiui.tyt", homepage="rtyt@yuu.uyu", day="4", month="March", year="2001",
                          address2="trtyyt", secondaryphone="75757", notes="uiygfhjkf")
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="asdfg", middlename="asdfg", lastname="asdfg", nickname="asdfg", title="asdfg",
                          company="asdfg", address="asdfg",
                          homephone="565656", mobilephone="677565", workphone="76876687", fax="67678678", email="rert@uyuy.try",
                          email2="rtrt@tyty.tyty",
                          email3="rtr@uiui.tyt", homepage="trtr@yuu.uyu", day="7", month="August", year="2000",
                          address2="trtyyt", secondaryphone="75757", notes="uiygfhjkf"))

    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    edit_contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, edit_contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = edit_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)