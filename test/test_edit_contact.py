from model.contact import Contact


def test_edit_first_contact(app):
    edit_contact = Contact(firstname="qwerty", middlename="qwerty", lastname="qwerty", nickname="qwerty", title="qwerty",
                          company="qwerty", address="qwerty",
                          home="1212", mobile="54564", work="456445", fax="545345", email="54t@hj.try",
                          email2="tyty@tyty.tyty",
                          email3="tyt@uiui.tyt", homepage="rtyt@yuu.uyu", day="4", month="March", year="2001")
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="asdfg", middlename="asdfg", lastname="asdfg", nickname="asdfg", title="asdfg",
                          company="asdfg", address="asdfg",
                          home="565656", mobile="677565", work="76876687", fax="67678678", email="rert@uyuy.try",
                          email2="rtrt@tyty.tyty",
                          email3="rtr@uiui.tyt", homepage="trtr@yuu.uyu", day="7", month="August", year="2000"))

    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(edit_contact)
    edit_contact.id = old_contacts[0].id
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = edit_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)