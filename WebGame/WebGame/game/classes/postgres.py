import psycopg2
import sys

class Postgres(object):  

    def __init__(self):
        conn_string = "host='localhost' dbname='zombiegamers' user='postgres' password='project3'"
        print("Connecting to database\n	->%s" % (conn_string))
        self.connection = psycopg2.connect(conn_string)
        self.cursor = self.connection.cursor()

    def getConnection(self):
        return self.connection

    def createDatabase(self):
        self.cursor.execute("CREATE TABLE Account(userid int NOT NULL, password varchar(255), username varchar(255), gender varchar(1), email varchar(255), birthday date, PRIMARY KEY(userid))")
        self.cursor.execute("CREATE TABLE Player(userid int NOT NULL, health int, attack int , luck int, accuracy int, speed int, skillpoints int, weaponid int, FOREIGN KEY(userid) REFERENCES Account(userid))")
        self.cursor.execute("CREATE TABLE Weapon(weaponid int NOT NULL, name varchar(255), class varchar(255), description varchar(255), level int, damage int, PRIMARY KEY(weaponid))")
        self.cursor.execute("CREATE TABLE Player_Weapon(userid int NOT NULL, weaponid int NOT NULL, FOREIGN KEY(userid) REFERENCES Account(userid), FOREIGN KEY(weaponid) REFERENCES Weapon(weaponid))")

    def getAccount(self):
        self.cursor.execute("SELECT * FROM Account WHERE userid='12'")
        return self.cursor.fetchone()

    def insertAccount(self):
        try:
            self.cursor.execute("INSERT INTO Account (userid, password, username, gender, email, birthday) Values(12, 'pass', 'user', 'm', 'user@gmail.com', '2000-10-10')")
            self.connection.commit()
        except:
            self.connection.rollback()

    def insertTestPlayer(self):
        try:
            self.cursor.execute("DELETE FROM Player WHERE userid = '12'")
            self.connection.commit()
        except:
            self.connection.rollback()

        try:
            self.cursor.execute("INSERT INTO Player(userid, health, attack, luck, accuracy, speed, skillpoints, weaponid) VALUES(12, 100, 10, 5, 10, 10, 0, 12);")
            self.connection.commit()
        except:
            self.connection.rollback()

    def getTestPlayer(self):
        self.cursor.execute("SELECT * FROM Player WHERE userid='12'")
        return self.cursor.fetchone()

    def insertWeapon(self, weapon):
        id = random.randint(0, 1000)
        try:
            self.cursor.execute("INSERT INTO Weapon (userid, name, class, description, level, damage) VALUES (" + str(id) + "," + weapon.getName() + "," + weapon.getClass() + "," + weapon.getDescription() + "," + str(weapon.getLevel()) + "," + str(weapon.getDamage()) + ")")
            self.connection.commit()
        except:
            self.connection.rollback()

    def getWeapon(self):
        print(self.cursor.execute("SELECT * FROM Weapon WHERE userid='12'"))

    def getWeapon(self, id):
        pass

    def getWeapons(self, username):
        pass

      
