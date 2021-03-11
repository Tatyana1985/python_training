from random import randrange

from model.contact import Contact

def test_delete_contact_by_index(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="asdfg", middlename="asdfg", lastname="asdfg", nickname="asdfg", title="asdfg",
                          company="asdfg", address="asdfg", homephone="565656", mobilephone="677565", workphone="76876687", fax="67678678",
                          email="rert@uyuy.try", email2="rtrt@tyty.tyty",email3="rtr@uiui.tyt", homepage="trtr@yuu.uyu",
                          day="7", month="August", year="2000",
                          address2='trtyyt', secondaryphone='75757', notes='uiygfhjkf'))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

