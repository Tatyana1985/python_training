from model.group import Group

def test_edit_first_group(app):
    edit_group = Group(name="erwew", header="eqweq", footer="ouiou")
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit_first_group(edit_group)
