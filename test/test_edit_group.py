from model.group import Group


def test_edit_first_group_name(app):
    old_groups = app.group.get_group_list()
    group = Group(name="Edited")
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
        old_groups = app.group.get_group_list()
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_edit_first_group_header(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    app.group.edit_first_group(Group(header="headerEdited"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
