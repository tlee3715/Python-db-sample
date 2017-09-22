import pymysql


class DatabaseConnector:
    "This class is used as the back end to connect to our database"

    def __init__(self, hostname, username, password, databaseName):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.databaseName = databaseName

    def openDBConnection(self):
        self.db = pymysql.connect(self.hostname,self.username,self.password,self.databaseName)
        
    def closeDBConnection(self):
        self.db.close()
        
    def insert(self,Fname,Lname,IDNumber,GPA):
        try:
            self.openDBConnection()
            cursor = self.db.cursor()
            sql = "INSERT INTO Students(fname,lname,IDNumber,GPA) VALUES('"+ Fname + "','" + Lname + "'," + str(IDNumber) + "," + str(GPA) + ")"
            rowAffected = cursor.execute(sql)
            self.closeDBConnection()
            print("Data inserted successfully ! " + str(rowAffected) + " row affected")
        except Exception as arg:
            print("Error !",arg)

    def update(self,Fname,Lname,IDNumber,GPA):
        try:
            self.openDBConnection()
            cursor = self.db.cursor()
            sql = "UPDATE Students SET fname = '" + Fname + "', lname = '" + Lname + "', GPA = " + str(GPA) + " WHERE IDNumber = " + str(IDNumber)
            rowAffected = cursor.execute(sql)
            self.closeDBConnection()
            print("Data updated successfully ! "  + str(rowAffected) + " row affected")
        except Exception as arg:
            print("Error !",arg)

    def remove(self,IDNumber):
        try:
            self.openDBConnection()
            cursor = self.db.cursor()
            sql = "DELETE FROM Students WHERE IDNumber = " + str(IDNumber)
            rowAffected = cursor.execute(sql)
            self.closeDBConnection()
            print("Data removed successfully ! "  + str(rowAffected) + " row affected")
        except Exception as arg:
            print("Error !",arg)

    def get(self,IDNumber):
        try:
            self.openDBConnection()
            cursor = self.db.cursor()
            sql = "SELECT fname,lname,IDNumber, GPA FROM Students WHERE IDNumber= " + str(IDNumber)
            data = cursor.execute(sql)
            self.closeDBConnection()
            print("Data retrieved successfully ! Retrieved " + str(data) + " row of data")
        except Exception as arg:
            print("Error !",arg)
