from model.contact import Contact


def test_modify_first_contact(app):
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

