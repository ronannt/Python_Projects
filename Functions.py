import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
import mysql.connector
from mysql.connector import errorcode


class Primary_Functions:
    def Login(self, user, password):
        try:
            self.conn = mysql.connector.connect(host='''localhost''', user=user, password=password, database='''data''')
            print("Database connection made!")
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                print("Server not available!")
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Wrong Password or User!")
            else:
                print(error)
        else:
            print("Unknow error!")
                
