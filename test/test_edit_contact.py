from model.contact import Contact


def test_edit_first_contact(app):
    edit_contact = Contact(firstname="qwerty", middlename="qwerty", lastname="qwerty", nickname="qwerty", title="qwerty",
                          company="qwerty", address="qwerty",
                          home="1212", mobile="54564", work="456445", fax="545345", email="54t@hj.try",
                          email2="tyty@tyty.tyty",
                          email3="tyt@uiui.tyt", homepage="rtyt@yuu.uyu", day="4", month="March", year="2001")
    app.contact.edit_first_contact(edit_contact)
