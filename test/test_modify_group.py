from model.group import Group


def test_modify_group(app):
    app.group.modify_first_group(Group(name="test_rename", header="test_rename_1", footer="test_rename_2"))
