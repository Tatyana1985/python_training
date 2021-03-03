from model.group import Group

def test_edit_first_group(app):
    edit_group = Group(name="erwew", header="eqweq", footer="ouiou")
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(edit_group)
    edit_group.id = old_groups[0].id
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = edit_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
