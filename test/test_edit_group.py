from model.group import Group
import random


def test_edit_first_group_name(app, db):
    group = Group(name="Edited")
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    modified_group = random.choice(old_groups)
    group.id = modified_group.id
    app.group.edit_group_by_id(group, group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    new_groups = db.get_group_list()
    index = old_groups.index(modified_group)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_edit_first_group_header(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    app.group.edit_first_group(Group(header="headerEdited"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
