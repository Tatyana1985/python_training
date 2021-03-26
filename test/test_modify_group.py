import random

from model.group import Group

def test_modify_group_name(app, db, check_ui):
    group_edit = Group(name="New group")
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="group"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    index = old_groups.index(group)
    app.group.modify_group_by_id(group.id, group_edit)
    group_edit.id = group.id
    old_groups[index] = group_edit
    new_groups = db.get_group_list()
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



#def test_modify_group_header(app):
    #old_groups = app.group.get_group_list()
    #app.group.modify_first_group(Group(header="New header"))
    #assert len(old_groups) == app.group.count()
    #new_groups = app.group.get_group_list()