from mysql import connector

class Connection:
    def __init__(self, host = None, user = None, password = None, database = None):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database
        self.__conn = self.__buildConnection(host, user, password, database)

    def __buildConnection(self, host = None, user = None, password = None, database = None):
        conn = connector.connect(host=host,
                                 user=user,
                                 password=password,
                                 database=database)
        return conn

    def getCursor(self):
        """
        :return: Cursor MySQL care suporta comenzi trimise ca String
        """
        return self.__conn.cursor()

