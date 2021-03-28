from model.contact import Contact
from model.group import Group
import random

def test_delete_contact_in_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(orm.get_contact_list()) == 0:
        app.contact.add_contact(Contact(firstname="asdfg", middlename="asdfg", lastname="asdfg", nickname="asdfg", title="asdfg",
                          company="asdfg", address="asdfg", homephone="565656", mobilephone="677565", workphone="76876687", fax="67678678",
                          email="rert@uyuy.try", email2="rtrt@tyty.tyty",email3="rtr@uiui.tyt", homepage="trtr@yuu.uyu",
                          day="7", month="August", year="2000",
                          address2="trtyyt", secondaryphone="75757", notes="uiygfhjkf"))
    contact = random.choice(orm.get_contact_list())
    group = random.choice(orm.get_group_list())
    if len(orm.get_groups_this_contacts(contact)) == 0:
        app.contact.add_contact_in_group(contact, group)
    groups_this_contacts_before = orm.get_groups_this_contacts(contact)
    group_for_del = random.choice(groups_this_contacts_before)
    app.contact.delete_contact_in_group(contact, group_for_del)
    groups_this_contacts_after = orm.get_groups_this_contacts(contact)
    groups_this_contacts_before.remove(group)
    assert sorted(groups_this_contacts_before, key=Contact.id_or_max) == sorted(groups_this_contacts_after, key=Contact.id_or_max)