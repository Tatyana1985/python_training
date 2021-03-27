import re
from random import randrange

from model.contact import Contact

def test_check_contact_on_homepage(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.add_contact(
            Contact(firstname="asdfg", middlename="asdfg", lastname="asdfg", nickname="asdfg", title="asdfg",
                    company="asdfg", address="asdfg", homephone="565656", mobilephone="677565", workphone="76876687",
                    fax="67678678",
                    email="rert@uyuy.try", email2="rtrt@tyty.tyty", email3="rtr@uiui.tyt", homepage="trtr@yuu.uyu",
                    day="7", month="August", year="2000",
                    address2='trtyyt', secondaryphone='75757', notes='uiygfhjkf'))
    contacts_db = orm.get_contact_list_all()
    contacts_home_page = app.contact.get_contact_list()
    for contact in contacts_db:
        contact.all_emails_from_home_page = merge_emails_like_on_home_page(contact)
        contact.all_phones_from_home_page = merge_phones_like_on_home_page(contact)
    assert len(contacts_home_page) == len(contacts_db)
    sortDb = sorted(contacts_db, key=Contact.id_or_max)
    sortPage = sorted(contacts_home_page, key=Contact.id_or_max)
    for index in range(len(contacts_home_page)):
        assert clearSpace(sortDb[index].firstname) == sortPage[index].firstname
        assert clearSpace(sortDb[index].lastname) == sortPage[index].lastname
        assert clearSpace(sortDb[index].address) == sortPage[index].address
        assert sortDb[index].all_emails_from_home_page == sortPage[index].all_emails_from_home_page
        assert sortDb[index].all_phones_from_home_page == sortPage[index].all_phones_from_home_page



def test_check_contact_by_index_on_homepage(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="asdfg", middlename="asdfg", lastname="asdfg", nickname="asdfg", title="asdfg",
                          company="asdfg", address="asdfg", homephone="565656", mobilephone="677565", workphone="76876687", fax="67678678",
                          email="rert@uyuy.try", email2="rtrt@tyty.tyty",email3="rtr@uiui.tyt", homepage="trtr@yuu.uyu",
                          day="7", month="August", year="2000",
                          address2='trtyyt', secondaryphone='75757', notes='uiygfhjkf'))
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def clearSpace(s):
    return ' '.join(s.split())

def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))
