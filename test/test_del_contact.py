
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create_contact(Contact(first_name="alex",
                                           middle_name="wellington",
                                           last_name="Andressen",
                                           nickname="Andy",
                                           title="test"))
    app.contact.delete_first_contact()
