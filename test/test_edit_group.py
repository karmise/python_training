from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group()
    app.group.fill_group_form(Group(name="Edited", header="headerEdited", footer="footerEdited"))
    app.group.submit_edition()
    app.group.return_to_groups_page()
    app.session.logout()
