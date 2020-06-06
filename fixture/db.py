import pymysql.cursors


class DbFixture:
    def __init__(self, host, user, name, password):
        self.host = host
        self.user = user
        self.name = name
        self.password = password
        self.connection = pymysql.connect(host=host, database=user, user=name, password=password)

    def destroy(self):
        self.connection.close()