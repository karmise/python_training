from model.group import Group


def test_edit_first_group_name(app):
    app.group.edit_first_group(Group(name="Edited"))


def test_edit_first_group_header(app):
    app.group.edit_first_group(Group(header="headerEdited"))
