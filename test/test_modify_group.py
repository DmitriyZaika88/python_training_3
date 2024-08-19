from model.group import Group


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(name="test_rename", header="test_rename_1", footer="test_rename_2"))


# def test_modify_contact_with_title(app):
#     if app.group.count_group_name() > 0:
#         app.contact.modify_first_group(Group(name="test_rename_without_title"))
#     app.group.modify_first_group(Group(name="test_rename", header="test_rename_1", footer="test_rename_2"))
