from fixture.db import DbFixture

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")


#try:
#    groups = db.get_group_list()
#    for group in groups:
#        print(group)
#    print(len(groups))
#finally:
#    db.destroy()

try:
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    db.destroy()