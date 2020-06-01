from model.contact import Contact
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                    address="", home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="",
                    bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", address2="",
                    phone2="", notes="")] + [
               Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                       lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                       title=random_string("title", 20), company=random_string("company", 10),
                       address=random_string("address", 20), home="+7111",
                       mobile="+72222", work="+7333",
                       fax="+74444", email=random_string("email", 20), email2=random_string("email2", 10),
                       email3=random_string("email3", 10),
                       homepage=random_string("homepage", 10), bday="11",
                       bmonth="May", byear="2010",
                       aday="13", amonth="September",
                       ayear="2020", address2=random_string("address2", 10),
                       phone2="+755555", notes=random_string("notes", 10), )
               for i in range(5)
           ]
