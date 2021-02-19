from model.group import Group

def test_edit_first_group(app):
    edit_group = Group(name="erwew", header="eqweq", footer="ouiou")
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(edit_group)
    app.session.logout()