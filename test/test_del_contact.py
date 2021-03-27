from random import randrange
import random
from model.contact import Contact

def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact(Contact(firstname="asdfg", middlename="asdfg", lastname="asdfg", nickname="asdfg", title="asdfg",
                          company="asdfg", address="asdfg", homephone="565656", mobilephone="677565", workphone="76876687", fax="67678678",
                          email="rert@uyuy.try", email2="rtrt@tyty.tyty",email3="rtr@uiui.tyt", homepage="trtr@yuu.uyu",
                          day="7", month="August", year="2000",
                          address2="trtyyt", secondaryphone="75757", notes="uiygfhjkf"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)

    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                      key=Contact.id_or_max)
