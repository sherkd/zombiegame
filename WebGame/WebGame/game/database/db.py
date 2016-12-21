from django.test import TestCase
import pymysql

class Database(object):

    def __init__(self):
        self.database = pymysql.connect(host="104.219.248.113",    # your host, usually localhost
                         user="amatfbgg_infdev6",         # your username
                         passwd="DbX3xb6K#nyE",  # your password
                         db="amatfbgg_infdev06b")        # name of the data base
    def getDB(self):
        return self.database

    def connect(self):
        cur = self.db.cursor()
        return cur.execute("Create Table Users (id int(25))")

    """
class TestDatabase(TestCase):

    
    def testDB(self):
        db = Database()
       
        con = pymysql.connect(host="104.219.248.111",    # your host, usually localhost
                         user="amatfbgg_infdev6",         # your username
                         passwd="DbX3xb6K#nyE",  # your password
                         db="amatfbgg_infdev06b")        # name of the data base
        self.assertAlmostEquals(con, db.getDB())
    """