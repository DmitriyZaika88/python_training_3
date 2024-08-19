
from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create_contact(Contact(title="loremipsum",
                                           company="test_loremipsum",
                                           address="test_loremipsum",
                                           home="test_loremipsum",
                                           mobile="test_loremipsum",
                                           work="test_loremipsum",
                                           fax="test_loremipsum",
                                           email_1="test_loremipsum",
                                           email_2="test_loremipsum",
                                           email_3="test_loremipsum"))
    app.contact.modify_first_contact(Contact(title="new_test",
                                             company="market",
                                             address="Saint-Petersburg",
                                             home="new_home",
                                             mobile="secret",
                                             work="QA",
                                             fax="new_fax",
                                             email_1="modified_email@gmail.com",
                                             email_2="modified_email2@gmail.com",
                                             email_3="modified_email3@gmail.com"))


def test_modify_contact_with_title(app):
    if app.contact.count_contact_first_name() > 0:
        app.contact.modify_first_contact(Contact(first_name="test_rename"))
