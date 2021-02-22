from model.group import Group

def test_edit_first_group(app):
    edit_group = Group(name="erwew", header="eqweq", footer="ouiou")
    app.group.edit_first_group(edit_group)
