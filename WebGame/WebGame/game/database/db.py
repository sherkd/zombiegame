class Database(object):

    def __init__(self):
        self.db = pymysql.connect(host="104.219.248.113 ",    # your host, usually localhost
                         user="amatfbgg_infdev6",         # your username
                         passwd="DbX3xb6K#nyE",  # your password
                         db="amatfbgg_infdev06b")        # name of the data base
    def getDB(self):
        return self.db

    def connect(self):
        cur = db.cursor()
        return cur.execute("Create Table Users (id int(25))")