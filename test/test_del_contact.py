from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="asdfg", middlename="asdfg", lastname="asdfg", nickname="asdfg", title="asdfg",
                          company="asdfg", address="asdfg",
                          home="565656", mobile="677565", work="76876687", fax="67678678", email="rert@uyuy.try",
                          email2="rtrt@tyty.tyty",
                          email3="rtr@uiui.tyt", homepage="trtr@yuu.uyu", day="7", month="August", year="2000"))
    app.contact.delete_first_contact()
